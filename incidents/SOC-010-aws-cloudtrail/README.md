# SOC-010 — Investigación de AWS CloudTrail

**Estado: pendiente de ejecución.** Etapa prevista: 10. Todavía no hay evidencias ni una clasificación del caso.

## Objetivo

Reconstruir quién hizo qué, cuándo, desde dónde, contra qué recurso y qué cambió en la cuenta de laboratorio.

## Actividad prevista

Generar cambios controlados de IAM, llamadas API y operaciones sobre recursos en la cuenta propia de AWS.

## Evidencias necesarias

**Fuentes:** Estado de IAM, eventos CloudTrail y entrega a CloudWatch comprobada por separado.

Principal o sesión, acción, tiempo, origen, recurso, cambio, resultado de la API, permisos y limpieza. Solo se publicarán muestras sin claves ni identificadores reales.

## Dependencias y siguiente paso

Requiere delimitar cuenta, regiones, permisos, costes y recursos, y verificar la cobertura de registro antes de ejecutar cambios.

Antes de ejecutar la prueba se comprobarán aislamiento, objetivos propios, sincronización horaria, instantáneas, condiciones de parada y limpieza. El orden de trabajo está en la [lista de implementación](../../docs/implementation-checklist.md). Esta etapa **requiere ejecución manual**.

Durante la investigación se completará la [plantilla de informe](../../templates/incident-report.md), con fragmentos revisados en `evidence/` y su procedencia según las [reglas de manejo de evidencias](../../docs/evidence-handling.md). Las alertas esperadas que no aparezcan se documentarán como brechas de detección.

[Volver al índice de investigaciones](../README.md)
