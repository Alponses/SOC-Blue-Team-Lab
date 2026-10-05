# Evidencia validada: Security

**Evidence Origin: Controlled Simulation** — actividad normal autorizada, sin ataques. **Local PASS / Wazuh PASS**, observado el 2026-10-05. Responsable: operador asistido por Codex.

Se seleccionó el inicio exitoso normal de consola: 4624, LogonType 2 y LogonProcessName `User32`. La sesión auxiliar `Advapi` de VirtualBox se conservó como diagnóstico privado y se excluyó de esta ficha. Hubo un fallo incidental de entrada automatizada de contraseña; no se usó como prueba ni se generaron fallos intencionados.

| Etapa | Resultado observado | Evidencia |
| --- | --- | --- |
| Windows local | PASS — evento 4624, RecordID 6609 | [Extracto y comparación](security-event.json) |
| Wazuh Agent | PASS — ID `001`, cinco suscripciones, servicio Running; recogida respaldada por evento idéntico en manager | [Configuración y log](windows-agent-checks.json), [Dashboard](windows-agent-dashboard.png) |
| Wazuh Manager | PASS — 1 coincidencia en JSON archives bajo el agente `001` | [Identidad y localizador](security-event.json) |
| Wazuh searchable document | PASS — 1 coincidencia por `_search` autenticado a través del Dashboard | [Consulta y documento](security-event.json) |
| Campos | Seis campos de identidad idénticos; EventData: 20 MATCH, 6 ABSENT, 2 DIFFERS | Comparación de originales privados antes de omitir datos |

## Evento y búsqueda reproducible

- Equipo: `SOC-WIN11`; Windows Enterprise Evaluation 25H2 `26200.6584`, agente `4.14.8`.
- Canal: `Security`; proveedor: `Microsoft-Windows-Security-Auditing`.
- Event ID: `4624`; EventRecordID: `6609`.
- UTC original, sin truncar: `2026-10-05T19:46:52.6679989Z`; extracción: `2026-10-05T19:49:44.3229148Z`.
- Manager timestamp: `2026-10-05T19:47:52.242+0000`; evento archives ID `1791229672.8555021`.
- Índice: `wazuh-archives-4.x-2026.10.05`; document ID: `TFGbDaEBlMjr8RN1w4S5`.
- Consulta realizada: `2026-10-05T19:50:28.437804+00:00`. El JSON conserva el cuerpo `_search` real con agent name/ID, channel, provider, computer, event ID, record ID y SystemTime. No se afirma una búsqueda visual en Discover.
- Zona original Windows: Pacific Standard Time, UTC−07:00 en esta fecha. Identidad/correlación usa `SystemTime` UTC, no la hora de pantalla ni la hora de recepción. [Ventana, relojes y cierre](telemetry-session.json).

## Campos y límites

Ausentes en el EventData decodificado de manager e indexer: `TransmittedServices`, `LmPackageName`, `RestrictedAdminMode`, `RemoteCredentialGuard`, `TargetOutboundUserName`, `TargetOutboundDomainName`.

Valores que difieren de su representación local: `LogonProcessName`, `ProcessName`.

Wazuh elimina el espacio final de `User32 ` y cambia la representación de escapes en `ProcessName`; se publican ambas representaciones y se conservan como DIFFERS, sin forzar igualdad. Los seis campos de identidad y LogonType sí coinciden. La dirección local observada es loopback `127.0.0.1`, no una atribución a un origen externo.

La recogida por el agente se infiere de su configuración efectiva, suscripción, servicio/conexión y la coincidencia del evento bajo ID `001` en manager. No se observó ni se inventa un ACK individual del agente. La consulta usa JSON archives; una ingestión PASS no demuestra una alerta ni una detección de ataque. No se cambió el umbral de alertas ni se añadieron reglas.

## Extracción y publicación

`Get-WinEvent` y `ToXml()` dentro de Windows conservaron XML y EventData originales en almacenamiento privado; se compararon con `/var/ossec/logs/archives/archives.json` y el `_source` indexado. Se publica una lista permitida de campos; se omiten mensajes completos, usuarios, SIDs y datos ajenos a la prueba. Omitido por sanitización no significa ausente de la fuente. El JSON identifica cada campo comparado y su resultado; las identidades y consultas se conservan reales. Hash del artefacto sanitizado en [SHA256SUMS](SHA256SUMS).
