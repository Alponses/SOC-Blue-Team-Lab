# SOC-002 — Fallos de autenticación en Windows

**Estado: pendiente de ejecución.** Etapa prevista: 4. Todavía no hay evidencias ni una clasificación del caso.

## Objetivo

Reconstruir los intentos fallidos de acceso y distinguir su origen, tipo de autenticación y resultado.

## Actividad prevista

Provocar fallos controlados en Windows respetando los límites de bloqueo de la cuenta.

## Evidencias necesarias

**Fuentes:** Registros Windows Security y eventos de Wazuh.

ID reales de eventos, cuenta, tipo de inicio de sesión, estado y subestado, origen cuando esté disponible y línea de tiempo.

## Dependencias y siguiente paso

Requiere telemetría Windows validada. El informe indicará si los intentos son locales o de dominio.

Antes de ejecutar la prueba se comprobarán aislamiento, objetivos propios, sincronización horaria, instantáneas, condiciones de parada y limpieza. El orden de trabajo está en la [lista de implementación](../../docs/implementation-checklist.md). Esta etapa **requiere ejecución manual**.

Durante la investigación se completará la [plantilla de informe](../../templates/incident-report.md), con fragmentos revisados en `evidence/` y su procedencia según las [reglas de manejo de evidencias](../../docs/evidence-handling.md). Las alertas esperadas que no aparezcan se documentarán como brechas de detección.

[Volver al índice de investigaciones](../README.md)
