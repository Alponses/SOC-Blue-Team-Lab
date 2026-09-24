# Implementation checklist

Complete one deliverable at a time. Deliverable 0 is the only authorized execution scope for the current task. All later work is **NOT STARTED — REQUIRES MANUAL EXECUTION** until environment access and execution are recorded. This checklist is a plan, not proof of installation or testing.

## Completion rules

- A deliverable is complete only when its acceptance evidence exists and has been reviewed.
- Report what was created, files changed, actual validation, evidence obtained, remaining issues, and the exact next deliverable.
- Record a **Detection Gap** when an expected detection is missing; preserve the failed test and investigate collection, parsing, rule logic, timing, and suppression.
- Snapshot before state changes, limit tests to explicit owned targets, and verify cleanup.
- Review staged content and make a logical local Git commit when the deliverable is ready.
- Do not proceed through an unresolved dependency merely to fill an incident report.

## Deliverable 0 — Repository skeleton and architecture

- [x] Inspect the working directory and parent guidance; establish existing Git status.
- [x] Create `SOC-Blue-Team-Lab` without overwriting unrelated files.
- [x] Create initial README, architecture document, and Mermaid network diagram.
- [x] Create public-repository ignore rules and evidence-handling guidance.
- [x] Create reusable incident and SOC playbook templates.
- [x] Reserve incident, configuration, detection, playbook, query, and screenshot locations.
- [x] Create this ordered implementation checklist.
- [x] Validate all internal Markdown links and inspect staged changes.
- [x] Record validation results and make the initial logical commit.

Acceptance: a navigable, locally committed scaffold with explicit unverified status. See the [execution report](deliverables/deliverable-0.md) for observed results. **Stop after this deliverable.**

## Deliverable 1 — Wazuh + Windows + Sysmon telemetry

Exact next scope: establish the isolated lab network and deploy only SOC-WAZUH and SOC-WIN11, with Wazuh agent, Sysmon, and existing Defender protection. Establish collection and benign event visibility; adversary-style investigations begin in later deliverables.

- [ ] Inventory usable host RAM/disk/CPU, supported hypervisor, guest requirements, evaluation media source, and available VM access. Confirm the proposed subnet is unused.
- [ ] Record versions, official download locations/checksums where supplied, VM sizing, guest identifiers, and recovery method. Do not commit installers or generated credentials.
- [ ] Create the host-only network and verify adapters, IPv4/IPv6 routes, host forwarding, management access, and absence of public exposure. Record temporary update NAT removal.
- [ ] Deploy Wazuh all-in-one at `10.10.10.10` and Windows 11 at `10.10.10.30`; confirm service health and take baseline snapshots.
- [ ] Enroll the Windows agent using privately stored enrollment material. Configure Security, System, PowerShell Operational, Sysmon Operational, and Defender Operational collection.
- [ ] Set Windows audit and PowerShell logging policies; configure Sysmon process creation, bounded network-connection, and DNS coverage. Record filters and why they were chosen.
- [ ] Verify time synchronization and document UTC conversion/skew, local event records, agent delivery, manager receipt, and SIEM search visibility.
- [ ] Generate harmless baseline events: an ordinary sign-in, a marker command/PowerShell script, and controlled local network/DNS activity where a local service/resolver is available. Capture a normal System/Defender event; do not disable protection or fabricate a malware alert.
- [ ] Prove at least one event from each required channel through the full collection path. Distinguish alerts from benign events available only through a deliberately enabled bounded archive path. Where a required Sysmon event cannot yet be stimulated, record the dependency and leave coverage unvalidated.
- [ ] Record exact queries, source/event IDs, timestamps, normalized fields, observed ingestion delay, dropped/absent fields, collection volume, and retention settings.
- [ ] Save small sanitized evidence, actual configuration exports without secrets, and a few evidence-captioned screenshots. Review public safety, rerun link checks, and commit the deliverable report.

Expected files: setup/validation documentation under `docs/`, sanitized templates/configuration under `configs/wazuh/` and `configs/windows/`, selected screenshots, and `docs/deliverables/deliverable-1.md`. Create links only once files exist.

