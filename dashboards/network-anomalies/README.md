# Network Anomalies — red y posibles anomalías DoS

**Estado: NO DATA — DEPLOYMENT PENDING.** No existe baseline ni detección volumétrica validada. Este diseño distingue ruido habitual, reconocimiento, credenciales y posibles interrupciones del servicio.

## Telemetría requerida

| Métrica | Fuente prevista y cálculo | Limitación |
| --- | --- | --- |
| Packets per second | Diferencia de contadores de interfaz/captura dividida por segundos medidos, separando entrada y salida | Detectar reinicios/wrap; EVE al cierre de flujo no proporciona PPS instantáneos |
| Bytes per second | Delta de bytes de interfaz o proveedor / tiempo | Diferencias por encapsulado, muestreo y punto de captura |
| Connections per second | Nuevas conexiones observadas por intervalo, con intento y establecimiento separados | No equivale a eventos Cowrie; requiere estado TCP o fuente equivalente |
| Requests per second | Solicitudes de aplicación del protocolo realmente instrumentado / tiempo | SSH usa intentos/comandos etiquetados; no llamarlos HTTP requests |
| Unique sources per interval | Cardinalidad por intervalo de IP válidas en la fuente seleccionada | Spoofing en tráfico sin conexión completada y NAT limitan interpretación |
| TCP SYN rate | SYN iniciales por segundo desde captura/contadores apropiados, política explícita para retransmisiones | No inferirlo del número de inicios de sesión |
| TCP state distribution | Estados y transiciones de host/captura, con instante de medición y duración | EVE y sistema operativo pueden ofrecer perspectivas distintas |
| Destination ports / protocol distribution | Paquetes, flujos o conexiones por puerto/protocolo; selector de unidad | No sumar unidades distintas; reconocer NAT |
| HTTP status codes | Logs HTTP o metadatos EVE si el tráfico es visible | No aplicable al Cowrie SSH/Telnet inicial; no abrir HTTP solo para llenar un panel |
| Source ASN / geographic distribution | Enriquecimiento de IP observadas con versión y desconocidos | Contexto estimado, no prueba de coordinación ni identidad |
| Historical baseline | Intervalos comparables de tasas, recursos y disponibilidad | No existe todavía; excluir lagunas, mantenimiento, replays y cambios de configuración |
| Salud e impacto | CPU, RAM, disco, cola, pérdida de captura, ancho de banda, disponibilidad/latencia del servicio y avisos del proveedor | Necesarios para separar saturación real, fallo de sensor y retraso del pipeline |

La [evaluación Suricata](../../honeypot/suricata-visibility.md) define el punto de captura. Si falta una fuente, mostrar «no disponible» y su efecto sobre la conclusión; no deducir todas las tasas a partir de JSON de Cowrie.

## Baseline y visualización

Registrar tasas en intervalos fijos con zona UTC, sensor/época y cobertura, conservar denominador en segundos y volumen de muestra. Propuesta de análisis: comparar intervalos de un minuto con su contexto horario y el historial disponible; resolución de captura y periodo mínimo válido se decidirán según recursos y variabilidad, no como umbral de ataque universal.

Mostrar mediana, percentiles y rango histórico por servicio/día/hora cuando haya suficientes intervalos comparables. Documentar duración, cobertura, exclusiones y cambios de configuración. Si el baseline es insuficiente, la conclusión será provisional. No convertir pausas de ingestión en ceros ni un lote atrasado en pico de tráfico: usar tiempo de evento/medición.

La vista combinará tasas y bandas históricas, composición por servicio/red, estados TCP, pérdida de captura y salud del servicio. La línea de tiempo marcará cambios de firewall, mantenimiento, interrupciones, avisos upstream e inicio de una investigación. Un clic llevará a evidencia y a [SOC-015](../../incidents/SOC-015-network-traffic-anomaly/README.md).

## Clasificación basada en evidencia

Estas categorías describen actividad; son independientes de True/False/Benign Positive e Inconclusive del informe de incidente. Registrar hipótesis alternativas, confianza y decisión.

| Categoría | Evidencia mínima para sostenerla |
| --- | --- |
| Internet Noise | Actividad de fondo observada, contexto y ausencia de señales suficientes de otra categoría; no implica benignidad de todos los intentos |
| Reconnaissance | Probing de servicios/protocolos y secuencia visible que respalde exploración |
| Port Scan | Intentos a distintos puertos/objetivos observados, con tiempos y cobertura; Cowrie solo en SSH no demuestra escaneo multipuerto |
| Credential Brute Force | Intentos repetidos de autenticación con cuentas, resultados, intervalo y deduplicación comprobados |
| Distributed Brute Force | Conducta de credenciales similar desde múltiples IP, con similitudes y límites de coordinación documentados; no basta contar IP |
| Traffic Spike | Aumento medido frente a baseline comparable, sin atribuir mecanismo ni intención automáticamente |
| Suspected DoS | Patrón de tráfico compatible y evidencia de presión/degradación del recurso o aviso upstream; faltan pruebas para confirmar causa/distribución |
| Confirmed DDoS | Evidencia de red/aplicación adecuada que demuestre distribución, mecanismo y efecto de denegación, o confirmación explícita del proveedor de seguridad upstream con alcance/tiempos documentados. Si fue mitigado antes del host, registrar ese resultado sin inventar caída local |

Un alto número de eventos o muchas IP no prueba DDoS. Considerar escaneo, brute force, retransmisiones, cambios de log, lotes atrasados, errores de parsing y pérdida de sensor. Si no hay datos suficientes, conservar clasificación no concluyente; no forzar el caso a «Confirmed DDoS».

Nunca generar un DDoS público. Cualquier carga de validación quedará acotada, autorizada y en una réplica privada, sin objetivos públicos. Hasta contar con pruebas, no publicar umbrales de detección como validados.

> Geographic information represents the estimated location of the observed source IP address and does not establish the physical location or identity of an attacker.
