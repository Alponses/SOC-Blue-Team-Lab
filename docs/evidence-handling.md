# Evidence handling and public publication

Status: repository policy defined; no operational evidence collected yet.

## Provenance and storage

Keep source logs, email originals, full packet captures, credentials, export bundles, and the real-to-sanitized identity map outside this repository in private storage. `private/`, `raw/`, `exports/`, and common sensitive formats are ignored as a second layer, not a secure vault. `.gitignore` does not protect files already tracked or files added with force.

Publish only the minimum reviewed excerpt needed to support a finding. Store future small sanitized excerpts beside the incident report in an `evidence/` subdirectory; add an evidence manifest with source type, collection time, original time zone, export/query method, source version, redactions, record locators, and SHA-256 of the published artifact. No evidence subdirectories contain samples at this stage.

Use consistent invented aliases and addresses throughout a case so correlation remains possible. Explain any timestamp shift and apply it consistently; preserve relative ordering and intervals. Keep important distinctions such as actor versus target and source versus destination. Do not replace failed outcomes with successful ones or fill missing fields from assumptions.

Label provenance as one of: observed lab simulation, sanitized export of observed lab evidence, or synthetic training sample. Synthetic email or fixtures are legitimate teaching inputs only when clearly labeled; they cannot prove a deployed detector worked. Planned steps and expected results are not observations.

## Sanitization review

Review nested JSON, command lines, script blocks, URLs/query parameters, email headers, screenshots, and metadata for secrets and identifying material. Remove credentials, passwords, API tokens, access keys, session tokens, cookies, private keys, live account IDs/ARNs, personal emails/usernames, public infrastructure addresses, and unrelated file paths. Keep mappings and unredacted originals private.

For synthetic names use invented lab identities and reserved domains such as `soc.test` or `example.invalid`. Defang phishing URLs in reports. Do not visit a suspicious URL merely to enrich it. Record external reputation results only if actually obtained, with lookup time and disclosure scope; a reserved domain has no meaningful live reputation verdict.

Do not upload confidential material to VirusTotal, URLScan, or similar services. A public lookup may disclose the indicator or artifact. Prefer local analysis and synthetic training samples; document checks that were deliberately not performed.

Keep raw logs, VM/ISO images, binaries, and packet captures out of Git. Small reviewed JSON/CSV/TXT excerpts are preferred. Review artifact size before staging; a project guideline of at most 1 MiB per text excerpt and 2 MiB per screenshot encourages selected evidence, not bulk export. These size limits are review guidance and are not enforced by `.gitignore`.

## Publication checklist

- [ ] Every claim is tied to observed evidence or explicitly labeled planned/synthetic/unverified.
- [ ] No credentials, keys, cookies, personal identifiers, public infrastructure targets, malicious binaries, VM images, or sensitive captures are present.
- [ ] Excerpts are small, relevant, consistently sanitized, and have provenance and record locators.
- [ ] Screenshots have evidence captions; inspect visible UI, tabs, metadata, and hidden personal information.
- [ ] Run `python3 scripts/validate_repository.py` and `git diff --check`.
- [ ] Review `git status --short`, `git diff --cached --stat`, and `git diff --cached` before committing.
- [ ] Review all history and Git author metadata before creating a public remote; deleting a secret in a later commit does not remove it from earlier history.
- [ ] Add a dedicated secret scanner before publishing real evidence; link validation and `.gitignore` are not secret scans.

No GitHub repository has been created or published in Deliverable 0. The local initial commit uses a generic project author and a reserved email address to avoid adding personal identity to this scaffold.
