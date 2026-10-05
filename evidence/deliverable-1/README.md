# Evidencia del entregable 1

**DELIVERABLE 1 — COMPLETE. CONTROLLED TELEMETRY:** validación benigna del 2026-10-05, sin ataques ni incidentes. Se conservan [preflight](preflight.md), [despliegue histórico Wazuh](wazuh-deployment.md) y [Windows preparado el 2026-09-30 y completado el 2026-10-05](windows-deployment.md).

| Fuente | Local | Wazuh | Evidencia |
| --- | --- | --- | --- |
| Security | PASS | PASS | [security.md](security.md) / [JSON](security-event.json) |
| System | PASS | PASS | [system.md](system.md) / [JSON](system-event.json) |
| Sysmon | PASS | PASS | [sysmon.md](sysmon.md) / [JSON](sysmon-event.json) |
| PowerShell | PASS | PASS | [powershell.md](powershell.md) / [JSON](powershell-event.json) |
| Defender | PASS | PASS | [defender.md](defender.md) / [JSON](defender-event.json) |

Orden real: Security → System → Sysmon → PowerShell → Defender. Cada JSON conserva identidad local, agent ID 001, localizador manager, índice/document ID, consulta real y comparación de campos. Sysmon incorpora además [red privada](sysmon-network-event.json). La [sesión](telemetry-session.json) conserva ventana cerrada, espacio/volumen/relojes y límites de archives.

## Artefactos publicados

- [Inventario Windows](windows-native-checks.json), [revisión final Windows](windows-final-checks.json) y [salud conjunta final](operational-final-checks.json).
- [Configuración efectiva/suscripciones del agente](windows-agent-checks.json), [observación Dashboard](windows-agent-dashboard.json) y [captura original de la fila active](windows-agent-dashboard.png), tomada a 2026-10-05T19:35:30Z. Prueba aparición/estado en ese momento; no sustituye la cadena de cada evento.
- [Instalación Sysmon](sysmon-install-observed.txt), [configuración efectiva](sysmon-effective-observed.txt) y [política PowerShell](powershell-policy-observed.json).
- Los cinco JSON de eventos enlazados arriba y [segunda muestra Sysmon](sysmon-network-event.json).
- [Checkpoints](deliverable-1-snapshots.json), [revisión estática](repository-validation.json) y [SHA256SUMS](SHA256SUMS).

Los JSON son extractos de originales privados; no son eventos de ejemplo. Se aplicó lista permitida de campos, se omitieron usuarios/SIDs, mensajes completos, claves y datos ajenos al lab. Las comparaciones preceden a la sanitización. Campo omitido para publicar no equivale a campo ausente de la fuente. La salida Sysmon se transcodificó UTF-16LE→UTF-8. La captura Dashboard permanece sin alterar. Aplicar [manejo de evidencias](../../docs/evidence-handling.md).

## Cadena exigida por fuente

Windows local → configuración efectiva/servicio/suscripción del agente → evento idéntico en manager → documento consultado en indexer mediante `_search` autenticado a través del Dashboard. No se inventó ACK individual del agente. La coincidencia del evento bajo ID 001 respalda la recogida. PASS demuestra esta cadena puntual; no una alerta, detección de ataque o cobertura completa. Ausencias y diferencias de escapes/espacios se conservan en las fichas.

Archives volvió a estar deshabilitado tras comprobar los documentos; las cinco fuentes del agente siguen activas. Los nuevos eventos sin alerta no se indexarán como archives después del cierre. Propuesta de revisión de retención: siete días, 2026-10-12, sin borrado automático implementado.

## Snapshots

Todos fueron leídos de VirtualBox, con UUID/UTC reales; los discos y snapshots quedan fuera de Git. Los checkpoints Windows se crearon cuando existía su estado: base activada y protegida → agente ACTIVE observado → Sysmon/configuración aceptados → validación completa/archives cerrado/tarea temporal retirada. Los dos checkpoints Wazuh previos se conservan y se añade el final.

| VM | Nombre | UUID | UTC | Estado del checkpoint |
| --- | --- | --- | --- | --- |
| SOC-WAZUH | `SOC-WAZUH-base-install` | `e0d50517-8586-4723-9224-28e68578d9ee` | `2026-09-26T19:44:39Z` | Apagado, sin RAM |
| SOC-WAZUH | `SOC-WAZUH-wazuh-operational` | `914fc1c2-0c02-41c4-980e-b8c8481217ab` | `2026-09-29T17:01:25Z` | Apagado, sin RAM |
| SOC-WAZUH | `SOC-WAZUH-deliverable-1-validated` | `f9610b8c-74b3-484d-88f4-c2e8a4f22f55` | `2026-10-05T20:12:14Z` | Apagado, sin RAM |
| SOC-WIN11 | `SOC-WIN11-base-install` | `90bb1641-7025-49a2-a5b0-5ba3ac260f2a` | `2026-10-05T19:09:50Z` | Apagado, sin RAM |
| SOC-WIN11 | `SOC-WIN11-wazuh-agent` | `73e66ce8-02f9-4241-836c-414246c5d18c` | `2026-10-05T19:36:16Z` | Apagado, sin RAM |
| SOC-WIN11 | `SOC-WIN11-sysmon-configured` | `3dd9edf1-8aed-42e4-81f7-dc67c669c0c2` | `2026-10-05T19:44:18Z` | Apagado, sin RAM |
| SOC-WIN11 | `SOC-WIN11-deliverable-1-validated` | `29e81f5e-787a-40c0-ab72-6095b2bb8926` | `2026-10-05T20:12:08Z` | Apagado, sin RAM |

Restaurar puede cambiar relojes o enrollment; volver a comprobar ambos antes de generar eventos. Ningún snapshot reemplaza los originales ni backups privados.
