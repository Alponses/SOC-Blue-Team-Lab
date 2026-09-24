# SOC-009 — Phishing investigation

**PLANNED — NOT RUN — REQUIRES MANUAL EXECUTION**

This is a scope stub, not an incident report. No alert, collected evidence, ATT&CK mapping, classification, severity, or closure decision is claimed.

- **Implementation phase:** 9.
- **Controlled scenario:** Analyze a clearly labeled synthetic email or safe training sample without visiting malicious infrastructure.
- **Planned sources:** Email headers/content, attachment metadata, local analysis, and permitted enrichment.
- **Evidence needed:** Executive summary, From/Reply-To/Return-Path/Received, SPF/DKIM/DMARC trust limits, defanged URLs/domains, hashes, metadata, IOC table, timeline, verdict, and actions. Record reputation checks as not performed unless actually obtained.

Before execution, verify telemetry, isolation, exact owned target scope, time synchronization, snapshots, stop conditions, and cleanup. Follow the [implementation checklist](../../docs/implementation-checklist.md).

When evidence exists, replace this stub with a completed [incident report](../../templates/incident-report.md), retaining every required section. Add small sanitized artifacts with provenance under this case's `evidence/` directory and follow the [evidence policy](../../docs/evidence-handling.md). Document missing expected alerts as **Detection Gap**. Do not fill unknown fields or results with invented data.

[Investigation index](../README.md)
