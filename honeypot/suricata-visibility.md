# Suricata en el entorno público

**Estado: evaluación de arquitectura; instalación y captura pendientes.** El diseño existente de Suricata en SOC-LINUX conserva su función prevista en las simulaciones y no cubre el VPS remoto.

## Punto de observación propuesto

Evaluar Suricata pasivo en la interfaz pública del VPS, solo si el proveedor y el sistema permiten captura y hay CPU/memoria suficientes. Registrar nombre real de interfaz, direcciones, MTU, direcciones de captura, NAT/redirecciones y runtime de Cowrie. No se asigna `eth0` por suposición. Si no es viable, evaluar un punto de observación del proveedor que reciba una copia verificable del tráfico; sin ese punto, declarar la carencia.

| Punto | Cobertura esperada que debe comprobarse | Fuera de cobertura |
| --- | --- | --- |
| Interfaz pública del VPS | Paquetes que llegan/salen de esa interfaz, puertos observados y metadatos disponibles | Tráfico bloqueado antes por el proveedor, otros VPS, toda la Internet o la LAN del analista |
| Interfaz interna o del runtime | Tráfico que realmente la atraviesa; puertos posiblemente posteriores a redirección | Puerto público original si no se conserva, tráfico descartado antes de esa interfaz |
| Registros del proveedor | Flujos, contadores o mitigación según producto y permisos | Comandos dentro de SSH y detalle no incluido en su exportación |

La captura antes/después del cortafuegos depende de la ubicación y del mecanismo utilizado; debe verificarse. Evitar sumar la misma comunicación capturada en dos interfaces. Registrar pérdida de paquetes, muestreo, pausas y contadores reiniciados; no extrapolar a tráfico que nunca llegó al sensor.

## Salidas y correlación previstas

EVE puede ofrecer alertas, flujos y metadatos de protocolos según la configuración. Se seleccionarán tipos concretos y se comprobarán con la versión instalada; `latest` puede ser una rama de desarrollo. [Documentación oficial EVE JSON](https://docs.suricata.io/en/latest/output/eve/eve-json-output.html).

| Salida o fuente | Uso previsto | Límite |
| --- | --- | --- |
| EVE alertas | Firma, revisión, severidad, flujo y evidencia que disparó la regla | Una alerta aislada no prueba impacto ni compromiso |
| EVE flujos | Direcciones, puertos, protocolo, inicio/fin, bytes y paquetes disponibles | Los registros al cierre/timeout no equivalen a PPS instantáneos |
| EVE DNS | Consulta/respuesta visible y código cuando exista | DNS cifrado o ausente no aporta esos campos |
| EVE HTTP/TLS | Método/estado HTTP o metadatos TLS, SNI/certificado cuando sean visibles | No descifra SSH/TLS; no se prometen comandos, URL completas ni códigos HTTP cifrados |
| Estadísticas de captura y host | Pérdida, paquetes/bytes, recursos y disponibilidad | Dependen de intervalo, reinicios y ubicación del contador |
| Métricas TCP del host y proveedor | SYN, estados, conexiones y evidencia de saturación | Requieren fuentes adicionales verificadas; Cowrie no las sustituye |

Cowrie registra interacción dentro de su servicio SSH; Suricata verá la conexión cifrada y sus metadatos, no esa shell. Correlacionar mediante sensor/época, tiempo, protocolo y tupla de red validada, anotando NAT y desfase. No presumir que el identificador de flujo EVE sea el identificador de sesión Cowrie.

Antes del despliegue, comprobar cobertura en una réplica privada con flujos inocuos conocidos y comparar eventos/paquetes. Reservar configuración futura del sensor público bajo `configs/honeypot/`; conservar la de SOC-LINUX en `configs/suricata/`. EVE público viajará por el mismo [límite de datos](telemetry-pipeline.md), con procedencia y fuente separadas.

El [panel de anomalías](../dashboards/network-anomalies/README.md) requiere contadores y estado del servicio además de logs de aplicación. No se publicarán PCAP completos sin revisión explícita ni se realizarán ataques de carga contra infraestructura pública.
