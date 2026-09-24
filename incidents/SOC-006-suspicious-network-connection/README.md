# SOC-006 — Suspicious network connection

**PLANNED — NOT RUN — REQUIRES MANUAL EXECUTION**

This is a scope stub, not an incident report. No alert, collected evidence, ATT&CK mapping, classification, severity, or closure decision is claimed.

- **Implementation phase:** 6.
- **Controlled scenario:** A harmless request from Windows to a temporary lab-local service on SOC-LINUX.
- **Planned sources:** Sysmon network/process events, Suricata EVE, Wazuh, and local service logs.
- **Evidence needed:** Process/parent/user, endpoint, destination, port/protocol, timestamps, cross-source correlation, and service cleanup.

Before execution, verify telemetry, isolation, exact owned target scope, time synchronization, snapshots, stop conditions, and cleanup. Follow the [implementation checklist](../../docs/implementation-checklist.md).

When evidence exists, replace this stub with a completed [incident report](../../templates/incident-report.md), retaining every required section. Add small sanitized artifacts with provenance under this case's `evidence/` directory and follow the [evidence policy](../../docs/evidence-handling.md). Document missing expected alerts as **Detection Gap**. Do not fill unknown fields or results with invented data.

[Investigation index](../README.md)
