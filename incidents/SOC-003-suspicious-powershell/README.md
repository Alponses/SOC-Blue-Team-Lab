# SOC-003 — Ejecución sospechosa de PowerShell

**Estado: pendiente de ejecución.** Etapa prevista: 5. Todavía no hay evidencias ni una clasificación del caso.

## Objetivo

Relacionar una ejecución de PowerShell con su proceso padre, usuario y efectos observados para evaluar si requiere escalamiento.

## Actividad prevista

Ejecutar una simulación inocua con un patrón que permita practicar la investigación, sin malware.

## Evidencias necesarias

**Fuentes:** Sysmon Operational, PowerShell Operational y Wazuh.

Proceso y padre, línea de comandos, contenido del script, usuario, equipo, hora, identificadores de correlación y conexiones solo si se observan.

## Dependencias y siguiente paso

Depende de los filtros de Sysmon y las políticas de registro de PowerShell definidos y comprobados en la etapa 1.

Antes de ejecutar la prueba se comprobarán aislamiento, objetivos propios, sincronización horaria, instantáneas, condiciones de parada y limpieza. El orden de trabajo está en la [lista de implementación](../../docs/implementation-checklist.md). Esta etapa **requiere ejecución manual**.

Durante la investigación se completará la [plantilla de informe](../../templates/incident-report.md), con fragmentos revisados en `evidence/` y su procedencia según las [reglas de manejo de evidencias](../../docs/evidence-handling.md). Las alertas esperadas que no aparezcan se documentarán como brechas de detección.

[Volver al índice de investigaciones](../README.md)