Acceptance: both VMs are healthy and isolated, Windows is enrolled, every required channel is shown arriving via a documented path, and field-level limitations are explicit. A connected agent alone is insufficient. An inaccessible hypervisor/guest remains **REQUIRES MANUAL EXECUTION**, with no claim that deployment is complete.

Out of scope for Deliverable 1: Ubuntu, simulator, brute force, AD/domain join, Suricata, real incident verdicts, phishing, AWS, Splunk, and public GitHub publishing.

## Deliverable 2 — Ubuntu and authentication/SSH telemetry

- [ ] Deploy SOC-LINUX at `10.10.10.40`; install/configure OpenSSH, agent, and scoped audit/system logging.
- [ ] Identify actual journal/rsyslog sources, prevent duplicate ingestion, and verify SSH, auth, sudo, system, and selected application logs with benign operations.
- [ ] Capture required users/processes/source fields and document limits on network attribution.
- [ ] Reserve a dedicated non-sensitive test file/directory for later FIM; establish baseline and decide who-data/audit requirements without claiming actor attribution yet.

Acceptance: source-to-SIEM evidence and queries, accurate timestamps, logging paths, resource/retention notes, and sanitized configuration. No brute-force case yet.

## Deliverable 3 — SOC-001 SSH brute force

- [ ] Establish SOC-SIM at `10.10.10.50`, target allowlist, test account, rate/attempt bounds, lockout implications, snapshots, and cleanup plan.
- [ ] Generate a bounded series of owned-lab SSH failures; investigate failure counts, account, source, time window, and any later successful login.
- [ ] Identify actual Wazuh alerts/rule IDs or a Detection Gap. Complete evidence-linked report, timeline, ATT&CK rationale, severity, disposition, and escalation logic.

Acceptance: first complete investigation based on observed evidence; attempt counts reconciled with event/alert counts, and cleanup verified.

## Deliverable 4 — SOC-002 Windows authentication failures

- [ ] Generate controlled failures under a lockout-aware procedure; record authentication type and local/domain context.
- [ ] Identify relevant actual Security event IDs, status/substatus, account, source where present, and related SIEM events; build a timeline.
- [ ] Complete the standard incident report with observed outcome and cleanup.

Acceptance: Windows authentication evidence supports the verdict and escalation criteria; missing source fields are not invented.

## Deliverable 5 — SOC-003 PowerShell / Sysmon

- [ ] Run a reviewed harmless PowerShell simulation with explicit marker, target, bounds, and cleanup.
- [ ] Correlate process/parent, command line, user, host, timestamp, script-block information, and network activity only if generated/observed.
- [ ] Record detection success/gap and finish the report and ATT&CK mapping based on the observed behavior.

Acceptance: cross-source process evidence, correct interpretation of authorized simulation, and documented detection improvements.

## Deliverable 6 — Suricata and network investigations

- [ ] Install/configure Suricata on SOC-LINUX and collect selected EVE output into Wazuh; demonstrate capture-path visibility first.
- [ ] Complete SOC-005 with a bounded scan of SOC-LINUX only, showing port/time pattern, actual IDS/flow evidence, and packet inspection if useful.
- [ ] Complete SOC-006 with a harmless workstation connection to a lab-local service, correlating process and network tuple; stop the service afterward.
- [ ] Start SOC-007 with a local controlled resolver and reserved domain; otherwise defer its execution to phase 7 and record the dependency.
- [ ] Document DNS response evidence, endpoint attribution, reputation methodology, encryption/visibility limits, false positives, and gaps.

Acceptance: actual network evidence and completed 005/006 reports; 007 is complete only with observed query/response evidence. No claim of whole-switch visibility without proof.

## Deliverable 7 — Active Directory and identity investigations

