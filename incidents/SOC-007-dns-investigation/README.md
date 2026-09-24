# SOC-007 — Investigación DNS

**Evidence Origin: Controlled Simulation**

**Entorno: Controlled Detection Lab — CONTROLLED TELEMETRY.** Escenario controlado; fuente prevista y aún no recopilada.

**Estado: pendiente de ejecución.** Etapa prevista: 6; 7 si depende de AD DNS. Todavía no hay evidencias ni una clasificación del caso.

## Objetivo

Relacionar una consulta DNS con el equipo solicitante, su respuesta y el proceso cuando esté disponible.

## Actividad prevista

Consultar nombres reservados de prueba a través de un resolvedor local controlado.

## Evidencias necesarias

**Fuentes:** Sysmon DNS, registros del servidor DNS o capturas en la ruta de la consulta, y Wazuh.

Nombre solicitado, equipo, proceso disponible, respuesta y código de resultado, línea de tiempo y método de enriquecimiento con consultas no realizadas identificadas.

## Dependencias y siguiente paso

Necesita un resolvedor local; si no existe en la etapa 6, se completará con AD DNS en la 7. Suricata en Ubuntu no ve automáticamente el tráfico entre Windows y el controlador.

Antes de ejecutar la prueba se comprobarán aislamiento, objetivos propios, sincronización horaria, instantáneas, condiciones de parada y limpieza. El orden de trabajo está en la [lista de implementación](../../docs/implementation-checklist.md). Esta etapa **requiere ejecución manual**.

Durante la investigación se completará la [plantilla de informe](../../templates/incident-report.md), con fragmentos revisados en `evidence/` y su procedencia según las [reglas de manejo de evidencias](../../docs/evidence-handling.md). Las alertas esperadas que no aparezcan se documentarán como brechas de detección.

[Volver al índice de investigaciones](../README.md)
