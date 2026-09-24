# SOC-008 — Integridad de archivos

**Evidence Origin: Controlled Simulation**

**Entorno: Controlled Detection Lab — CONTROLLED TELEMETRY.** Escenario controlado; fuente prevista y aún no recopilada.

**Estado: pendiente de ejecución.** Etapa prevista: 8. Todavía no hay evidencias ni una clasificación del caso.

## Objetivo

Determinar qué cambió en un archivo supervisado, cuándo ocurrió y quién lo modificó si la auditoría permite demostrarlo.

## Actividad prevista

Modificar y restaurar un archivo o directorio de prueba protegido y sin información sensible.

## Evidencias necesarias

**Fuentes:** Wazuh FIM, estado de referencia del archivo y auditoría o who-data cuando sean compatibles.

Ruta, equipo, hora, estado o hash anterior y posterior, actor con evidencia, autorización y restauración verificada.

## Dependencias y siguiente paso

Requiere una referencia previa de FIM. La atribución del actor se comprobará por separado; un cambio de hash no identifica a la persona o proceso responsable.

Antes de ejecutar la prueba se comprobarán aislamiento, objetivos propios, sincronización horaria, instantáneas, condiciones de parada y limpieza. El orden de trabajo está en la [lista de implementación](../../docs/implementation-checklist.md). Esta etapa **requiere ejecución manual**.

Durante la investigación se completará la [plantilla de informe](../../templates/incident-report.md), con fragmentos revisados en `evidence/` y su procedencia según las [reglas de manejo de evidencias](../../docs/evidence-handling.md). Las alertas esperadas que no aparezcan se documentarán como brechas de detección.

[Volver al índice de investigaciones](../README.md)
