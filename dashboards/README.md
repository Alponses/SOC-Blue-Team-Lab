# Especificaciones de paneles SOC

**Estado: diseño documental. NO DATA — DEPLOYMENT PENDING.** No hay dashboards desplegados, objetos de importación, capturas ni estadísticas de ataques.

| Panel | Pregunta que resolverá |
| --- | --- |
| [Global Honeypot Activity](attack-map/README.md) | ¿Qué orígenes de red se observaron y qué contexto geográfico estimado tienen? |
| [SOC Overview](soc-overview/README.md) | ¿Qué actividad, sesiones y detecciones necesitan atención? |
| [Network Anomalies](network-anomalies/README.md) | ¿La variación de tráfico es ruido, reconocimiento, credenciales o una anomalía con impacto? |

## Convenciones comunes

Cada vista mostrará origen de evidencia, sensor/época, intervalo UTC, última recepción, retraso de importación, uptime/cobertura y filtros activos. Separar `CONTROLLED TELEMETRY` de `OBSERVED INTERNET TELEMETRY`; ningún total combinará ambos sin segmentación explícita. Las pruebas del operador y reproducciones quedarán fuera de las métricas de Internet.

Utilizar tiempo del evento y ventana semiabierta inicio incluido/fin excluido, con deduplicación del [pipeline](../honeypot/telemetry-pipeline.md). Diferenciar eventos, intentos, sesiones y alertas; los datos ausentes no son cero. Antes del despliegue todos los indicadores tendrán `NO DATA — DEPLOYMENT PENDING`; después se distinguirán cero confirmado, campo no disponible, sensor sin conexión y datos retrasados/incompletos.

Registrar también el corte de ingestión de la consulta. Cuando llegue un lote tardío, recalcular la ventana afectada y señalar la revisión; no añadir su actividad al periodo actual por su hora de importación. Las alertas por umbral deberán cumplir la [validación temporal Wazuh](../configs/honeypot/wazuh/README.md#correlación-temporal-por-lotes) antes de interpretarse como ráfagas de autenticación o tráfico.

El contrato de campos y los índices reales se resolverán en [Wazuh](../configs/honeypot/wazuh/README.md) con eventos inspeccionados. Los nombres de métricas de estas especificaciones son conceptos de análisis, no campos inventados. Cada visualización tendrá consulta versionada, denominador, agrupación, tratamiento de null, evidencia de reconciliación y enlace a casos pertinentes.

Las vistas operativas permanecerán privadas. Exportar solo agregados o fragmentos revisados; no mostrar contraseñas, URL activas, transcripciones completas ni direcciones de infraestructura propia. Si el mapa necesita teselas externas, evaluar metadatos compartidos y preferir recursos locales; no enviar IP o sesiones a un servicio de mapas automáticamente.

GeoIP no es atribución. Texto obligatorio en cualquier panel con geografía:

> Geographic information represents the estimated location of the observed source IP address and does not establish the physical location or identity of an attacker.
