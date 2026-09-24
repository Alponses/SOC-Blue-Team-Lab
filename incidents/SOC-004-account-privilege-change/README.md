# SOC-004 — Account / privilege change

**PLANNED — NOT RUN — REQUIRES MANUAL EXECUTION**

This is a scope stub, not an incident report. No alert, collected evidence, ATT&CK mapping, classification, severity, or closure decision is claimed.

- **Implementation phase:** 7.
- **Controlled scenario:** Create a test identity and change group membership/elevated privilege in the lab, then restore state.
- **Planned sources:** Windows/DC Security events, identity state, and Wazuh.
- **Evidence needed:** Actor, affected identity, previous/new group or privilege, host, time, authorization context, and cleanup verification.

Before execution, verify telemetry, isolation, exact owned target scope, time synchronization, snapshots, stop conditions, and cleanup. Follow the [implementation checklist](../../docs/implementation-checklist.md).

When evidence exists, replace this stub with a completed [incident report](../../templates/incident-report.md), retaining every required section. Add small sanitized artifacts with provenance under this case's `evidence/` directory and follow the [evidence policy](../../docs/evidence-handling.md). Document missing expected alerts as **Detection Gap**. Do not fill unknown fields or results with invented data.

[Investigation index](../README.md)
