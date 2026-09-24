# Repository validation

Run from the repository root with Python 3.9+ and Git:

```sh
python3 scripts/validate_repository.py
git diff --check
```

The validator checks tracked and non-ignored untracked Markdown files for the inline-link syntax used by this repository. It checks file/directory targets, repository boundaries, and same-file/cross-file GitHub-style heading anchors, including duplicate headings. Fenced examples are excluded. It exits nonzero for broken links or a missing Git context.

Keep authored links inline. Reference-style links, HTML links/anchors, and unusual Markdown constructs need a parser upgrade if introduced. This is not a general Markdown renderer, external URL checker, Mermaid renderer, secret scanner, or lab test. It cannot establish infrastructure health or detection success.

No provisioning or simulation scripts exist in Deliverable 0. All operational work remains **REQUIRES MANUAL EXECUTION** until later phases.
