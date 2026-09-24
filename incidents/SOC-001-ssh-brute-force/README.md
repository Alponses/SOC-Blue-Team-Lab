# SOC-001 — SSH brute force

**PLANNED — NOT RUN — REQUIRES MANUAL EXECUTION**

This is a scope stub, not an incident report. No alert, collected evidence, ATT&CK mapping, classification, severity, or closure decision is claimed.

- **Implementation phase:** 3.
- **Controlled scenario:** Repeated, bounded failed SSH authentications against SOC-LINUX from SOC-SIM.
- **Planned sources:** SSH/authentication records and Wazuh events.
- **Evidence needed:** Source IP, target account, unique attempt count, timestamps, subsequent successful login if any, and actual alert/rule references.

Before execution, verify telemetry, isolation, exact owned target scope, time synchronization, snapshots, stop conditions, and cleanup. Follow the [implementation checklist](../../docs/implementation-checklist.md).

When evidence exists, replace this stub with a completed [incident report](../../templates/incident-report.md), retaining every required section. Add small sanitized artifacts with provenance under this case's `evidence/` directory and follow the [evidence policy](../../docs/evidence-handling.md). Document missing expected alerts as **Detection Gap**. Do not fill unknown fields or results with invented data.

[Investigation index](../README.md)
