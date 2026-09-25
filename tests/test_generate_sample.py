import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts/generate-sample.py"
SPEC = importlib.util.spec_from_file_location("generate_sample", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class GenerateSampleTests(unittest.TestCase):
    def test_slugify(self):
        self.assertEqual(MODULE.slugify("My Fancy Sample!"), "my-fancy-sample")

    def test_load_sample_and_render(self):
        with tempfile.TemporaryDirectory() as directory:
            yaml_file = Path(directory) / "sample.yml"
            yaml_file.write_text(
                'Title: My Sample\nFile: sample.zip\nDescription: |-\n  First line.\n\n  Second paragraph.\nIllustration: sample.png\nMinimum version: 14.0.1\n',
                encoding="utf-8",
            )
            sample = MODULE.load_sample(yaml_file)
            rendered = MODULE.render_snippet(sample, MODULE.slugify(sample["Title"]))
        self.assertIn("## Sample: My Sample {#sample-my-sample}", rendered)
        self.assertIn("all-samples.resources/sample.png", rendered)
        self.assertIn("all-samples.resources/sample.zip", rendered)
        self.assertIn("</p><p>Second paragraph.</p>", rendered)

    def test_update_page_inserts_before_marker(self):
        content = "before\n\n<!-- sample-item -->\n\n</table>\n"
        updated = MODULE.update_page(content, "{{sample-new-sample}}", "new-sample", False)
        self.assertLess(updated.index("{{sample-new-sample}}"), updated.index("<!-- sample-item -->"))

    def test_update_page_replaces_existing_reference(self):
        content = "{{sample-old}}\n{{sample-new-sample}}\n\n<!-- sample-item -->\n"
        updated = MODULE.update_page(content, "{{sample-new-sample}}", "new-sample", True)
        self.assertEqual(updated.count("{{sample-new-sample}}"), 1)


if __name__ == "__main__":
    unittest.main()
