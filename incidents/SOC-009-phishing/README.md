# SOC-009 — Investigación de phishing

**Estado: pendiente de ejecución.** Etapa prevista: 9. Todavía no hay evidencias ni una clasificación del caso.

## Objetivo

Evaluar un correo y justificar una conclusión a partir de sus encabezados, contenido, enlaces y adjuntos.

## Actividad prevista

Analizar un correo sintético identificado como tal o una muestra segura de entrenamiento, sin visitar infraestructura maliciosa.

## Evidencias necesarias

**Fuentes:** Encabezados y contenido del correo, metadatos de adjuntos, análisis local y enriquecimiento permitido.

Resumen ejecutivo, From, Reply-To, Return-Path, Received, límites de confianza de SPF/DKIM/DMARC, URL no navegables, dominios, hashes, metadatos, tabla de IOC, línea de tiempo, conclusión y acciones.

## Dependencias y siguiente paso

La procedencia de la muestra debe quedar documentada. Los resultados de reputación solo se incluirán si se obtienen; los encabezados sintéticos no prueban autenticación real.

Antes de ejecutar la prueba se comprobarán aislamiento, objetivos propios, sincronización horaria, instantáneas, condiciones de parada y limpieza. El orden de trabajo está en la [lista de implementación](../../docs/implementation-checklist.md). Esta etapa **requiere ejecución manual**.

Durante la investigación se completará la [plantilla de informe](../../templates/incident-report.md), con fragmentos revisados en `evidence/` y su procedencia según las [reglas de manejo de evidencias](../../docs/evidence-handling.md). Las alertas esperadas que no aparezcan se documentarán como brechas de detección.

[Volver al índice de investigaciones](../README.md)
