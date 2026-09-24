# SOC-004 — Cambios de cuentas y privilegios

**Estado: pendiente de ejecución.** Etapa prevista: 7. Todavía no hay evidencias ni una clasificación del caso.

## Objetivo

Identificar quién modificó una cuenta o sus privilegios y comprobar si el cambio estaba autorizado.

## Actividad prevista

Crear una identidad de prueba, cambiar su pertenencia a un grupo o elevar sus privilegios y restaurar el estado al terminar.

## Evidencias necesarias

**Fuentes:** Eventos Security del equipo o controlador de dominio, estado de las identidades y Wazuh.

Actor, cuenta afectada, grupo o privilegio anterior y posterior, equipo, hora, autorización y comprobación de limpieza.

## Dependencias y siguiente paso

La variante de dominio requiere Active Directory, políticas de auditoría y usuarios de prueba de la etapa 7.

Antes de ejecutar la prueba se comprobarán aislamiento, objetivos propios, sincronización horaria, instantáneas, condiciones de parada y limpieza. El orden de trabajo está en la [lista de implementación](../../docs/implementation-checklist.md). Esta etapa **requiere ejecución manual**.

Durante la investigación se completará la [plantilla de informe](../../templates/incident-report.md), con fragmentos revisados en `evidence/` y su procedencia según las [reglas de manejo de evidencias](../../docs/evidence-handling.md). Las alertas esperadas que no aparezcan se documentarán como brechas de detección.

[Volver al índice de investigaciones](../README.md)
