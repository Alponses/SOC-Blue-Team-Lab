# SOC-012 — Interactive Honeypot Session

**Evidence Origin: Observed Honeypot Telemetry**

**Entorno: Internet Honeypot — OBSERVED INTERNET TELEMETRY.**

**Estado: placeholder; NO DATA — DEPLOYMENT PENDING.** La procedencia indica la fuente requerida; no hay alerta, investigación abierta, evidencia, métricas, clasificación ni decisión existentes. Depende de HP-2/HP-3 y de observar actividad pertinente en HP-4.

## Objetivo

Reconstruir una sesión Cowrie real con comandos y evaluar el comportamiento registrado y sus límites.

## Evidencias necesarias

Inicio de sesión, autenticación, identificador y sensor, comandos en orden, intentos de descarga, indicadores de red, resultados registrados, cierre y duración cuando estén disponibles.

Originales privados; publicar solo extractos revisados con manifiesto y localizadores según [manejo de evidencias](../../docs/evidence-handling.md). No sustituirlos por muestras inventadas ni simulaciones presentadas como Internet.

## Recorrido de investigación pendiente

Alerta → triage → evidencia → enriquecimiento → timeline → ATT&CK → clasificación → decisión.

1. Seleccionar una sesión observada con actividad interactiva y verificar sus eventos de conexión/autenticación; conservar sensor y época para evitar cruces de sesión.
2. Ordenar comandos y respuestas disponibles; distinguir intención expresada, respuesta emulada y efectos que no se pueden demostrar en el host.
3. Examinar intentos de recuperación de archivos y destinos como texto. Diferenciar intento, transferencia fallida y archivo realmente recibido; no ejecutar payloads ni visitar URL.
4. Si hay hash o URL, revisar confidencialidad y realizar solo enriquecimiento seguro opcional. Registrar cierre/duración o sesión incompleta sin inventar un final.

## Entrega y decisión

Completar la [plantilla de incidente](../../templates/incident-report.md) con evidencia vinculada, timeline UTC, [enriquecimiento](../../enrichment/README.md) con fuente/fecha/confianza/limitación, comportamiento que respalde ATT&CK, severidad y clasificación justificadas, decisión de cierre o escalamiento, responsable y mejora de detección. No asignar técnicas ni resultado antes del análisis.

**Límites específicos:** Una secuencia interactiva puede provenir de automatización. No prueba presencia humana, ejecución en el host ni éxito de una descarga. La política inicial bloquea recuperaciones salientes.

Observed Internet activity does not imply compromise of a production environment. La reputación y GeoIP no determinan identidad, ubicación física ni responsabilidad.

## Dependencias y siguiente paso

Cumplir [seguridad y despliegue](../../honeypot/deployment-checklist.md), [contrato Wazuh](../../configs/honeypot/wazuh/README.md) y [criterios de red](../../dashboards/network-anomalies/README.md). Esperar telemetría real suficiente y registrar carencias; ninguna actividad pública se ejecuta para completar esta ficha.

[Volver al índice de investigaciones](../README.md)
