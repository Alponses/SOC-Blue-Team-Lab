# Evidencia validada: PowerShell

**Evidence Origin: Controlled Simulation** — actividad normal autorizada, sin ataques. **Local PASS / Wazuh PASS**, observado el 2026-10-05. Responsable: operador asistido por Codex.

Después de validar Sysmon, se observó y habilitó la política `EnableScriptBlockLogging=1`. Una sesión nueva de Windows PowerShell 5.1 ejecutó exactamente el marcador `SOC-D1-20261005-POWERSHELL-BENIGN` y `Get-Date`. Se seleccionó el bloque exacto del proceso hijo, excluyendo el script auxiliar de extracción.

| Etapa | Resultado observado | Evidencia |
| --- | --- | --- |
| Windows local | PASS — evento 4104, RecordID 2109 | [Extracto y comparación](powershell-event.json) |
| Wazuh Agent | PASS — ID `001`, cinco suscripciones, servicio Running; recogida respaldada por evento idéntico en manager | [Configuración y log](windows-agent-checks.json), [Dashboard](windows-agent-dashboard.png) |
| Wazuh Manager | PASS — 1 coincidencia en JSON archives bajo el agente `001` | [Identidad y localizador](powershell-event.json) |
| Wazuh searchable document | PASS — 1 coincidencia por `_search` autenticado a través del Dashboard | [Consulta y documento](powershell-event.json) |
| Campos | Seis campos de identidad idénticos; EventData: 4 MATCH, 1 ABSENT, 0 DIFFERS | Comparación de originales privados antes de omitir datos |

## Evento y búsqueda reproducible

- Equipo: `SOC-WIN11`; Windows Enterprise Evaluation 25H2 `26200.6584`, agente `4.14.8`.
- Canal: `Microsoft-Windows-PowerShell/Operational`; proveedor: `Microsoft-Windows-PowerShell`.
- Event ID: `4104`; EventRecordID: `2109`.
- UTC original, sin truncar: `2026-10-05T19:55:48.1738454Z`; extracción: `2026-10-05T19:55:52.6008908Z`.
- Manager timestamp: `2026-10-05T19:56:46.293+0000`; evento archives ID `1791230206.10379837`.
- Índice: `wazuh-archives-4.x-2026.10.05`; document ID: `9lGjDaEBlMjr8RN16Jdi`.
- Consulta realizada: `2026-10-05T19:57:09.490093+00:00`. El JSON conserva el cuerpo `_search` real con agent name/ID, channel, provider, computer, event ID, record ID y SystemTime. No se afirma una búsqueda visual en Discover.
- Zona original Windows: Pacific Standard Time, UTC−07:00 en esta fecha. Identidad/correlación usa `SystemTime` UTC, no la hora de pantalla ni la hora de recepción. [Ventana, relojes y cierre](telemetry-session.json).

## Campos y límites

Ausentes en el EventData decodificado de manager e indexer: `Path`.

Valores que difieren de su representación local: Ninguno.

[Política efectiva](powershell-policy-observed.json): PowerShell `5.1.26100.6584`, canal habilitado; la política previa no existía. `EnableScriptBlockInvocationLogging` no está definido, no se presenta como 0. El evento prueba el texto de este bloque; no se infiere transcripción, comandos anteriores ni otros hosts PowerShell. El Path vacío local y su ausencia decodificada se registran según la comparación.

La recogida por el agente se infiere de su configuración efectiva, suscripción, servicio/conexión y la coincidencia del evento bajo ID `001` en manager. No se observó ni se inventa un ACK individual del agente. La consulta usa JSON archives; una ingestión PASS no demuestra una alerta ni una detección de ataque. No se cambió el umbral de alertas ni se añadieron reglas.

## Extracción y publicación

`Get-WinEvent` y `ToXml()` dentro de Windows conservaron XML y EventData originales en almacenamiento privado; se compararon con `/var/ossec/logs/archives/archives.json` y el `_source` indexado. Se publica una lista permitida de campos; se omiten mensajes completos, usuarios, SIDs y datos ajenos a la prueba. Omitido por sanitización no significa ausente de la fuente. El JSON identifica cada campo comparado y su resultado; las identidades y consultas se conservan reales. Hash del artefacto sanitizado en [SHA256SUMS](SHA256SUMS).
