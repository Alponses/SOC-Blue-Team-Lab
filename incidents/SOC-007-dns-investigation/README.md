# SOC-007 — DNS investigation

**PLANNED — NOT RUN — REQUIRES MANUAL EXECUTION**

This is a scope stub, not an incident report. No alert, collected evidence, ATT&CK mapping, classification, severity, or closure decision is claimed.

- **Implementation phase:** 6, or 7 if waiting for AD DNS.
- **Controlled scenario:** Query reserved test names using a controlled local resolver; never use live malicious domains.
- **Planned sources:** Sysmon DNS, controlled DNS server logs or captures on the DNS path, and Wazuh.
- **Evidence needed:** Requested name, requester, process when available, actual response/rcode, timeline, enrichment methodology and unperformed checks. Ubuntu Suricata does not automatically see workstation-to-DC traffic.

Before execution, verify telemetry, isolation, exact owned target scope, time synchronization, snapshots, stop conditions, and cleanup. Follow the [implementation checklist](../../docs/implementation-checklist.md).

When evidence exists, replace this stub with a completed [incident report](../../templates/incident-report.md), retaining every required section. Add small sanitized artifacts with provenance under this case's `evidence/` directory and follow the [evidence policy](../../docs/evidence-handling.md). Document missing expected alerts as **Detection Gap**. Do not fill unknown fields or results with invented data.

[Investigation index](../README.md)
