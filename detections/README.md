# Detection engineering

Status: **PLANNED — no custom detections implemented or validated**.

Use observed investigation findings to decide what to build. Initial detections may be added while investigating; phase 8 consolidates coverage and validation. A source event arriving is not the same as a detection firing.

| Directory | Intended artifact |
| --- | --- |
| [Wazuh](wazuh/README.md) | Custom rules and decoders only where needed, with sanitized inputs and observed output |
| [Sigma](sigma/README.md) | Portable behavior logic with source/field/backend assumptions |
| [Suricata](suricata/README.md) | Lab-relevant IDS rules validated on the actual capture path |

Every detection needs an adjacent description covering objective, log source, required fields, logic/threshold/window/grouping, ATT&CK rationale, expected true positives, possible false positives, and validation procedure. Include engine/rule versions, exact scoped input, expected versus observed results, a benign negative control, threshold boundary tests where relevant, limitations, and an incident link. Label failed validation **Detection Gap**. Do not invent rule IDs or success evidence in advance.