- [ ] Deploy SOC-DC01 at `10.10.10.20`, AD DS and local DNS for `soc.test`; configure explicit service flows and appropriate audit policies.
- [ ] Create invented normal users, a separate administrator identity, and security groups; join Windows 11 to the domain.
- [ ] Validate DC/workstation authentication sources and time synchronization; finish SOC-007 if it required AD DNS.
- [ ] Complete SOC-004: create a test account, change group membership/elevation, identify actor/target/privilege/host/time, check authorization, then restore state.

Acceptance: evidence-backed identity report and domain/DNS collection proof, including actual successful/failed authentication and authorized administrator activity.

## Deliverable 8 — Detections, FIM investigation, and playbooks

- [ ] Build/tune only detections justified by preceding investigations in Wazuh, Sigma where portable, and Suricata where relevant.
- [ ] Document objective, source, logic, ATT&CK, expected true positives, false positives, validation steps, observed results, and known gaps for each rule.
- [ ] Validate positive and negative controls and threshold boundaries where applicable; record engine/backend versions and parsing/field requirements.
- [ ] Complete SOC-008 with a controlled test-file change, previous/current state, FIM evidence, supported actor attribution, and restoration verification.
- [ ] Write the eight scoped operational playbooks listed in the playbook index; link actual queries and cases. Revalidate phishing/AWS playbooks after those investigations run.

Acceptance: tested meaningful detection content, an evidence-backed FIM case, and usable analyst checklists. A Sigma file without target-backend testing is marked unvalidated for that backend.

## Deliverable 9 — SOC-009 phishing

- [ ] Create a clearly labeled synthetic email or choose a safe training sample with documented provenance.
- [ ] Analyze header trust boundaries, From/Reply-To/Return-Path/Received, SPF/DKIM/DMARC, defanged URLs/domains, hashes, and attachment metadata.
- [ ] Document enrichment results actually obtained or why enrichment was not performed; do not upload confidential information.
- [ ] Complete executive summary, evidence, IOC table, timeline, verdict, actions, and the standard report sections; validate the phishing playbook.

Acceptance: reproducible analysis that distinguishes synthetic assertions from authenticated delivery evidence.

## Deliverable 10 — SOC-010 AWS CloudTrail

- [ ] Establish owner's AWS lab account scope, secure access, resource/region boundaries, costs/retention, and cleanup procedure before controlled changes.
- [ ] Configure/verify IAM, CloudTrail coverage, and CloudWatch log delivery. Generate bounded identity/API/resource changes, including API access-key identity context where appropriate; keep all key material private.
- [ ] Reconstruct who/what/when/from where/resource/change and API outcome, then verify resource and permission cleanup.
- [ ] Publish only sanitized samples, documented limitations, standard incident report, and validated AWS playbook.

Acceptance: actual source events support the reconstruction; no credentials, public infrastructure targets, or live identity details in Git.

## Deliverable 11 — Splunk / SPL investigations

- [ ] Introduce Splunk Enterprise only after Wazuh investigations work; record version, resources, source types, field mappings, timestamp extraction, and import counts.
- [ ] Import sanitized lab datasets; reconcile event counts and document preprocessing.
- [ ] Implement and validate the seven SPL investigations in the query index with objective, query, fields, time bounds, expected behavior, actual output, and caveats.
- [ ] Distinguish SPL/Enterprise practice from Enterprise Security, which remains unclaimed unless actually used.

Acceptance: reproducible searches of real sanitized datasets with observed results and known limitations.

## Deliverable 12 — Final portfolio review

- [ ] Update README status, architecture, environment versions, investigation results/links, and concrete skills demonstrated.
- [ ] Keep only a few captioned screenshots that prove findings; preserve primary evidence and analyst reasoning.
- [ ] Verify every report uses the standard sections and every classification/severity/decision follows from evidence.
- [ ] Review internal links, repository size, all tracked artifacts/history, secrets, privacy, licensing, Git authors, and any remaining detection gaps.
- [ ] Check that a reviewer can understand actual scope and evidence within 2–3 minutes; remove unsupported experience claims.

Acceptance: public-ready reviewed repository. Remote creation or publishing is a separate action, not part of Deliverable 0.
