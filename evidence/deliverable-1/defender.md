# Evidencia validada: Defender

**Evidence Origin: Controlled Simulation** — actividad normal autorizada, sin ataques. **Local PASS / Wazuh PASS**, observado el 2026-10-05. Responsable: operador asistido por Codex.

Se ejecutó únicamente `Start-MpScan -ScanType QuickScan`, con Defender/Antivirus/RTP activos antes y después. Se observó inicio 1000/393 y finalización 1001/394 con el mismo Scan ID; ambos pasaron la cadena de ingestión. No se usaron malware, EICAR, exclusiones ni cambios de protección.

| Etapa | Resultado observado | Evidencia |
| --- | --- | --- |
| Windows local | PASS — evento 1001, RecordID 394 | [Extracto y comparación](defender-event.json) |
| Wazuh Agent | PASS — ID `001`, cinco suscripciones, servicio Running; recogida respaldada por evento idéntico en manager | [Configuración y log](windows-agent-checks.json), [Dashboard](windows-agent-dashboard.png) |
| Wazuh Manager | PASS — 1 coincidencia en JSON archives bajo el agente `001` | [Identidad y localizador](defender-event.json) |
| Wazuh searchable document | PASS — 1 coincidencia por `_search` autenticado a través del Dashboard | [Consulta y documento](defender-event.json) |
| Campos | Seis campos de identidad idénticos; EventData: 13 MATCH, 0 ABSENT, 0 DIFFERS | Comparación de originales privados antes de omitir datos |

## Evento y búsqueda reproducible

- Equipo: `SOC-WIN11`; Windows Enterprise Evaluation 25H2 `26200.6584`, agente `4.14.8`.
- Canal: `Microsoft-Windows-Windows Defender/Operational`; proveedor: `Microsoft-Windows-Windows Defender`.
- Event ID: `1001`; EventRecordID: `394`.
- UTC original, sin truncar: `2026-10-05T20:05:51.6382165Z`; extracción: `2026-10-05T20:05:53.6627879Z`.
- Manager timestamp: `2026-10-05T20:06:25.393+0000`; evento archives ID `1791230785.14379963`.
- Índice: `wazuh-archives-4.x-2026.10.05`; document ID: `eFGsDaEBlMjr8RN1vqo5`.
- Consulta realizada: `2026-10-05T20:06:48.707918+00:00`. El JSON conserva el cuerpo `_search` real con agent name/ID, channel, provider, computer, event ID, record ID y SystemTime. No se afirma una búsqueda visual en Discover.
- Zona original Windows: Pacific Standard Time, UTC−07:00 en esta fecha. Identidad/correlación usa `SystemTime` UTC, no la hora de pantalla ni la hora de recepción. [Ventana, relojes y cierre](telemetry-session.json).

## Campos y límites

Ausentes en el EventData decodificado de manager e indexer: Ninguno entre los campos EventData comparados.

Valores que difieren de su representación local: Ninguno.

La ficha principal valida la finalización. El proveedor aporta nombre/versión de producto, Scan ID, tipo/parámetros y duración. No aporta una creación de proceso, hash o destino de red del análisis; no se reconstruyen. Usuario/dominio/SID se compararon en privado y se omiten. Se conservan los tiempos originales del evento y del estado Mp; no se sustituyen unos por otros.

La recogida por el agente se infiere de su configuración efectiva, suscripción, servicio/conexión y la coincidencia del evento bajo ID `001` en manager. No se observó ni se inventa un ACK individual del agente. La consulta usa JSON archives; una ingestión PASS no demuestra una alerta ni una detección de ataque. No se cambió el umbral de alertas ni se añadieron reglas.

## Extracción y publicación

`Get-WinEvent` y `ToXml()` dentro de Windows conservaron XML y EventData originales en almacenamiento privado; se compararon con `/var/ossec/logs/archives/archives.json` y el `_source` indexado. Se publica una lista permitida de campos; se omiten mensajes completos, usuarios, SIDs y datos ajenos a la prueba. Omitido por sanitización no significa ausente de la fuente. El JSON identifica cada campo comparado y su resultado; las identidades y consultas se conservan reales. Hash del artefacto sanitizado en [SHA256SUMS](SHA256SUMS).

[Inicio 1000/393 correlacionado](defender-scan-start-event.json), documento `DFGkDaEBlMjr8RN1wZyY`. La finalización pertenece al mismo Scan ID. [Estado nativo de protecciones tras el análisis](defender-scan-observed.json).
