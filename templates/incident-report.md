# Incident ID

Replace this heading with `SOC-NNN — Scenario title` when creating a report.

| Record | Value |
| --- | --- |
| Status | NOT STARTED / REQUIRES MANUAL EXECUTION / IN PROGRESS / VALIDATED |
| Analyst | Lab alias only |
| Evidence provenance | Observed lab simulation / sanitized observed export / synthetic training sample |
| Execution window | Start and end in UTC; retain original zone and clock offset |
| Environment / versions | Guest, agent, rules/configuration revision, relevant tools |
| Authorization | Owned targets, test purpose, authorized actor, approved window |
| Simulation record | Exact bounded steps, snapshot reference, expected signal, stop conditions, cleanup and observed cleanup result |

This is an unfilled template, not an executed incident. Remove instructions and unused placeholders only after recording real observations. Label synthetic samples explicitly; do not present them as collected events.

## Executive Summary

Briefly describe the observed behavior, affected assets, evidence-backed impact, verdict, and action. For phishing, include the delivery/pretext and whether user interaction or execution is known. Separate facts, hypotheses, and unknowns.

## Alert

Record alert time, rule ID/name/version, level, source, triggering fields, and the actual alert reference. Describe why it was investigated. If there was no alert, write **Detection Gap**, document the attempted validation, and identify the manual hunt/source event that began the case. Do not invent an alert ID.

## Initial Triage

Check asset criticality, alert duplication, collection health, timestamps/skew, authorized activity, and immediate impact. Record the initial hypothesis and what would disprove it.

## Scope

Identify in-scope hosts, users, source/destination addresses, services, time range, related activity, and collection blind spots. Explain how scope expanded or remained bounded.

## Evidence

Use stable evidence IDs and actual relative links to reviewed excerpts. Keep originals private; public artifacts must follow the repository's evidence policy. Remove the blank row below when filling the table.

| Evidence ID | Source / event ID | Artifact and record locator | What it proves | Limitations / redactions |
| --- | --- | --- | --- | --- |
| To fill | To fill | To fill | To fill | To fill |

Record query text, search window, timezone, count method, and deduplication method. Distinguish event count from alert count and unique attempts; preserve event IDs needed to cross-reference sources. Hash published artifacts only after sanitization and identify the hash algorithm. An export hash verifies that export, not the private original.

## Timeline

| Timestamp (UTC) | Host / actor | Observed event | Evidence ID | Analyst interpretation / uncertainty |
| --- | --- | --- | --- | --- |
| To fill | To fill | To fill | To fill | To fill |

Order by event time; retain ingestion time if useful. Explain gaps, clock drift, snapshot effects, or conflicting sources.

## Indicators

| Type | Sanitized value | Context / role | Enrichment source and lookup time | Result / confidence |
| --- | --- | --- | --- | --- |
| To fill | To fill | To fill | To fill | To fill |

An internal IP, account, or process is an investigative indicator, not automatically a malicious IOC. Label invented and reserved domains. For phishing, inspect From, Reply-To, Return-Path, Received chains, trustworthy authentication results (SPF/DKIM/DMARC), defanged URLs/domains, attachment metadata, and hashes. Distinguish synthetically supplied authentication results from verified results; do not trust sender-inserted headers. Record reputation checks as not performed when appropriate; absence of reputation data does not mean benign. Never submit confidential content to enrichment services.

## MITRE ATT&CK

Record tactic, technique/sub-technique ID, official technique reference, and the specific behavior/evidence supporting each mapping. ATT&CK describes behavior, not a verdict. Use “not applicable” with reasoning for generic changes that do not establish adversary behavior. Do not infer credential theft, persistence, or command-and-control from a single ambiguous event.

## Analysis

Correlate the evidence and explain the causal sequence, competing explanations, and missing information. Include relevant source fields rather than screenshots alone. For authentication cases distinguish failures, lockout, and later success. For AWS answer **Who → What → When → From Where → Against Which Resource → What Changed**, including outcome/errors and previous/new state where available.

## Classification

Choose exactly one after analysis: **True Positive**, **False Positive**, **Benign Positive**, or **Inconclusive**. Leave unassigned while this is a template.

- True Positive: evidence supports the malicious/unauthorized behavior the detection is intended to identify. A simulation verdict must explicitly say it is simulated and describe its test ground truth.
- False Positive: the detection asserted a condition that the evidence does not support; explain the mismatch.
- Benign Positive: the behavior was correctly detected and was authorized/expected in context.
- Inconclusive: evidence is insufficient or conflicting; specify what is needed.

Record detection validation separately as **not tested / fired as expected / Detection Gap**. A rule can fire correctly for an approved simulation while the analyst disposition is Benign Positive. Explain the verdict with evidence and authorization context.

## Severity

Assign a justified severity using observed impact, target privilege/criticality, scope, successful versus failed actions, and uncertainty. Record the original SIEM level separately. Explain any increase or decrease; a large failure count alone does not prove compromise.

## Decision

Choose **Close** or **Escalate** when sufficiently supported. State why, the owner/recipient role, urgency, evidence handoff, and specific unanswered questions. An incomplete template has no decision. Document any containment request separately from an action actually performed.

## Recommended Actions

Separate immediate containment, further investigation, remediation, and prevention. State owner and execution status; L1 recommendations do not imply authority to disable accounts or isolate machines. For an authorized lab simulation, document removal of test artifacts, restoration of modified state, and verification of cleanup.

## Lessons Learned / Detection Improvement

Describe collection gaps, incorrect assumptions, tuning proposals, and expected false positives. Link the eventual detection and playbook changes. Record actual positive/negative control outcomes and residual gaps; do not say a change fixed detection before testing it.
