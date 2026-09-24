# Entregable 0.5 — Honeypot Architecture Refactor

**Fecha de cierre: 24 de septiembre de 2026. Estado: completado, alcance documental.** El entregable 0 y su [informe histórico](deliverable-0.md) se preservan. No se ha iniciado el entregable 1.

## Resultado de arquitectura

El proyecto ahora distingue **Controlled Detection Lab** en `10.10.10.0/24` e **Internet Honeypot** en un sensor público dedicado. Se conservan Wazuh, Windows/Sysmon, Linux/Audit, AD/DNS, Suricata, simulador, AWS/CloudTrail y Splunk. Las direcciones privadas y los diez casos originales no se renumeran ni se sustituyen.

Cowrie será el primer honeypot, con shell emulada, administración separada y sin ejecución de payloads. El diseño envía JSON por transporte saliente cifrado/autenticado a un receptor separado sin rutas al SOC; la base introduce lotes revisados sin conexión de red en Wazuh. El protocolo y la infraestructura exactos siguen pendientes. La demora por lotes queda explícita; no se promete analítica continua.

Se documentan firewall IPv4/IPv6, egress, proveedor, cuotas, fallos, recuperación, procedencia, parsing/normalización, detecciones posteriores a eventos reales, enriquecimiento opcional y seguridad de evidencia. GeoIP no atribuye identidad; un volumen alto no confirma DDoS. La visibilidad de Suricata depende del punto de captura. T-Pot permanece opcional y posterior a demostrar el pipeline Cowrie completo.

**Observed Internet activity does not imply compromise of a production environment.** Los dashboards son especificaciones y los casos nuevos son placeholders, todos sin datos: **NO DATA — DEPLOYMENT PENDING**.

## Archivos creados

22 archivos Markdown nuevos:

| Ubicación | Contenido |
| --- | --- |
| [honeypot/README.md](../../honeypot/README.md) | Propósito, Cowrie y T-Pot opcional |
| [honeypot/security-model.md](../../honeypot/security-model.md) | Zonas, firewall, egress, supuestos, riesgos y recuperación |
| [honeypot/telemetry-pipeline.md](../../honeypot/telemetry-pipeline.md) | Mermaid, transporte, transferencia, contrato y calidad |
| [honeypot/deployment-checklist.md](../../honeypot/deployment-checklist.md) | Revisión de proveedor y controles previos |
| [honeypot/suricata-visibility.md](../../honeypot/suricata-visibility.md) | Interfaz, cobertura y EVE |
| [configs/honeypot/README.md](../../configs/honeypot/README.md) | Índice de futuras configuraciones |
| [configs/honeypot/cowrie/README.md](../../configs/honeypot/cowrie/README.md) | Requisitos del sensor, sin configuración ejecutable |
| [configs/honeypot/wazuh/README.md](../../configs/honeypot/wazuh/README.md) | Contrato pendiente de campos, ingestión y reglas |
| [dashboards/README.md](../../dashboards/README.md) | Convenciones de origen, tiempo, métricas y datos ausentes |
| [dashboards/attack-map/README.md](../../dashboards/attack-map/README.md) | Global Honeypot Activity |
| [dashboards/soc-overview/README.md](../../dashboards/soc-overview/README.md) | SOC Overview |
| [dashboards/network-anomalies/README.md](../../dashboards/network-anomalies/README.md) | Tasas, baseline y clasificación DoS/DDoS |
| [enrichment/README.md](../../enrichment/README.md) | Fuentes, privacidad, confianza y limitaciones |
| [reports/README.md](../../reports/README.md) | Procedimiento de informes periódicos |
| [reports/templates/weekly-honeypot-threat-report.md](../../reports/templates/weekly-honeypot-threat-report.md) | Plantilla semanal para responsable SOC |
| [datasets/sanitized-honeypot/README.md](../../datasets/sanitized-honeypot/README.md) | Publicación de extractos y manifiestos |
| [SOC-011/README.md](../../incidents/SOC-011-internet-ssh-brute-force/README.md) | Internet SSH Brute Force |
| [SOC-012/README.md](../../incidents/SOC-012-interactive-honeypot-session/README.md) | Interactive Honeypot Session |
| [SOC-013/README.md](../../incidents/SOC-013-distributed-credential-activity/README.md) | Distributed Credential Activity |
| [SOC-014/README.md](../../incidents/SOC-014-internet-reconnaissance/README.md) | Internet Reconnaissance |
| [SOC-015/README.md](../../incidents/SOC-015-network-traffic-anomaly/README.md) | Network Traffic Anomaly |
| Este archivo: docs/deliverables/deliverable-0.5.md | Resultado, inventario, validación y siguiente alcance |

## Archivos modificados

22 archivos existentes, sin eliminaciones:

