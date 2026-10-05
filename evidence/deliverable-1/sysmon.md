# Evidencia pendiente: Sysmon

**Evidence Origin: Controlled Simulation** — taxonomía del repositorio para pruebas del operador; aquí solo validación benigna, sin ataques.

**REQUIRES MANUAL EXECUTION.** Host previsto: SOC-WIN11. Canal: `Microsoft-Windows-Sysmon/Operational`. Proveedor esperado: Microsoft-Windows-Sysmon. Conservar por separado proceso y conexión privada; creación de archivo opcional. DNS/registro/módulos/acceso a procesos no se presumen validados.

| Etapa | Resultado observado | Referencia de evidencia |
| --- | --- | --- |
| Evento local | No verificado | No recopilada |
| Canal/configuración efectiva y agente | No verificado | No recopilada |
| Evento correlacionado en manager | No verificado | No recopilada |
| Documento en indexer/Discover | No verificado | No recopilada |
| Campos comparados | Ninguno | No recopilada |

## Registro a completar con observaciones

- Versión Windows/agente/fuente y hostname real: pendiente.
- Event ID, EventRecordID, proveedor y canal observados: pendiente.
- Timestamp original, zona/UTC, desfase medido e inicio/fin de ventana: pendiente.
- Agent ID real, estado/hora, configuración aplicada y hash: pendiente.
- Datos locales y campos presentes/ausentes (sin reconstruir los ausentes): pendiente.
- Localizador en archives, consulta y correlación con el origen: pendiente.
- Índice, document ID, consulta, intervalo y hora de consulta en Discover: pendiente.
- Explicación de screenshot, si se obtiene: pendiente.
- Archivos publicados, SHA-256, método de extracción y sanitización: pendiente.
- Volumen/latencia observados, limitaciones, resultado y responsable: pendiente.

No completar campos con valores de ejemplo. Seguir la [guía](../../docs/telemetry-validation.md) y actualizar la [matriz](../../docs/deliverables/deliverable-1.md#matriz-de-validación) solo tras observar los resultados.
