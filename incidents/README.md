# Investigaciones SOC — laboratorio y honeypot

El objetivo de estos casos es practicar el recorrido desde una alerta hasta una decisión documentada, utilizando registros de equipos, identidades, red y nube.

**Avance: 15 fichas planificadas; 10 controladas y 5 de honeypot; ninguna investigación completada ni incidente abierto a partir de estas fichas.** No existe telemetría pública recopilada. Cada ficha recoge el objetivo, las evidencias necesarias y sus dependencias. Las técnicas ATT&CK y la clasificación se incorporarán durante el análisis de los eventos observados.

## Controlled Detection Lab — SOC-001–SOC-010

**CONTROLLED TELEMETRY.** Se preservan números, alcance y dependencias. SOC-009 requiere muestra sintética y SOC-010 actividad controlada de AWS sanitizada; cada ficha identifica su origen exacto.

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

## Internet Honeypot — SOC-011–SOC-015

**OBSERVED INTERNET TELEMETRY. Evidence Origin: Observed Honeypot Telemetry.** La procedencia es la requerida para completar estas fichas, no una afirmación de datos ya existentes. Todos los casos están en `NO DATA — DEPLOYMENT PENDING` y dependen de HP-2/HP-3, cobertura y comportamiento real suficiente.

| Caso | Evidencia necesaria |
| --- | --- |
| [SOC-011 — Internet SSH Brute Force](SOC-011-internet-ssh-brute-force/README.md) | Autenticación, frecuencia, resultados, ASN/GeoIP y antecedentes |
| [SOC-012 — Interactive Honeypot Session](SOC-012-interactive-honeypot-session/README.md) | Sesión real, secuencia de comandos, intentos de descarga y duración |
| [SOC-013 — Distributed Credential Activity](SOC-013-distributed-credential-activity/README.md) | Similitud entre fuentes, tiempos y alternativas a coordinación |
| [SOC-014 — Internet Reconnaissance](SOC-014-internet-reconnaissance/README.md) | Probing, puertos/protocolos y punto de observación verificado |
| [SOC-015 — Network Traffic Anomaly](SOC-015-network-traffic-anomaly/README.md) | Tasas de red, baseline, distribución y evidencia de impacto/upstream |

No reemplazar actividad inexistente por simulaciones etiquetadas como Internet. La aceptación de sesión es emulada; **Observed Internet activity does not imply compromise of a production environment.** SOC-011 y posteriores seguirán este origen salvo excepción explícita documentada.

## Formato y evidencia

Los informes seguirán la [plantilla de incidente](../templates/incident-report.md): resumen, alerta, evaluación inicial, alcance, evidencias, línea de tiempo, indicadores, ATT&CK, análisis, clasificación, severidad, decisión, acciones y lecciones aprendidas.

La primera investigación será SOC-001, después de validar la recopilación SSH en Linux. Los originales se conservarán de forma privada y solo se publicarán fragmentos revisados. Consulta el [manejo de evidencias](../docs/evidence-handling.md) y el [plan de implementación](../docs/implementation-checklist.md).
