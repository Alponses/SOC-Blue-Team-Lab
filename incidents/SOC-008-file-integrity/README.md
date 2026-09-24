# SOC-008 — File integrity / unexpected change

**PLANNED — NOT RUN — REQUIRES MANUAL EXECUTION**

This is a scope stub, not an incident report. No alert, collected evidence, ATT&CK mapping, classification, severity, or closure decision is claimed.

- **Implementation phase:** 8.
- **Controlled scenario:** Modify and restore a dedicated non-sensitive monitored test file or directory.
- **Planned sources:** Wazuh FIM, baseline file state, and audit/who-data where supported.
- **Evidence needed:** Path, endpoint, time, before/after state or hashes, actor only if evidenced, authorization, and restoration verification.

Before execution, verify telemetry, isolation, exact owned target scope, time synchronization, snapshots, stop conditions, and cleanup. Follow the [implementation checklist](../../docs/implementation-checklist.md).

When evidence exists, replace this stub with a completed [incident report](../../templates/incident-report.md), retaining every required section. Add small sanitized artifacts with provenance under this case's `evidence/` directory and follow the [evidence policy](../../docs/evidence-handling.md). Document missing expected alerts as **Detection Gap**. Do not fill unknown fields or results with invented data.

[Investigation index](../README.md)
