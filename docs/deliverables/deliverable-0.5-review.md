# Entregable 0.5 — Revisión de arquitectura y cierre

**Fecha: 25 de septiembre de 2026. Alcance: arquitectura y documentación.** Base de esta revisión: `9834c9b`. El refactor híbrido, las quince fichas, los tres diseños de paneles y la plantilla semanal ya existían en esa base. Se preservan y se revisan; no se presentan como archivos creados de nuevo. El [informe inicial de 0.5](deliverable-0.5.md) conserva su inventario histórico y sus comprobaciones anteriores.

El estado inicial mostró 52 archivos modificados únicamente por CRLF/LF. Se comprobó igualdad de contenido con `HEAD` tras normalizar saltos de línea y se restauró LF sin perder texto. `.gitattributes` fija esa convención para documentación y Python. No había cambios de contenido ni archivos preparados antes de esta revisión.

## Cobertura de los requisitos

Los siguientes resultados son documentales. Ninguno acredita controles desplegados ni telemetría real.

| Tareas solicitadas | Resultado y evidencia |
| --- | --- |
| 1–2: inspección y preservación | Conservados archivos, directorios, validador, informe 0, plantillas e incidentes; [arquitectura original ampliada](../architecture.md) y antecedentes de operación preservados |
| 3–5: modelo híbrido, frontera y Cowrie | [README](../../README.md), [seguridad](../../honeypot/security-model.md) y [requisitos Cowrie](../../configs/honeypot/cowrie/README.md): sensor externo, emulación y administración separada |
| 6–7: transporte y Mermaid | [Pipeline](../../honeypot/telemetry-pipeline.md): envío saliente autenticado al receptor, copia minimizada y lotes sin conexión al SOC; tres diagramas alineados |
| 8: supuestos y riesgos | Firewall/egress, datos hostiles, fallos y recuperación en seguridad; [lista previa](../../honeypot/deployment-checklist.md) exige AUP, ToS, abuso, banda y cargos |
| 9: GeoIP | [Enriquecimiento](../../enrichment/README.md): estimación de IP, intermediarios, fuentes y límites; consultas externas opcionales fuera del SOC |
| 10–12: paneles | [Global Honeypot Activity](../../dashboards/attack-map/README.md), [SOC Overview](../../dashboards/soc-overview/README.md) y [Network Anomalies](../../dashboards/network-anomalies/README.md) conservan especificaciones y NO DATA — DEPLOYMENT PENDING |
| 13: nuevas investigaciones | [SOC-011–SOC-015](../../incidents/README.md#internet-honeypot--soc-011soc-015) ya reservadas para observaciones reales, sin renumerar SOC-001–SOC-010 ni completar casos ficticios |
| 14: reporte semanal | [Plantilla](../../reports/templates/weekly-honeypot-threat-report.md) conserva métricas pendientes, decisiones y limitaciones; añade revisiones por lotes tardíos |
| 15–17: plan, siguiente etapa y estado | [Checklist](../implementation-checklist.md) y README mantienen 1 después de 0.5; [decisiones HP-1](../../honeypot/implementation-decisions.md) separan arquitectura de elecciones pendientes |
| 18–22: enlaces, validación, espacios, diff y commit | Evidencia de cierre debajo; un único commit local de esta revisión, sin despliegue ni publicación remota |

Los [campos Wazuh](../../configs/honeypot/wazuh/README.md) siguen siendo requisitos semánticos pendientes de inspeccionar eventos; no se añadieron decodificadores ni reglas. Se preservan [Suricata público](../../honeypot/suricata-visibility.md), [evidencia sanitizada](../../datasets/sanitized-honeypot/README.md) y [T-Pot opcional](../../honeypot/README.md#fases-posteriores-y-t-pot).

## Ajustes de esta revisión

- Separar original restringido, copia analítica privada y extracto público; minimizar y validar el lote antes del colector Wazuh, incluidos secretos repetidos en texto.
- Exigir comprobación del reloj de correlación y consultas por tiempo de evento; un lote atrasado no prueba una ráfaga. Versionar informes corregidos por llegadas tardías.
- Situar consultas externas opcionales en una estación dedicada, sin conexión simultánea al SOC; retornar resultados revisados mediante la frontera de datos existente.
- Registrar decisiones HP-1 y sus pruebas; verificar recepción mínima en Wazuh antes de apertura y reservar validación analítica completa para HP-3.
- Conservar notas de VirtualBox/SOC-LAB como antecedentes que deben revalidarse; actualizar estado y evidencia de cierre sin atribuir nuevos despliegues.

## Archivos creados y modificados

**3 archivos creados y 14 modificados; ninguno eliminado.** Los espacios solicitados para honeypot, configuraciones, paneles, enriquecimiento, informes y datasets ya existían y se conservan.

| Estado | Archivo | Cambio |
| --- | --- | --- |
| Creado | [.gitattributes](../../.gitattributes) | Convención de finales de línea sin cambios de contenido en archivos preservados |
| Creado | [honeypot/implementation-decisions.md](../../honeypot/implementation-decisions.md) | Decisiones HP-1, responsables pendientes y evidencia requerida |
| Creado | [docs/deliverables/deliverable-0.5-review.md](deliverable-0.5-review.md) | Esta revisión, trazabilidad de requisitos, inventario y validación |
| Modificado | [README.md](../../README.md) | Estado, diagrama, antecedentes locales y enlaces de cierre |
| Modificado | [configs/honeypot/cowrie/README.md](../../configs/honeypot/cowrie/README.md) | Emulación local explícita, sin backend externo |
| Modificado | [configs/honeypot/wazuh/README.md](../../configs/honeypot/wazuh/README.md) | Minimización antes del colector y aceptación temporal por lotes |
| Modificado | [dashboards/README.md](../../dashboards/README.md) | Corte de ingestión y corrección de ventanas tardías |
| Modificado | [docs/architecture.md](../architecture.md) | Diagrama y separación de copias, enriquecimiento y relojes |
| Modificado | [docs/deliverables/deliverable-0.5.md](deliverable-0.5.md) | Distinguir evidencia histórica de esta revisión |
| Modificado | [docs/implementation-checklist.md](../implementation-checklist.md) | Criterios HP-1/HP-2/HP-3 y verificación previa de red existente |
| Modificado | [docs/lab-operations.md](../lab-operations.md) | Nota de alcance sin retirar procedimientos ni antecedentes |
| Modificado | [enrichment/README.md](../../enrichment/README.md) | Ubicación de consultas y retorno seguro de resultados |
| Modificado | [honeypot/README.md](../../honeypot/README.md) | Índice del registro de decisiones |
| Modificado | [honeypot/deployment-checklist.md](../../honeypot/deployment-checklist.md) | Controles de minimización y recepción antes de apertura |
| Modificado | [honeypot/security-model.md](../../honeypot/security-model.md) | Excepciones de egress acotadas y riesgo de importación tardía/parcial |
| Modificado | [honeypot/telemetry-pipeline.md](../../honeypot/telemetry-pipeline.md) | Diagrama de copias, validación de lotes y fronteras de datos |
| Modificado | [reports/templates/weekly-honeypot-threat-report.md](../../reports/templates/weekly-honeypot-threat-report.md) | Revisiones trazables por datos tardíos |

## Validación de esta revisión

La comprobación inicial fue `python3 scripts/validate_repository.py`: **299 enlaces internos en 50 archivos Markdown**, con salida 0. Los 49 Markdown del informe histórico no describen la base actual, que ya incluye la guía de operaciones.

| Comprobación | Resultado |
| --- | --- |
| `python3 scripts/validate_repository.py` | Salida 0: **355 enlaces internos en 52 archivos Markdown**, incluidas rutas y anclas |
| `git diff --check` | Salida 0, sin errores de espacios |
| `git diff --cached --check` | Salida 0, sin errores de espacios |
| Preservación frente a `9834c9b` | Los 58 archivos de la base siguen presentes; 30 archivos seleccionados idénticos byte a byte: informe 0, validador, `.gitignore`, ambas plantillas SOC, índice y 15 fichas de incidentes, seis `.gitkeep` y tres especificaciones de paneles |
| IDs, procedencia y estado | 15 IDs únicos con Evidence Origin válido al inicio; SOC-011–SOC-015 y tres paneles conservan NO DATA — DEPLOYMENT PENDING |
| Formato de enlaces | Los 52 Markdown usan enlaces en línea compatibles con el validador; sin enlaces por referencia ni HTML detectados |
| Exclusiones de evidencia | `git check-ignore --no-index`: 10 rutas privadas excluidas y 4 rutas de configuración/extractos permitidas; no se crearon muestras para comprobarlo |
| Inventario y diff completo | 3 archivos nuevos y 14 modificados, revisados; sin eliminaciones. Solo texto UTF-8 menor de 1 MiB por archivo, sin configuración ejecutable, telemetría, payloads, PCAP ni imágenes añadidas |
| Mermaid | Tres diagramas revisados como código: README, arquitectura y pipeline; sin generar imágenes ni verificar renderizado visual |

El validador original se conserva sin cambios. Estas comprobaciones no demuestran funcionamiento de infraestructura, integración, reglas, métricas ni privacidad de datos futuros. La igualdad byte a byte y el inventario se comprobaron contra Git mediante Python; no se ejecutaron los procedimientos operativos de las guías.

Se contrastaron las referencias oficiales de [modos Cowrie](https://docs.cowrie.org/en/latest/README.html), [eventos Cowrie](https://docs.cowrie.org/en/latest/OUTPUT.html), [JSON Wazuh](https://documentation.wazuh.com/current/user-manual/ruleset/decoders/json-decoder.html), [archivo Wazuh](https://documentation.wazuh.com/current/user-manual/manager/event-logging.html), [sintaxis de reglas Wazuh](https://documentation.wazuh.com/current/user-manual/ruleset/ruleset-xml-syntax/rules.html), [EVE Suricata](https://docs.suricata.io/en/latest/output/eve/eve-json-output.html) y [precisión GeoIP](https://support.maxmind.com/knowledge-base/articles/maxmind-geolocation-accuracy). Son referencias de diseño; no sustituyen eventos ni pruebas de una versión instalada. No se hizo validación automática de todos los enlaces externos.

Commit local de esta revisión: `docs: extend SOC lab with isolated Internet honeypot architecture`. Su hash se consulta en Git para evitar una referencia circular en el propio commit.

## Decisiones pendientes y siguiente entregable

Siguen pendientes proveedor/región y permiso, recursos y presupuesto, versión/aislamiento Cowrie, management plane, firewall/egress concreto, mecanismo y endpoints del transporte, medio/cadencia de transferencia, retención/cuotas, salud/recuperación, cobertura Suricata, fuentes GeoIP/ASN y tecnología del mapa. Campos, índices, reglas, umbrales, ATT&CK y baseline requieren eventos inspeccionados y pruebas futuras. El [registro HP-1](../../honeypot/implementation-decisions.md) define evidencia y responsables por completar.

**Siguiente entregable: 1 — Wazuh, Windows y Sysmon.** Verificar recursos, hipervisor y red existente; verificar o crear la red aislada `10.10.10.0/24`; desplegar únicamente SOC-WAZUH `10.10.10.10` y SOC-WIN11 `10.10.10.30`, con agente Wazuh, Sysmon y Defender activo. Configurar Security, System, PowerShell Operational, Sysmon Operational y Defender Operational; demostrar eventos inocuos desde cada canal hasta una consulta en el SIEM, con UTC/desfase, campos, latencia, aislamiento, instantáneas y evidencia revisada. Conservar coberturas no verificadas como pendientes. El [plan detallado](../implementation-checklist.md#entregable-1--wazuh-windows-y-sysmon) mantiene los criterios originales.

Cowrie/VPS, receptor, puertos públicos, T-Pot, simulaciones de ataque, Linux, AD, Suricata, AWS y Splunk siguen en fases posteriores. No se instalaron componentes, modificaron recursos cloud, generaron datos ni crearon screenshots. **La ejecución se detiene en 0.5.**
