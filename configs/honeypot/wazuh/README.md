# Cowrie → Wazuh — contrato de integración pendiente

**Estado: NO DATA — DEPLOYMENT PENDING.** No se han inspeccionado eventos del sensor. No se crean decodificadores, XML de reglas, consultas ejecutables ni nombres de campos normalizados supuestos en el entregable 0.5.

## Fuente y campos

La [referencia oficial de eventos Cowrie](https://docs.cowrie.org/en/latest/OUTPUT.html) documenta, entre otros, `eventid`, `timestamp`, `sensor`, `session`, `src_ip`, atributos de conexión como `src_port`, `dst_ip`, `dst_port` y `protocol`, `username` en autenticación e `input` en comandos. Es una referencia de documentación, **no evidencia capturada ni contrato validado para una versión desplegada**. También deben comprobarse atributos, unidades de duración y diferencias entre tipos/versiones.

La siguiente tabla define conceptos requeridos. Cada ruta JSON de origen y campo de destino Wazuh deberá añadirse con un localizador de evidencia real antes de implementar la correspondencia.

| Concepto a preservar | Validación y transformación necesarias |
| --- | --- |
| ID/tipo de evento | Distinguir código de comportamiento, identidad única de registro y ID de regla; no son intercambiables |
| Timestamp | Formato y zona reales; conservar tiempo de evento, recepción e ingestión por separado |
| Sensor | Conservar valor nativo y contrastar identidad del transporte e inventario; añadir época de despliegue como metadato del pipeline |
| IP y puerto de origen | Validar IPv4/IPv6 y tipo numérico; no usar un origen declarado en un comando como origen de conexión |
| IP y puerto de destino | Distinguir listener interno, servicio expuesto y destino solicitado por forwarding o descarga; registrar NAT |
| Protocolo | Separar transporte de red y aplicación SSH/Telnet cuando la fuente lo permita |
| Username | Alias coherente para publicación; registrar ausencias y resultado de autenticación |
| Session ID | Correlacionar con sensor/época; verificar ámbito y sesiones incompletas |
| Command | Preservar orden y contenido privado como texto hostil; redactar credenciales, URL y datos personales para publicación |
| Session duration | Verificar unidad y evento de cierre; si se deriva de tiempos, etiquetar cálculo; una sesión sin cierre tiene duración desconocida |
| Event type normalizado | Definir categorías solo tras inspeccionar tipos nativos y probar su significado |
| Intento de recuperación de archivo | Separar comando solicitado, transferencia registrada y resultado; URL, filename y hash solo si existen, con tratamiento seguro |
| Evidence Origin | Metadato obligatorio de procedencia asignado por el pipeline, no atribuido a Cowrie; excluir pruebas de los agregados de Internet |

Las contraseñas se conservarán solo en almacenamiento privado restringido cuando sean necesarias y durante la retención aprobada. La copia analítica de uso general debe excluirlas; correlaciones sensibles, si se justifican, se calcularán en privado. No publicar contraseñas en bulk, hashes simples reversibles por diccionario ni diccionarios extraídos.

## Ingestión y parsing

El colector local Wazuh leerá JSON aprobado desde una ruta dedicada, después del [transporte e importación](../../../honeypot/telemetry-pipeline.md). Se documentarán framing por registro, permisos, rotación y checkpoint. No habrá agente del VPS conectado directamente al manager privado ni receptor Wazuh abierto a Internet.

La ruta recibirá únicamente la copia analítica minimizada, publicada después de validar el lote completo; los originales con credenciales permanecen en almacenamiento restringido fuera de ese colector. El parser JSON no sustituye esta revisión. Probar que los secretos retirados tampoco reaparezcan en `message`, comandos, `full_log`, archivos de eventos, alertas o exportaciones. Registrar explícitamente qué transformaciones limitan un análisis posterior.

Probar primero el decodificador JSON integrado con eventos reales de la versión seleccionada. Wazuh permite extraer campos JSON; las salidas y limitaciones deben comprobarse antes de decidir si hace falta un decodificador personalizado. [Decodificador JSON oficial](https://documentation.wazuh.com/current/user-manual/ruleset/decoders/json-decoder.html).

Registrar para cada correspondencia: ruta exacta de origen, ejemplo revisado, tipo/unidad, campo de destino observado, transformación, null/ausente, versión y resultado de prueba. Comprobar cómo aparecen IP, tiempos y campos anidados en análisis e indexación; el nombre utilizado por una regla puede diferir de la ruta consultada en el índice. No forzar campos ajenos para que una regla aparente funcionar.

## Eventos, alertas y almacenamiento

Definir una ruta consultable para todos los eventos Cowrie aceptados, con retención y cuota, además de las alertas. El archivo de eventos de Wazuh permite conservar eventos que no producen alertas; requiere habilitación y configuración de indexación apropiadas, no es un panel disponible automáticamente. [Archivo e indexación de eventos Wazuh](https://documentation.wazuh.com/current/user-manual/manager/event-logging.html).

No calcular autenticaciones o sesiones únicamente desde el índice de alertas. Registrar índice/ruta real, filtros de origen/sensor, cobertura, control de acceso, eliminación y costes antes de activar archivo global. Separar el original privado de la copia analítica minimizada y de la evidencia pública; aplicar minimización también a texto duplicado del mensaje original, exportaciones y `full_log` si aparece. No prometer ausencia de contraseñas eliminando un único atributo visible.

## Correlación temporal por lotes

El tiempo Cowrie validado, la recepción del lote y la hora de análisis Wazuh son relojes distintos. La [sintaxis de reglas Wazuh](https://documentation.wazuh.com/current/user-manual/ruleset/ruleset-xml-syntax/rules.html) define controles como `frequency` y `timeframe`; extraer un timestamp no demuestra qué reloj utiliza una correlación de la versión elegida. Esa semántica se comprobará antes de interpretar una alerta como frecuencia observada en Internet.

Las reglas de evento individual pueden clasificar comportamiento tras inspeccionar sus campos. Para SOC-011/SOC-013 y tasas históricas, validar agregaciones sobre tiempo de evento y sensor en el conjunto consultable. Si una regla usa tiempo de procesamiento, no utilizar su agrupación de llegadas como prueba de una ráfaga histórica: respaldar la investigación con una consulta por ventana de observación. El mecanismo de búsqueda/correlación y sus límites se documentarán en HP-3, sin añadir reglas supuestas en 0.5.

La aceptación privada comparará importación inmediata y demorada de la misma muestra real del software, con origen de prueba y conjunto separados. Incluir intentos separados en el tiempo que llegan juntos, una sesión dividida entre lotes, registros fuera de orden y reenvío duplicado. Los recuentos deduplicados y la clasificación sustentada en tiempo de evento deben coincidir; guardar diferencias de alertas como limitaciones del motor. Una llegada tardía puede revisar una ventana anterior: conservar corte de ingestión, versión del resultado y motivo del cambio.

## Detecciones y aceptación

Las hipótesis iniciales son fallos repetidos, aceptación emulada tras intentos, comandos interactivos, comportamiento de credenciales entre varios orígenes y reconocimiento con cobertura de red. Las tasas, ventanas, agrupaciones, niveles y ATT&CK quedan pendientes de evidencia; no se asignan números de técnicas por intuición.

Después de inspeccionar eventos, guardar aquí reglas/decodificadores necesarios sin secretos y enlazar su prueba desde [detections/wazuh](../../../detections/wazuh/README.md). Cada regla tendrá muestra real revisada, origen de prueba, semántica, controles positivos/negativos y de umbral, limitaciones, revisión y resultado de prueba de reglas. Verificar por separado la llegada de alerta al índice y panel. Las reproducciones se excluyen de métricas observadas y no autorizan ataques públicos.

Antes de cerrar HP-3 se comprobarán campos útiles, pérdida/rechazo, reenvío sin doble conteo, orden de sesión, tiempo, eventos sin alerta, privacidad, consulta reproducible y al menos una detección basada en comportamiento realmente disponible. Una alerta esperada ausente se registra como **Detection Gap**.
