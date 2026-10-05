# Evidencia validada: System

**Evidence Origin: Controlled Simulation** — actividad normal autorizada, sin ataques. **Local PASS / Wazuh PASS**, observado el 2026-10-05. Responsable: operador asistido por Codex.

Se seleccionó un evento normal ya existente de `Microsoft-Windows-Winlogon`, ID 7001, RecordID 824, asociado al inicio de sesión de consola. No se provocó una avería de servicios. La selección inicial de SCM/7036 no encontró eventos en la ventana; se inspeccionó el canal y se usó el evento realmente disponible.

| Etapa | Resultado observado | Evidencia |
| --- | --- | --- |
| Windows local | PASS — evento 7001, RecordID 824 | [Extracto y comparación](system-event.json) |
| Wazuh Agent | PASS — ID `001`, cinco suscripciones, servicio Running; recogida respaldada por evento idéntico en manager | [Configuración y log](windows-agent-checks.json), [Dashboard](windows-agent-dashboard.png) |
| Wazuh Manager | PASS — 1 coincidencia en JSON archives bajo el agente `001` | [Identidad y localizador](system-event.json) |
| Wazuh searchable document | PASS — 1 coincidencia por `_search` autenticado a través del Dashboard | [Consulta y documento](system-event.json) |
| Campos | Seis campos de identidad idénticos; EventData: 2 MATCH, 0 ABSENT, 0 DIFFERS | Comparación de originales privados antes de omitir datos |

## Evento y búsqueda reproducible

- Equipo: `SOC-WIN11`; Windows Enterprise Evaluation 25H2 `26200.6584`, agente `4.14.8`.
- Canal: `System`; proveedor: `Microsoft-Windows-Winlogon`.
- Event ID: `7001`; EventRecordID: `824`.
- UTC original, sin truncar: `2026-10-05T19:46:52.7132190Z`; extracción: `2026-10-05T19:53:12.8437126Z`.
- Manager timestamp: `2026-10-05T19:47:51.796+0000`; evento archives ID `1791229671.8544282`.
- Índice: `wazuh-archives-4.x-2026.10.05`; document ID: `R1GbDaEBlMjr8RN1w4S5`.
- Consulta realizada: `2026-10-05T19:53:47.845802+00:00`. El JSON conserva el cuerpo `_search` real con agent name/ID, channel, provider, computer, event ID, record ID y SystemTime. No se afirma una búsqueda visual en Discover.
- Zona original Windows: Pacific Standard Time, UTC−07:00 en esta fecha. Identidad/correlación usa `SystemTime` UTC, no la hora de pantalla ni la hora de recepción. [Ventana, relojes y cierre](telemetry-session.json).

## Campos y límites

Ausentes en el EventData decodificado de manager e indexer: Ninguno entre los campos EventData comparados.

Valores que difieren de su representación local: Ninguno.

El evento local contiene `TSId` y `UserSid`. El SID se comparó en los originales privados y se omitió de la publicación. Esta muestra no aporta CommandLine, Hashes ni una dirección remota; no se reconstruyen a partir del evento Security cercano.

La recogida por el agente se infiere de su configuración efectiva, suscripción, servicio/conexión y la coincidencia del evento bajo ID `001` en manager. No se observó ni se inventa un ACK individual del agente. La consulta usa JSON archives; una ingestión PASS no demuestra una alerta ni una detección de ataque. No se cambió el umbral de alertas ni se añadieron reglas.

## Extracción y publicación

`Get-WinEvent` y `ToXml()` dentro de Windows conservaron XML y EventData originales en almacenamiento privado; se compararon con `/var/ossec/logs/archives/archives.json` y el `_source` indexado. Se publica una lista permitida de campos; se omiten mensajes completos, usuarios, SIDs y datos ajenos a la prueba. Omitido por sanitización no significa ausente de la fuente. El JSON identifica cada campo comparado y su resultado; las identidades y consultas se conservan reales. Hash del artefacto sanitizado en [SHA256SUMS](SHA256SUMS).
