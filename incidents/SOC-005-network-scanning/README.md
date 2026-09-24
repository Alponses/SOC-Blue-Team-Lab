# SOC-005 — Escaneo de red

**Estado: pendiente de ejecución.** Etapa prevista: 6. Todavía no hay evidencias ni una clasificación del caso.

## Objetivo

Explicar por qué el patrón de tráfico observado corresponde a un escaneo y diferenciarlo de actividad de inventario autorizada.

## Actividad prevista

Realizar un escaneo acotado desde SOC-SIM únicamente hacia SOC-LINUX y los puertos definidos para la prueba.

## Evidencias necesarias

**Fuentes:** Suricata EVE, Wazuh e inspección privada de paquetes cuando aporte contexto.

Visibilidad de la interfaz, origen y destino, protocolos, puertos distintos, intervalos, alertas y reglas si se activan, y explicaciones alternativas.

## Dependencias y siguiente paso

Requiere Suricata y recopilación EVE validadas en la interfaz que recibe el tráfico. No se presupone una alerta de las reglas predeterminadas.

Antes de ejecutar la prueba se comprobarán aislamiento, objetivos propios, sincronización horaria, instantáneas, condiciones de parada y limpieza. El orden de trabajo está en la [lista de implementación](../../docs/implementation-checklist.md). Esta etapa **requiere ejecución manual**.

Durante la investigación se completará la [plantilla de informe](../../templates/incident-report.md), con fragmentos revisados en `evidence/` y su procedencia según las [reglas de manejo de evidencias](../../docs/evidence-handling.md). Las alertas esperadas que no aparezcan se documentarán como brechas de detección.

[Volver al índice de investigaciones](../README.md)
