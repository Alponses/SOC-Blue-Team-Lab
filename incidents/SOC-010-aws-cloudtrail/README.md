# SOC-010 — AWS CloudTrail investigation

**PLANNED — NOT RUN — REQUIRES MANUAL EXECUTION**

This is a scope stub, not an incident report. No alert, collected evidence, ATT&CK mapping, classification, severity, or closure decision is claimed.

- **Implementation phase:** 10.
- **Controlled scenario:** Reconstruct controlled IAM/API/resource changes in the owner's AWS lab account.
- **Planned sources:** IAM state, CloudTrail events, and separately verified CloudWatch delivery.
- **Evidence needed:** Who, what, when, from where, resource, change, API outcome, permission context, and cleanup. Publish only sanitized samples; never keys or live account/resource identifiers.

Before execution, verify telemetry, isolation, exact owned target scope, time synchronization, snapshots, stop conditions, and cleanup. Follow the [implementation checklist](../../docs/implementation-checklist.md).

When evidence exists, replace this stub with a completed [incident report](../../templates/incident-report.md), retaining every required section. Add small sanitized artifacts with provenance under this case's `evidence/` directory and follow the [evidence policy](../../docs/evidence-handling.md). Document missing expected alerts as **Detection Gap**. Do not fill unknown fields or results with invented data.

[Investigation index](../README.md)