| Archivo o conjunto | Cambio |
| --- | --- |
| [.gitignore](../../.gitignore) | Exclusiones adicionales de salidas Cowrie/EVE, TTY, cuarentena y cola |
| [README.md](../../README.md) | Dos entornos, estado 0.5, diagrama, capacidades e índices |
| [docs/architecture.md](../architecture.md) | Arquitectura híbrida conservando red y componentes originales |
| [docs/implementation-checklist.md](../implementation-checklist.md) | 0.5 antes de 1; fases HP posteriores sin renumerar entregables |
| [docs/evidence-handling.md](../evidence-handling.md) | Evidence Origin, sanitización pública y seguridad de payloads |
| [configs/README.md](../../configs/README.md) | Enlace al nuevo espacio honeypot |
| [detections/README.md](../../detections/README.md) | Procedencia y campos verificados |
| [detections/wazuh/README.md](../../detections/wazuh/README.md) | Enlace al contrato y reglas futuras Cowrie |
| [detections/suricata/README.md](../../detections/suricata/README.md) | Diferencia de cobertura pública y privada |
| [incidents/README.md](../../incidents/README.md) | Índice de quince fichas y origen de cada entorno |
| [SOC-001](../../incidents/SOC-001-ssh-brute-force/README.md), [SOC-002](../../incidents/SOC-002-windows-authentication/README.md), [SOC-003](../../incidents/SOC-003-suspicious-powershell/README.md), [SOC-004](../../incidents/SOC-004-account-privilege-change/README.md), [SOC-005](../../incidents/SOC-005-network-scanning/README.md), [SOC-006](../../incidents/SOC-006-suspicious-network-connection/README.md), [SOC-007](../../incidents/SOC-007-dns-investigation/README.md), [SOC-008](../../incidents/SOC-008-file-integrity/README.md), [SOC-009](../../incidents/SOC-009-phishing/README.md), [SOC-010](../../incidents/SOC-010-aws-cloudtrail/README.md) — sus diez README.md | Solo metadatos de origen/entorno al inicio; cuerpo de cada ficha preservado |
| [templates/incident-report.md](../../templates/incident-report.md) | Procedencia obligatoria y análisis específico del honeypot |
| [templates/soc-playbook.md](../../templates/soc-playbook.md) | Comprobaciones de origen, límites y recuperación |

El validador original, el informe de entregable 0, las plantillas previas como base, los directorios originales y sus `.gitkeep` se conservan. No hay scripts de instalación, infraestructura como código, reglas inventadas, datasets, capturas ni binarios nuevos.

## Validación de cierre

La base inicial pasó `python3 scripts/validate_repository.py`: 112 enlaces internos en 27 Markdown. Los resultados finales se registran tras revisar todos los cambios:

| Comprobación | Resultado |
| --- | --- |
| Validador original: rutas y anclas Markdown | CORRECTO: 299 enlaces internos en 49 archivos Markdown |
| `git diff --check` y `git diff --cached --check` | Ambos sin errores de espacios |
| Preservación de archivos, incidentes y procedencia | 35 archivos originales presentes; informe 0 y validador idénticos; cuerpos SOC-001–SOC-010 idénticos tras retirar solo metadatos nuevos; 15 orígenes válidos al inicio |
| Exclusiones e inventario de archivos | 8 rutas privadas excluidas y 4 rutas de configuración/extractos permitidas mediante `git check-ignore`; 22 nuevos Markdown; archivos UTF-8 menores de 1 MiB; sin nuevos datos ni imágenes |
| Revisión de diff completo | Revisados todos los cambios preparados: 22 archivos nuevos y 22 modificados, sin eliminaciones ni trabajo ajeno; ajustes finales de claridad incluidos |

La revisión es documental. No valida red, seguridad operativa, ingestión, reglas, consultas ni paneles desplegados. Los diagramas Mermaid se revisan como código; su representación visual en GitHub permanece pendiente. No se generaron screenshots ni resultados de ataque. Se consultaron referencias oficiales de Cowrie, Wazuh, Suricata y GeoIP enlazadas junto a las afirmaciones técnicas; no se verifican todos los enlaces externos mediante el validador.

Mensaje del commit de cierre: `docs: extend SOC lab with isolated Internet honeypot architecture`. Base preservada: `833de89`. El hash final se consultará en el historial Git; no se introduce una referencia circular dentro del propio commit.

## Decisiones operativas sin resolver

- Proveedor/región permitidos, AUP/ToS, abuso, costes y límites de transferencia; ningún recurso ha sido creado.
- Recursos del anfitrión/hipervisor y de sensor/receptor, versión Cowrie, aislamiento del proceso y puertos de administración; Telnet es opcional.
- Transporte cifrado/autenticado exacto, identidades, endpoint, receptor y permisos; procedimiento/medio de transferencia sin conexión, responsable, frecuencia y latencia aceptable.
- Cuotas, retención, salud, pérdida tolerable, condiciones de parada y pruebas de recuperación.
- Interfaz/cobertura Suricata pública, métricas del host/proveedor y suficiencia del baseline; backend de mapa y fuentes/licencias GeoIP/ASN.
- Campos reales, parsing, normalización, índices, umbrales, severidad y técnicas ATT&CK; requieren eventos y validación posterior.

Estas decisiones no bloquean el cierre de arquitectura 0.5. Bloquean las tareas de despliegue que dependan de ellas.

## Alcance exacto del siguiente entregable

**Entregable 1 — Wazuh, Windows y Sysmon**, después de 0.5, conserva su alcance original: comprobar recursos/hipervisor y colisiones de subred; crear la red aislada; desplegar solo SOC-WAZUH `10.10.10.10` y SOC-WIN11 `10.10.10.30`; mantener Defender activo; configurar agente, Security, System, PowerShell Operational, Sysmon Operational y Defender Operational; comprobar tiempo y recepción de eventos inocuos de cada canal; documentar campos, consultas, retraso, ausencias, aislamiento e instantáneas, y guardar configuraciones/extractos revisados.

Un agente conectado no basta: se requiere evidencia de extremo a extremo por canal y limitaciones explícitas. El detalle está en el [plan de entregable 1](../implementation-checklist.md#entregable-1--wazuh-windows-y-sysmon). Requiere acceso operativo al hipervisor y a los invitados; no se ha ejecutado aquí.

Cowrie, VPS/receptor, puertos públicos, T-Pot, Linux/simulador, ataques, AD, Suricata, cambios AWS, Splunk y publicación remota quedan fuera del siguiente entregable y conservan sus fases propias. **El trabajo de esta sesión termina en 0.5.**
