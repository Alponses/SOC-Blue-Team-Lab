# SOC-014 — Internet Reconnaissance

**Evidence Origin: Observed Honeypot Telemetry**

**Entorno: Internet Honeypot — OBSERVED INTERNET TELEMETRY.**

**Estado: placeholder; NO DATA — DEPLOYMENT PENDING.** La procedencia indica la fuente requerida; no hay alerta, investigación abierta, evidencia, métricas, clasificación ni decisión existentes. Depende de HP-2/HP-3 y de observar actividad pertinente en HP-4.

## Objetivo

Investigar probing o reconocimiento observado por el sensor público y precisar su cobertura.

## Evidencias necesarias

Origen, destinos observados, puertos, protocolos, frecuencia, temporización, flujos/alertas EVE o firewall/proveedor, interfaz y pérdida de captura, actividad relacionada.

Originales privados; publicar solo extractos revisados con manifiesto y localizadores según [manejo de evidencias](../../docs/evidence-handling.md). No sustituirlos por muestras inventadas ni simulaciones presentadas como Internet.

## Recorrido de investigación pendiente

Alerta → triage → evidencia → enriquecimiento → timeline → ATT&CK → clasificación → decisión.

1. Documentar interfaz y punto de captura, NAT, direcciones del sensor y servicios expuestos antes de interpretar los intentos.
2. Reconstruir patrón de puertos/protocolos, tiempos y repeticiones desde eventos reales; separar conexiones completas, intentos y paquetes descartados si la fuente lo permite.
3. Relacionar con sesiones Cowrie mediante tiempo y tupla de red comprobados. No suponer una identidad común de flujo y sesión.
4. Contrastar escaneo con reintentos, chequeos de salud autorizados o ruido. No atribuir al origen un escaneo global a partir de un único VPS.

## Entrega y decisión

Completar la [plantilla de incidente](../../templates/incident-report.md) con evidencia vinculada, timeline UTC, [enriquecimiento](../../enrichment/README.md) con fuente/fecha/confianza/limitación, comportamiento que respalde ATT&CK, severidad y clasificación justificadas, decisión de cierre o escalamiento, responsable y mejora de detección. No asignar técnicas ni resultado antes del análisis.

**Límites específicos:** Cowrie por sí solo no demuestra reconocimiento de puertos que no observa. Sin cobertura de red suficiente, limitar la conclusión o mantener el caso pendiente; no generar un escaneo público para completarlo.

Observed Internet activity does not imply compromise of a production environment. La reputación y GeoIP no determinan identidad, ubicación física ni responsabilidad.

## Dependencias y siguiente paso

Cumplir [seguridad y despliegue](../../honeypot/deployment-checklist.md), [contrato Wazuh](../../configs/honeypot/wazuh/README.md) y [criterios de red](../../dashboards/network-anomalies/README.md). Esperar telemetría real suficiente y registrar carencias; ninguna actividad pública se ejecuta para completar esta ficha.

[Volver al índice de investigaciones](../README.md)
