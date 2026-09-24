# SOC-005 — Network scanning

**PLANNED — NOT RUN — REQUIRES MANUAL EXECUTION**

This is a scope stub, not an incident report. No alert, collected evidence, ATT&CK mapping, classification, severity, or closure decision is claimed.

- **Implementation phase:** 6.
- **Controlled scenario:** A bounded scan from SOC-SIM targeting only SOC-LINUX and documented ports.
- **Planned sources:** Suricata EVE, Wazuh, and private packet inspection where useful.
- **Evidence needed:** Sensor interface/path proof, source/destination, protocol/ports, port fan-out and timing, rule IDs if alerts occur, and alternative explanations.

Before execution, verify telemetry, isolation, exact owned target scope, time synchronization, snapshots, stop conditions, and cleanup. Follow the [implementation checklist](../../docs/implementation-checklist.md).

When evidence exists, replace this stub with a completed [incident report](../../templates/incident-report.md), retaining every required section. Add small sanitized artifacts with provenance under this case's `evidence/` directory and follow the [evidence policy](../../docs/evidence-handling.md). Document missing expected alerts as **Detection Gap**. Do not fill unknown fields or results with invented data.

[Investigation index](../README.md)
