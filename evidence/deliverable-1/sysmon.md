# Evidencia validada: Sysmon

**Evidence Origin: Controlled Simulation** — actividad normal autorizada, sin ataques. **Local PASS / Wazuh PASS**, observado el 2026-10-05. Responsable: operador asistido por Codex.

Se ejecutó `cmd.exe /c echo SOC-D1-20261005-SYSMON-BENIGN` y luego una única conexión privada benigna con `Test-NetConnection` a TCP/1514 del manager. Sysmon 15.22 usa el XML original del repositorio; instalación y configuración efectiva verificadas antes de esta fuente.

| Etapa | Resultado observado | Evidencia |
| --- | --- | --- |
| Windows local | PASS — evento 1, RecordID 530 | [Extracto y comparación](sysmon-event.json) |
| Wazuh Agent | PASS — ID `001`, cinco suscripciones, servicio Running; recogida respaldada por evento idéntico en manager | [Configuración y log](windows-agent-checks.json), [Dashboard](windows-agent-dashboard.png) |
| Wazuh Manager | PASS — 1 coincidencia en JSON archives bajo el agente `001` | [Identidad y localizador](sysmon-event.json) |
| Wazuh searchable document | PASS — 1 coincidencia por `_search` autenticado a través del Dashboard | [Consulta y documento](sysmon-event.json) |
| Campos | Seis campos de identidad idénticos; EventData: 15 MATCH, 1 ABSENT, 7 DIFFERS | Comparación de originales privados antes de omitir datos |

## Evento y búsqueda reproducible

- Equipo: `SOC-WIN11`; Windows Enterprise Evaluation 25H2 `26200.6584`, agente `4.14.8`.
- Canal: `Microsoft-Windows-Sysmon/Operational`; proveedor: `Microsoft-Windows-Sysmon`.
- Event ID: `1`; EventRecordID: `530`.
- UTC original, sin truncar: `2026-10-05T19:54:15.6489722Z`; extracción: `2026-10-05T19:54:18.6289419Z`.
- Manager timestamp: `2026-10-05T19:54:28.419+0000`; evento archives ID `1791230068.9563188`.
- Índice: `wazuh-archives-4.x-2026.10.05`; document ID: `PlGhDaEBlMjr8RN1zJIc`.
- Consulta realizada: `2026-10-05T19:54:51.359021+00:00`. El JSON conserva el cuerpo `_search` real con agent name/ID, channel, provider, computer, event ID, record ID y SystemTime. No se afirma una búsqueda visual en Discover.
- Zona original Windows: Pacific Standard Time, UTC−07:00 en esta fecha. Identidad/correlación usa `SystemTime` UTC, no la hora de pantalla ni la hora de recepción. [Ventana, relojes y cierre](telemetry-session.json).

## Campos y límites

Ausentes en el EventData decodificado de manager e indexer: `RuleName`.

Valores que difieren de su representación local: `Image`, `CommandLine`, `CurrentDirectory`, `User`, `ParentImage`, `ParentCommandLine`, `ParentUser`.

ProcessCreate conserva ProcessGuid, ProcessId, UtcTime, ParentProcessGuid/Id, IntegrityLevel y SHA256 reales. `RuleName` no está en el EventData decodificado. Los DIFFERS corresponden a representación de escapes y espacios finales; se conservan ambos valores sin forzar igualdad. Usuario/ParentUser y ParentCommandLine se compararon en privado y se omitieron de la publicación. DNS, FileCreate y RegistryEvent no se validaron mediante correlación en esta sesión.

La recogida por el agente se infiere de su configuración efectiva, suscripción, servicio/conexión y la coincidencia del evento bajo ID `001` en manager. No se observó ni se inventa un ACK individual del agente. La consulta usa JSON archives; una ingestión PASS no demuestra una alerta ni una detección de ataque. No se cambió el umbral de alertas ni se añadieron reglas.

## Extracción y publicación

`Get-WinEvent` y `ToXml()` dentro de Windows conservaron XML y EventData originales en almacenamiento privado; se compararon con `/var/ossec/logs/archives/archives.json` y el `_source` indexado. Se publica una lista permitida de campos; se omiten mensajes completos, usuarios, SIDs y datos ajenos a la prueba. Omitido por sanitización no significa ausente de la fuente. El JSON identifica cada campo comparado y su resultado; las identidades y consultas se conservan reales. Hash del artefacto sanitizado en [SHA256SUMS](SHA256SUMS).

La segunda cadena también pasó: NetworkConnect ID `3`, RecordID `554`, UTC `2026-10-05T19:54:45.8239373Z`, de `.30` a `.10:1514`. [Evento, consulta y comparación de red](sysmon-network-event.json). Documento `fVGiDaEBlMjr8RN1fJNi` del mismo índice archives; ProcessGuid/Id y direcciones/puertos observados se conservan. No se afirma que sea el mismo proceso cmd: el iniciador de red es PowerShell.

En NetworkConnect, `SourceHostname`, `SourcePortName`, `DestinationHostname` y `DestinationPortName` están ausentes del EventData decodificado. `Image` y `User` presentan diferencias de escapes; direcciones, puertos, protocolo, ProcessGuid/Id, UtcTime y RuleName coinciden. No se reconstruyen nombres de host o servicio a partir de IP/puerto.
