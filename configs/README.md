# Configuration locations

Status: **RESERVED — no deployment configurations have been created or applied**.

| Directory | Future content | Phase |
| --- | --- | --- |
| [wazuh](wazuh/) | Reviewed central/agent collection configuration, retention and validation notes | 1 onward |
| [windows](windows/) | Audit/PowerShell logging, Sysmon filters, agent event channels | 1 |
| [linux](linux/) | Auth/journal collection, audit, SSH, dedicated FIM test path | 2 |
| [suricata](suricata/) | Capture interface assumptions and selected EVE output | 6 |
| [active-directory](active-directory/) | Lab identity/DNS/audit configuration and change procedures | 7 |
| [aws](aws/) | Sanitized lab logging/IAM configuration with no credentials or live resource identifiers | 10 |

Record exact versions and validation when adding files. Use obvious placeholders for per-installation secrets and inject their real values privately. Never commit enrollment keys, generated passwords, cloud access keys, or private certificates. A configuration file in Git is not proof it was applied.
