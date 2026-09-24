# Analyst playbooks

Status: **PLANNED — only the reusable template exists**.

Use the [SOC playbook template](../templates/soc-playbook.md). Complete operational checklists in Deliverable 8 using real investigation findings; validate phishing and AWS specifics in their later phases. No playbook is operationally validated yet.

| Planned playbook | Core decision |
| --- | --- |
| Brute force | Are failures bounded/expected, and was access subsequently gained? |
| Suspicious PowerShell | What process/script executed, by whom, with what effect and authorization? |
| Suspicious login | Is the source, authentication method, account, and timing consistent with authorized access? |
| Privilege / account changes | Who changed which identity or privilege, and was it approved? |
| Phishing | What do trusted headers and content establish, and was there user interaction? |
| Network scanning | Does the observed port/host pattern match an approved inventory or a suspicious probe? |
| Suspicious outbound connection | Which process contacted which destination, and what supports escalation? |
| AWS IAM activity | Which principal/session performed which API change against which resource? |

Each checklist must specify first checks, exact logs/fields, queries/pivots, enrichment handling, common false/benign positives, escalation criteria, and closure requirements. Link cases and commands only after they exist and have been reviewed.
