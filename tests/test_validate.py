"""Exercise structural faults using minimal, isolated plugin packages."""

import json
from pathlib import Path
import tempfile
import unittest

from scripts.validate import validate


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for host in ("codex", "claude"):
            self.write(
                f".{host}-plugin/plugin.json",
                json.dumps({"name": "sample", "version": "0.1.0", "description": "A sample plugin", "skills": "./skills/"}),
            )
        self.write("skills/sample/SKILL.md", "---\nname: sample\ndescription: >-\n  A sample skill with\n  folded metadata.\n---\n\n[Guide](references/guide.md#start)\n")
        self.write("skills/sample/references/guide.md", "# Start\n[Return](../SKILL.md)\n")
        self.write("skills/sample/agents/openai.yaml", "interface:\n  display_name: Sample\n")

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_valid_package_and_nonfile_links(self):
        self.write("skills/sample/references/guide.md", """# Guide
[Web](https://example.com/docs)
[Mail](mailto:hello@example.com)
[Anchor](#heading)
[Encoded filename](space%20name.md)
[Reference][detail]
[detail]: <space name.md>
Inline syntax example: `[Example](nonexistent-course/chapter.md)`.
```markdown
[Example output](nonexistent-course/chapter.md)
```
""")
        self.write("skills/sample/references/space name.md", "# Supporting material\n")
        self.write("skills/sample/assets/template.md", "[Next]({{NEXT_LESSON}})\n")
        self.assertEqual([], validate(self.root))

    def test_missing_markdown_link_and_explicit_supporting_path(self):
        for reference in ("[Missing](absent.md)", "`references/absent.md`", "[missing]: absent.md"):
            with self.subTest(reference=reference):
                self.write("skills/sample/references/guide.md", reference + "\n")
                errors = validate(self.root)
                self.assertTrue(any("missing referenced file" in error and "absent.md" in error for error in errors), errors)

    def test_links_cannot_escape_skill_directory(self):
        self.write("outside.md", "# Exists, but is outside the skill\n")
        for target in ("../../../outside.md", str(self.root / "outside.md"), "..%2F..%2F..%2Foutside.md"):
            with self.subTest(target=target):
                self.write("skills/sample/references/guide.md", f"[Escape]({target})\n")
                self.assertTrue(any("path escapes" in error for error in validate(self.root)))

    def test_symlink_escape_is_rejected(self):
        outside = self.write("outside.md", "# Outside\n")
        (self.root / "skills/sample/references/linked.md").symlink_to(outside)
        self.write("skills/sample/references/guide.md", "[Escape](linked.md)\n")
        self.assertTrue(any("path escapes" in error for error in validate(self.root)))
        self.write("skills/sample/references/guide.md", "# No links\n")
        self.assertTrue(any("path escapes" in error for error in validate(self.root)))

    def test_manifest_identity_and_version_must_agree(self):
        for field, changed in (("name", "different"), ("version", "0.2.0")):
            with self.subTest(field=field):
                path = self.root / ".claude-plugin/plugin.json"
                metadata = {"name": "sample", "version": "0.1.0", "description": "Example"}
                metadata[field] = changed
                self.write(str(path.relative_to(self.root)), json.dumps(metadata))
                self.assertIn(f"Plugin manifests must agree on {field!r}", validate(self.root))

    def test_invalid_manifest_metadata_is_reported(self):
        for content in ("[", "null", "[]", '{"name": 123, "version": []}', '{"skills": [false]}'):
            with self.subTest(content=content):
                self.write(".codex-plugin/plugin.json", content)
                errors = validate(self.root)
                self.assertTrue(errors)
                self.assertTrue(any(".codex-plugin/plugin.json" in error for error in errors))

    def test_invalid_frontmatter_is_reported(self):
        for content in ("No metadata", "---\n[invalid\n---\n", "---\n- list\n---\n", "---\nname: 12\ndescription: []\n---\n"):
            with self.subTest(content=content):
                self.write("skills/sample/SKILL.md", content)
                errors = validate(self.root)
                self.assertTrue(any("SKILL.md" in error for error in errors), errors)

    def test_manifest_skill_path_must_exist_and_stay_in_package(self):
        for target in ("./absent/", "../", str(self.root / "skills")):
            with self.subTest(target=target):
                self.write(".codex-plugin/plugin.json", json.dumps({"name": "sample", "version": "0.1.0", "description": "Example", "skills": target}))
                errors = validate(self.root)
                self.assertTrue(any(".codex-plugin/plugin.json" in error for error in errors), errors)

    def test_empty_skill_directory_and_missing_agent_metadata(self):
        (self.root / "skills/sample/agents/openai.yaml").unlink()
        self.assertTrue(any("agents/openai.yaml" in error for error in validate(self.root)))
        (self.root / "skills/sample/SKILL.md").unlink()
        self.assertTrue(any("no SKILL.md" in error for error in validate(self.root)))


if __name__ == "__main__":
    unittest.main()
