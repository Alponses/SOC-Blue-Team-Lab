# SOC-015 — Network Traffic Anomaly

**Evidence Origin: Observed Honeypot Telemetry**

**Entorno: Internet Honeypot — OBSERVED INTERNET TELEMETRY.**

**Estado: placeholder; NO DATA — DEPLOYMENT PENDING.** La procedencia indica la fuente requerida; no hay alerta, investigación abierta, evidencia, métricas, clasificación ni decisión existentes. Depende de HP-2/HP-3 y de observar actividad pertinente en HP-4.

## Objetivo

Investigar un pico real frente a baseline y decidir qué clasificación sostienen tasas, distribución e impacto.

## Evidencias necesarias

PPS, CPS, solicitudes por segundo cuando aplique, bytes por segundo, fuentes únicas, SYN/estados TCP, puertos/protocolos, ASN/GeoIP, baseline, salud del servicio, pérdida y evidencia upstream disponible.

Originales privados; publicar solo extractos revisados con manifiesto y localizadores según [manejo de evidencias](../../docs/evidence-handling.md). No sustituirlos por muestras inventadas ni simulaciones presentadas como Internet.

## Recorrido de investigación pendiente

Alerta → triage → evidencia → enriquecimiento → timeline → ATT&CK → clasificación → decisión.

1. Verificar ventana de medición, unidades, tiempo de evento, reinicios de contadores y ausencia de duplicados; descartar picos causados por importación atrasada.
2. Comparar tasas con historia de cobertura equivalente; registrar periodo y suficiencia del baseline, mantenimiento, cambios de configuración y datos ausentes.
3. Relacionar fuentes, protocolos y puertos con recursos, pérdida de captura y disponibilidad del servicio; contrastar ruido, escaneo, brute force y actividad distribuida.
4. Comparar Internet Noise, Reconnaissance, Port Scan, Credential Brute Force, Distributed Brute Force, Traffic Spike, Suspected DoS y Confirmed DDoS con los criterios del panel Network Anomalies. Registrar actividad volumétrica sospechosa como hipótesis si falta evidencia y mantener no concluyente cuando corresponda.
5. Para Confirmed DDoS exigir evidencia adecuada de distribución, mecanismo y denegación, o confirmación explícita del proveedor de seguridad upstream; documentar mitigación y no inventar impacto local.

## Entrega y decisión

Completar la [plantilla de incidente](../../templates/incident-report.md) con evidencia vinculada, timeline UTC, [enriquecimiento](../../enrichment/README.md) con fuente/fecha/confianza/limitación, comportamiento que respalde ATT&CK, severidad y clasificación justificadas, decisión de cierre o escalamiento, responsable y mejora de detección. No asignar técnicas ni resultado antes del análisis.

**Límites específicos:** Un conteo alto de eventos no prueba DoS/DDoS. Sin baseline o telemetría de red, declarar la limitación; nunca generar DDoS público ni hacer carga contra infraestructura pública para crear el caso.

Observed Internet activity does not imply compromise of a production environment. La reputación y GeoIP no determinan identidad, ubicación física ni responsabilidad.

## Dependencias y siguiente paso

Cumplir [seguridad y despliegue](../../honeypot/deployment-checklist.md), [contrato Wazuh](../../configs/honeypot/wazuh/README.md) y [criterios de red](../../dashboards/network-anomalies/README.md). Esperar telemetría real suficiente y registrar carencias; ninguna actividad pública se ejecuta para completar esta ficha.

[Volver al índice de investigaciones](../README.md)
