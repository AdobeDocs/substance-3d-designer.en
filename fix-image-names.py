#!/usr/bin/env python3
"""
Renames image files in help/assets that contain parenthesised numbers
(e.g. "foo(1).png" -> "foo_1.png") and updates all image links in every
Markdown file under the repo root to point to the new filenames.
"""

import os
import re
import sys

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(REPO_ROOT, "help", "assets")

# Matches a parenthesised number immediately before the file extension,
# e.g. "foo(1).png", "bar(12).gif"
PAREN_NUMBER_RE = re.compile(r"^(.+)\((\d+)\)(\.[^.]+)$")

# Image extensions we care about (lowercase)
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp"}

# ---------------------------------------------------------------------------
# Step 1 – Rename files and build the rename map
# ---------------------------------------------------------------------------

rename_map: dict[str, str] = {}  # old basename -> new basename

print("=== Scanning for files to rename ===\n")

for filename in sorted(os.listdir(ASSETS_DIR)):
    m = PAREN_NUMBER_RE.match(filename)
    if not m:
        continue

    stem, number, ext = m.group(1), m.group(2), m.group(3)

    if ext.lower() not in IMAGE_EXTENSIONS:
        continue

    new_filename = f"{stem}_{number}{ext}"

    old_path = os.path.join(ASSETS_DIR, filename)
    new_path = os.path.join(ASSETS_DIR, new_filename)

    if os.path.exists(new_path):
        print(f"  SKIP  {filename}  ->  {new_filename}  (target already exists)")
        continue

    os.rename(old_path, new_path)
    rename_map[filename] = new_filename
    print(f"  RENAMED  {filename}  ->  {new_filename}")

if not rename_map:
    print("  No files needed renaming.")

print(f"\nTotal files renamed: {len(rename_map)}\n")

# ---------------------------------------------------------------------------
# Step 2 – Update Markdown files
# ---------------------------------------------------------------------------


def collect_md_files(root: str) -> list[str]:
    """Return every .md file under *root* (recursive)."""
    md_files = []
    for dirpath, _dirnames, filenames in os.walk(root):
        for fname in filenames:
            if fname.lower().endswith(".md"):
                md_files.append(os.path.join(dirpath, fname))
    return md_files


def update_md_file(filepath: str, rename_map: dict[str, str]) -> int:
    """
    Replace every occurrence of an old image basename with the new one inside
    a Markdown file.  Returns the number of substitutions made.
    """
    with open(filepath, "r", encoding="utf-8") as fh:
        content = fh.read()

    original = content
    total_replacements = 0

    for old_name, new_name in rename_map.items():
        # Replace only the bare filename portion so we don't corrupt the
        # surrounding Markdown link syntax.
        count = content.count(old_name)
        if count:
            content = content.replace(old_name, new_name)
            total_replacements += count

    if content != original:
        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write(content)

    return total_replacements


if rename_map:
    print("=== Updating Markdown files ===\n")

    md_files = collect_md_files(REPO_ROOT)
    files_updated = 0

    for md_path in sorted(md_files):
        replacements = update_md_file(md_path, rename_map)
        if replacements:
            rel = os.path.relpath(md_path, REPO_ROOT)
            print(f"  UPDATED  {rel}  ({replacements} substitution(s))")
            files_updated += 1

    print(f"\nTotal Markdown files updated: {files_updated}")
else:
    print("No renames were made, so no Markdown files need updating.")

print("\nDone.")
