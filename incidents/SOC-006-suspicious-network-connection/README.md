# SOC-006 — Conexión de red sospechosa

**Evidence Origin: Controlled Simulation**

**Entorno: Controlled Detection Lab — CONTROLLED TELEMETRY.** Escenario controlado; fuente prevista y aún no recopilada.

**Estado: pendiente de ejecución.** Etapa prevista: 6. Todavía no hay evidencias ni una clasificación del caso.

## Objetivo

Atribuir una conexión a su proceso y usuario, y valorar el destino y el contexto para decidir si es sospechosa.

## Actividad prevista

Enviar una solicitud inocua desde Windows a un servicio temporal en SOC-LINUX; detener el servicio al terminar.

## Evidencias necesarias

**Fuentes:** Eventos de procesos y red de Sysmon, Suricata EVE, Wazuh y registros del servicio local.

Proceso, padre y usuario, equipo, destino, puerto, protocolo, tiempos, correlación entre fuentes y limpieza del servicio.

## Dependencias y siguiente paso

Depende de eventos de red Sysmon y de una captura Suricata validada. El destino será local y controlado.

Antes de ejecutar la prueba se comprobarán aislamiento, objetivos propios, sincronización horaria, instantáneas, condiciones de parada y limpieza. El orden de trabajo está en la [lista de implementación](../../docs/implementation-checklist.md). Esta etapa **requiere ejecución manual**.

Durante la investigación se completará la [plantilla de informe](../../templates/incident-report.md), con fragmentos revisados en `evidence/` y su procedencia según las [reglas de manejo de evidencias](../../docs/evidence-handling.md). Las alertas esperadas que no aparezcan se documentarán como brechas de detección.

[Volver al índice de investigaciones](../README.md)
