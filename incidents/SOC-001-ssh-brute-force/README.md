# SOC-001 — Fuerza bruta SSH

**Estado: pendiente de ejecución.** Etapa prevista: 3. Todavía no hay evidencias ni una clasificación del caso.

## Objetivo

Determinar si una serie de fallos SSH corresponde a un intento de fuerza bruta y comprobar si después hubo un acceso exitoso.

## Actividad prevista

Generar un número limitado de fallos desde SOC-SIM hacia SOC-LINUX con una cuenta de prueba.

## Evidencias necesarias

**Fuentes:** Registros SSH y de autenticación; eventos y alertas de Wazuh.

IP de origen, cuenta objetivo, número de intentos únicos, tiempos, posibles accesos exitosos posteriores e identificadores de alertas y reglas.

## Dependencias y siguiente paso

Depende de la recopilación Linux del entregable 2 y de preparar el simulador con límites de intentos y una política de bloqueo conocida.

Antes de ejecutar la prueba se comprobarán aislamiento, objetivos propios, sincronización horaria, instantáneas, condiciones de parada y limpieza. El orden de trabajo está en la [lista de implementación](../../docs/implementation-checklist.md). Esta etapa **requiere ejecución manual**.

Durante la investigación se completará la [plantilla de informe](../../templates/incident-report.md), con fragmentos revisados en `evidence/` y su procedencia según las [reglas de manejo de evidencias](../../docs/evidence-handling.md). Las alertas esperadas que no aparezcan se documentarán como brechas de detección.

[Volver al índice de investigaciones](../README.md)
