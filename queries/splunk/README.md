# Splunk Enterprise and SPL investigations

Status: **DEFERRED — no Splunk deployment, dataset import, or queries tested**. Begin in Deliverable 11 after the Wazuh investigations work. Wazuh remains the primary SIEM. Splunk Enterprise Security has not been used and is not claimed.

| Planned search | Investigation purpose |
| --- | --- |
| Failed authentication | Count failures by account/source/host in an explicit time window, accounting for duplicate records |
| Successful login after multiple failures | Reconstruct ordered failures then success for the same relevant account/source; an unordered aggregate is insufficient |
| Suspicious PowerShell | Inspect command-line and script-block behavior with process/parent/user context |
| Account creation | Identify actor, created identity, host, and related subsequent actions |
| Privilege changes | Identify group/privilege before and after, actor/target, and authorization context |
| Network scanning | Evaluate distinct destination ports/hosts and event timing, excluding explained inventory activity |
| DNS analysis | Correlate queries, responses, requesting endpoint/process where available, and lookup outcomes |

Each eventual query must state objective, source type, field mapping, dataset provenance, event-time parsing/timezone, exact time bounds, SPL, why the search is useful, expected behavior, observed results, and limitations. Do not assume CIM fields or Enterprise Security data models exist. Use only reviewed sanitized lab datasets, and preserve enough fields to make correlation reproducible.
