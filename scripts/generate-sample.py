#!/usr/bin/env python3
"""Generate an all-samples entry from a YAML sample definition."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
import unicodedata
from pathlib import Path
from typing import Any

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SAMPLES_PAGE = REPOSITORY_ROOT / "help/learning-tutorials/all-samples/all-samples.md"
SNIPPETS_FILE = REPOSITORY_ROOT / "help/_includes/snippets.md"
RESOURCES_DIR = REPOSITORY_ROOT / "help/learning-tutorials/all-samples/all-samples.resources"
SAMPLE_ITEM_MARKER = "<!-- sample-item -->"
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
SNIPPET_HEADING_RE = re.compile(
    r"^## Sample: .+ \{#sample-(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)\}$",
    re.MULTILINE,
)


def slugify(title: str) -> str:
    normalized = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", normalized).strip("-").lower()
    if not slug:
        raise ValueError("Title must contain at least one letter or number")
    return slug


def load_sample(path: Path) -> dict[str, str]:
    with path.open(encoding="utf-8") as stream:
        data: Any = yaml.safe_load(stream)

    if not isinstance(data, dict):
        raise ValueError("YAML root must be a mapping")

    required = {"Title", "File", "Description", "Illustration", "Minimum version"}
    missing = sorted(required - data.keys())
    if missing:
        raise ValueError(f"Missing required field(s): {', '.join(missing)}")

    sample = {}
    for key in required:
        value = data[key]
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{key} must be a non-empty string")

        value = value.strip()
        if key != "Description" and "\n" in value:
            raise ValueError(f"{key} must be a single-line string")

        sample[key] = value

    file_suffix = Path(sample["File"]).suffix.lower()
    if file_suffix not in {".sbs", ".zip"}:
        raise ValueError("File must have a .sbs or .zip extension")
    if Path(sample["Illustration"]).suffix.lower() not in {".png", ".jpg", ".jpeg"}:
        raise ValueError("Illustration must have a .png, .jpg, or .jpeg extension")
    if not VERSION_RE.fullmatch(sample["Minimum version"]):
        raise ValueError("Minimum version must use the form <int>.<int>.<int>")
    return sample


def relative_asset_path(filename: str) -> str:
    return f"all-samples.resources/{Path(filename).name}"


def render_description(description: str) -> str:
    paragraphs = re.split(r"\n\s*\n", description)
    return "".join(
        f"<p>{paragraph.replace(chr(10), '<br>')}</p>" for paragraph in paragraphs
    )


def render_snippet(sample: dict[str, str], slug: str) -> str:
    illustration = relative_asset_path(sample["Illustration"])
    download = relative_asset_path(sample["File"])
    return "\n".join(
        [
            f"## Sample: {sample['Title']} {{#sample-{slug}}}",
            "",
            '<tr style="border: 0">',
            '    <td style="border: 0; width: 90px; vertical-align: top; padding-top: 30px">',
            f'        <img src="{illustration}" alt="{sample["Title"]}" width="128" />',
            "    </td>",
            '    <td style="border: 0">',
            f"        <h3>{sample['Title']}</h3>",
            f"        {render_description(sample['Description'])}",
            f"        <p><i>Minimum version: {sample['Minimum version']}</i></p>",
            "    </td>",
            '    <td style="border: 0; width: 90px; vertical-align: top; padding-top: 30px">',
            f'        <a href="{download}"><img src="all-samples.resources/sbs-file-icon.png" alt="Download sample project" width="64" /></a>',
            "    </td>",
            "</tr>",
            "",
        ]
    )


def confirm(prompt: str) -> bool:
    answer = input(f"{prompt} [y/N] ").strip().lower()
    return answer in {"y", "yes"}


def replace_or_append_snippet(content: str, snippet: str, slug: str) -> tuple[str, bool]:
    matches = list(SNIPPET_HEADING_RE.finditer(content))
    matching = [match for match in matches if match.group("slug") == slug]
    if not matching:
        return content.rstrip() + "\n\n" + snippet, False

    match = matching[0]
    next_heading = re.search(r"^## ", content[match.end() :], re.MULTILINE)
    end = match.end() + next_heading.start() if next_heading else len(content)
    return content[: match.start()] + snippet + content[end:].lstrip("\n"), True


def update_page(content: str, reference: str, slug: str, replace: bool) -> str:
    reference_re = re.compile(rf"^\{{\{{sample-{re.escape(slug)}\}}\}}\s*$", re.MULTILINE)
    matches = list(reference_re.finditer(content))
    if matches:
        if not replace:
            raise ValueError(f"Page reference sample-{slug} already exists")
        content = reference_re.sub("", content).replace("\n\n\n", "\n\n")

    marker_index = content.find(SAMPLE_ITEM_MARKER)
    if marker_index < 0:
        raise ValueError(f"Could not find {SAMPLE_ITEM_MARKER} in {SAMPLES_PAGE}")
    return content[:marker_index].rstrip() + f"\n{reference}\n\n" + content[marker_index:]


def copy_asset(source: Path, destination: Path, allow_replace: bool) -> None:
    if not source.is_file():
        raise ValueError(f"Asset does not exist: {source}")
    if destination.exists() and not allow_replace:
        raise ValueError(f"Asset already exists: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def generate(yaml_path: Path) -> None:
    sample = load_sample(yaml_path)
    slug = slugify(sample["Title"])
    snippet = render_snippet(sample, slug)
    snippets_content = SNIPPETS_FILE.read_text(encoding="utf-8")
    page_content = SAMPLES_PAGE.read_text(encoding="utf-8")
    new_snippets, replacing_snippet = replace_or_append_snippet(snippets_content, snippet, slug)
    reference = f"{{{{sample-{slug}}}}}"
    existing_reference = f"{{{{sample-{slug}}}}}" in page_content

    if replacing_snippet or existing_reference:
        if not confirm(f"sample-{slug} already exists; replace it"):
            raise RuntimeError("Cancelled")

    sources = [yaml_path.parent / sample["File"], yaml_path.parent / sample["Illustration"]]
    destinations = [RESOURCES_DIR / Path(path).name for path in (sample["File"], sample["Illustration"])]
    replacements = []
    for source, destination in zip(sources, destinations):
        replace_asset = destination.exists()
        if replace_asset and not confirm(f"{destination.name} already exists; replace it"):
            raise RuntimeError("Cancelled")
        replacements.append((source, destination, replace_asset))

    new_page = update_page(page_content, reference, slug, replacing_snippet or existing_reference)
    for source, destination, replace_asset in replacements:
        copy_asset(source, destination, replace_asset)
    SNIPPETS_FILE.write_text(new_snippets, encoding="utf-8")
    SAMPLES_PAGE.write_text(new_page, encoding="utf-8")
    print(f"Generated sample-{slug}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("yaml_file", type=Path)
    args = parser.parse_args()
    try:
        generate(args.yaml_file.resolve())
    except (OSError, RuntimeError, ValueError, yaml.YAMLError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
