# SOC playbook — scenario

Status: **DRAFT — NOT OPERATIONALLY VALIDATED**. This template is a checklist structure, not a completed playbook.

| Field | Value |
| --- | --- |
| Purpose / trigger | Specific alert or observation and intended analyst outcome |
| Scope / owner | Allowed assets and responsible role |
| Required access | Read permissions, indexes, tools, and any limitations |
| Log prerequisites | Sources, collection-health checks, field availability, time window |
| Related artifacts | Add working relative links to reports, queries, and detections |
| Validation | Tool/config versions, test date, actual outcomes, reviewer alias |

## First Checks

- [ ] Preserve the original alert, rule/version, event time, and source evidence reference.
- [ ] Confirm affected host, user, privilege, criticality, and current observed impact.
- [ ] Verify log freshness, time zones/skew, duplicates, and missing sources.
- [ ] Check approved changes, lab simulation records, and previous related cases.
- [ ] Apply the immediate escalation triggers defined below; do not delay urgent escalation for optional enrichment.

## Logs and Fields

| Question to answer | Exact source/channel/index | Required fields | Query or pivot | Expected limitations |
| --- | --- | --- | --- | --- |
| To fill | To fill | To fill | To fill | To fill |

## Investigation Checklist

- [ ] Define the initial time window and expand it with a stated reason.
- [ ] Correlate source and destination, actor and target, process and parent, and success/failure as relevant.
- [ ] Check related hosts/users and prior or subsequent successful activity.
- [ ] Deduplicate events and distinguish events from aggregated alerts.
- [ ] Build a UTC timeline with evidence IDs; preserve uncertainty.
- [ ] Compare the leading explanation with an alternative supported by evidence.

## Enrichment

- [ ] Identify whether indicators are internal, synthetic, reserved, or externally routable.
- [ ] Use local context first: asset inventory, user role, change window, known service, hash/signature.
- [ ] If external enrichment is appropriate, record service, lookup time, result, and confidence.
- [ ] Do not upload confidential files, full private URLs, headers, tokens, or sensitive hashes without an appropriate basis for disclosure. Use synthetic content or document an unperformed lookup.

## Common False Positives and Benign Positives

| Alternative explanation | Evidence needed to confirm | When it is unsafe to dismiss |
| --- | --- | --- |
| To fill | To fill | To fill |

Do not use a blanket user/IP allowlist as a substitute for checking context.

## Escalation Criteria

Define scenario-specific thresholds and evidence. Include successful activity after suspicious failures, unexpected privileged changes, verified impact, scope expansion, and unresolved evidence gaps where applicable.

| Condition | Priority / receiving role | Minimum evidence and unanswered questions | L1 action permitted |
| --- | --- | --- | --- |
| To fill | To fill | To fill | To fill |

Containment actions require the appropriate operational authority; this checklist alone does not grant it. In the lab, only named lab assets may be changed under the simulation procedure.

## Classification and Closure

- [ ] Select True Positive, False Positive, Benign Positive, or Inconclusive with evidence.
- [ ] Separate detection test outcome from incident classification.
- [ ] Justify severity, Close/Escalate decision, and recommended follow-up.
- [ ] Record case owner, handoff contents, and next review requirement if unresolved.
- [ ] Confirm required cleanup, remediation verification, and no unexplained remaining activity.
- [ ] Attach reviewed evidence and timeline using the incident-report structure.

## Validation and Improvement

- [ ] Run the scoped positive control, benign/negative control, and boundary condition where relevant.
- [ ] Record actual results and limitations; missing expected alerts are a **Detection Gap**.
- [ ] Update queries, collection requirements, and escalation logic from what the test showed.
