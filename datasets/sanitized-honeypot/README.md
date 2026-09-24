# Evidencia sanitizada de honeypot

**Estado: NO DATA — DEPLOYMENT PENDING.** No hay datasets, sesiones, payloads ni muestras de entrenamiento añadidas en el entregable 0.5.

Este directorio contendrá únicamente extractos mínimos de telemetría real revisada y su manifiesto. Los originales quedan fuera del repositorio en almacenamiento privado con acceso y retención definidos. No usarlo como destino de logs Cowrie/EVE, cola de transporte, descargas o exportaciones completas.

## Manifiesto requerido por extracto

| Dato | Contenido a registrar al recopilar evidencia |
| --- | --- |
| Evidence Origin | Observed Honeypot Telemetry; si se usa una muestra de prueba, declararlo explícitamente y mantenerla fuera del conjunto observado |
| Sensor, época y software | Alias, versión, configuración y fuente real |
| Observation window | Intervalo UTC, zona original, desfase y cobertura |
| Procedencia y selección | Método/consulta, lote y localizadores privados, criterio de selección y recuentos de registros |
| Transformaciones | Campos eliminados, alias, fechas desplazadas, URL neutralizadas, restricciones de correlación y enriquecimiento previo |
| Integridad | Nombre del extracto y SHA-256 calculado después de sanitizar; hash/original privado por separado |
| Revisión | Fecha, alias del revisor, clasificación de datos y limitaciones de publicación |
| Investigación relacionada | Enlace al caso o informe que usa la evidencia |

Revisar campos y duplicados de texto completo, credenciales, usuarios, comandos, rutas, filenames, URL, query strings, payload indicators, tokens, identificadores personales e infraestructura origen/destino. Sustituir valores por alias coherentes; no publicar passwords en bulk ni hashes de contraseñas. Si un análisis necesita comparar credenciales, hacerlo en privado y publicar solo una conclusión sustentada con agregados o alias no reversibles.

Neutralizar esquemas/dominios de URL sospechosas como texto y retirar parámetros sensibles; nunca enlaces Markdown navegables. Ningún archivo malicioso, ejecutable o PCAP completo se publica sin la revisión explícita aplicable; los binarios maliciosos quedan excluidos siempre. No hay descargas ni ejecución de payloads como parte del análisis.

Los extractos seleccionados **no representan todo el tráfico**. Los informes calcularán métricas en el conjunto privado con consulta reproducible y registrarán cuánto puede verificar el lector con el extracto. Si se sustituyen IP, preservar ASN/GeoIP solo como enriquecimiento previo documentado; no geolocalizar alias. Seguir [manejo de evidencias](../../docs/evidence-handling.md) y [enriquecimiento](../../enrichment/README.md).
