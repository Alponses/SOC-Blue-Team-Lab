# Investigaciones del laboratorio

El objetivo de estos casos es practicar el recorrido desde una alerta hasta una decisión documentada, utilizando registros de equipos, identidades, red y nube.

**Avance: 10 escenarios definidos; 0 ejecutados; 0 informes completados.** Cada ficha recoge el objetivo, las evidencias necesarias y sus dependencias. Las técnicas ATT&CK y la clasificación se incorporarán durante el análisis de los eventos observados.

| Caso | Etapa prevista |
| --- | --- |
| [SOC-001 — Fuerza bruta SSH](SOC-001-ssh-brute-force/README.md) | 3 |
| [SOC-002 — Fallos de autenticación en Windows](SOC-002-windows-authentication/README.md) | 4 |
| [SOC-003 — Ejecución sospechosa de PowerShell](SOC-003-suspicious-powershell/README.md) | 5 |
| [SOC-004 — Cambios de cuentas y privilegios](SOC-004-account-privilege-change/README.md) | 7 |
| [SOC-005 — Escaneo de red](SOC-005-network-scanning/README.md) | 6 |
| [SOC-006 — Conexión de red sospechosa](SOC-006-suspicious-network-connection/README.md) | 6 |
| [SOC-007 — Investigación DNS](SOC-007-dns-investigation/README.md) | 6; 7 si depende de AD DNS |
| [SOC-008 — Integridad de archivos](SOC-008-file-integrity/README.md) | 8 |
| [SOC-009 — Investigación de phishing](SOC-009-phishing/README.md) | 9 |
| [SOC-010 — Investigación de AWS CloudTrail](SOC-010-aws-cloudtrail/README.md) | 10 |

Los informes seguirán la [plantilla de incidente](../templates/incident-report.md): resumen, alerta, evaluación inicial, alcance, evidencias, línea de tiempo, indicadores, ATT&CK, análisis, clasificación, severidad, decisión, acciones y lecciones aprendidas.

La primera investigación será SOC-001, después de validar la recopilación SSH en Linux. Los originales se conservarán de forma privada y solo se publicarán fragmentos revisados. Consulta el [manejo de evidencias](../docs/evidence-handling.md) y el [plan de implementación](../docs/implementation-checklist.md).
