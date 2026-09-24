# SOC-003 — Suspicious PowerShell execution

**PLANNED — NOT RUN — REQUIRES MANUAL EXECUTION**

This is a scope stub, not an incident report. No alert, collected evidence, ATT&CK mapping, classification, severity, or closure decision is claimed.

- **Implementation phase:** 5.
- **Controlled scenario:** A safe PowerShell simulation that generates inspectable execution telemetry without malware.
- **Planned sources:** Sysmon Operational, PowerShell Operational, and Wazuh.
- **Evidence needed:** Process and parent, command line/script content, user, host, time, process correlation IDs, and network activity only if observed.

Before execution, verify telemetry, isolation, exact owned target scope, time synchronization, snapshots, stop conditions, and cleanup. Follow the [implementation checklist](../../docs/implementation-checklist.md).

When evidence exists, replace this stub with a completed [incident report](../../templates/incident-report.md), retaining every required section. Add small sanitized artifacts with provenance under this case's `evidence/` directory and follow the [evidence policy](../../docs/evidence-handling.md). Document missing expected alerts as **Detection Gap**. Do not fill unknown fields or results with invented data.

[Investigation index](../README.md)
