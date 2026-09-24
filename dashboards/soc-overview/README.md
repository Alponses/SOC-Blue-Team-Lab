# SOC Overview

**Estado de todos los indicadores: NO DATA — DEPLOYMENT PENDING.** Diseño orientado a triage, actividad y calidad de datos; no hay métricas observadas todavía.

La vista inicial seleccionará `OBSERVED INTERNET TELEMETRY`. Una vista separada permitirá el laboratorio controlado, con su origen visible y sin mezclar ensayos. Aplicar las [convenciones comunes](../README.md).

## Métricas y definiciones

| Métrica | Unidad y método previsto |
| --- | --- |
| Total events | Registros Cowrie únicos aceptados en la ventana; telemetría de host/EVE en series separadas para evitar doble conteo de actividad |
| Unique source IPs | Cardinalidad de IP de conexión válidas; si el motor aproxima cardinalidad, indicarlo y verificar recuentos exactos para el informe |
| Unique ASNs | ASN distintos conocidos asociados a fuentes; «desconocido» separado |
| Countries observed | Países estimados distintos, sin sumar desconocidos como país |
| Authentication attempts | Eventos de autenticación únicos con resultado comprobado; desglose fallo/aceptación/desconocido, sin contar conexiones como intentos |
| Successful honeypot sessions | Sesiones distintas con autenticación aceptada por la emulación; no significa compromiso del host ni interacción humana |
| Interactive sessions | Sesiones con comandos/input registrados; separar sesiones autenticadas sin actividad posterior |
| Commands observed | Entradas de comandos únicas registradas y sesiones que las contienen; distinguir solicitudes, respuestas emuladas y efectos reales no demostrados |
| Events over time | Eventos deduplicados por intervalo UTC configurable; marcar lagunas, mantenimiento y demora de importación |
| Protocols / destination ports | Distribución por aplicación y puerto expuesto verificado; transporte de red y puertos internos separados |
| Usernames attempted | Frecuencia por usuario revisado/alias; nunca contraseñas ni listas masivas de credenciales |
| Top source networks | Recuento por ASN y red/proveedor con origen y fecha del enriquecimiento; incluir desconocidos |
| Alerts by severity | Alertas únicas por regla/revisión y nivel Wazuh; severidad analítica del caso en dimensión distinta |
| MITRE ATT&CK | Técnicas asociadas solo a detecciones validadas y enlazadas a comportamiento/evidencia; pendientes fuera del recuento |

## Distribución de la vista

Cabecera con ventana UTC, origen, sensor, última ingestión y estado de salud. Primera fila de métricas de volumen y fuentes; después series temporales y autenticaciones. Tablas de protocolos, puertos, usuarios revisados y redes permitirán filtrar sesiones. La cola de alertas mostrará severidad, regla, evidencia y estado del caso para decidir investigar, cerrar o escalar.

Las sesiones incompletas se marcarán como tales; no asignar duración cero ni éxito por ausencia de fallos. Mostrar también retraso, rechazos de parsing, duplicados y cobertura para distinguir falta de telemetría de quietud. Los objetivos de latencia y umbrales dependen del modo por lotes y se fijarán antes de operar.

## Validación futura

Reconciliar intentos/sesiones con registros reales y controles de ingestión; comprobar que una reproducción no incrementa métricas de observación y que una caída se visualiza como dato ausente. Comparar agregados con la consulta del [informe semanal](../../reports/templates/weekly-honeypot-threat-report.md). Las alertas no se usarán como sustituto del conjunto completo de eventos.

Cuando aparezcan países o geografía, mostrar:

> Geographic information represents the estimated location of the observed source IP address and does not establish the physical location or identity of an attacker.
