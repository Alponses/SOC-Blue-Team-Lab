# Frontera de confianza del honeypot

**Estado: diseño pendiente de implementación y comprobación.** La exposición pública nunca se extenderá a la red `10.10.10.0/24`.

## Zonas y confianza

| Zona | Función | Confianza permitida |
| --- | --- | --- |
| Internet | Origen de interacciones no solicitadas | Contenido y direcciones observadas no confiables |
| Sensor público dedicado | Cowrie emulado y almacenamiento local limitado | Se asume que puede ser comprometido; no contiene credenciales del SOC ni identidades personales |
| Receptor de telemetría separado | Aceptar mensajes autenticados y limitar volumen | Fuera del laboratorio y separado del sensor; no enruta hacia el SOC |
| Transferencia controlada | Revisar y trasladar lotes de datos | Sin doble conexión simultánea al exterior y al laboratorio; sin reenvío de paquetes |
| SOC privado | Wazuh y análisis | Conserva su administración privada y el aislamiento del laboratorio |
| Administración del sensor | Consola del proveedor o acceso restringido dedicado | Identidades distintas de Cowrie, del receptor y del laboratorio |

No habrá VPN de subred, peering, puente, túnel inverso ni agente del sensor público conectado directamente al Wazuh de `10.10.10.10`. El sensor y el receptor carecerán de rutas confiables hacia LAN doméstica, equipos personales, sistemas corporativos, AD y Windows del laboratorio. Cifrar una conexión no elimina esa frontera.

El [transporte](telemetry-pipeline.md) terminará en el receptor separado. La base conserva el aislamiento mediante importación de lotes sin conexión de red. La analítica continua requeriría una futura revisión de arquitectura; no se habilitará añadiendo una segunda interfaz al SIEM o una ruta al laboratorio.

## Servicios y cortafuegos propuestos

Denegar por defecto entrada, salida iniciada y reenvío, tanto IPv4 como IPv6. Si IPv6 no se utiliza, retirarlo de la exposición y verificar que no eluda las reglas. Revisar cortafuegos del proveedor y del host, NAT, reglas del runtime y sockets efectivos.

| Flujo | Política de diseño |
| --- | --- |
| Internet → sensor, TCP 22 | SSH emulado de Cowrie; puerto público propuesto, sujeto a aprobación del proveedor y prueba de redirección al proceso sin privilegios |
| Internet → sensor, TCP 23 | Telnet emulado opcional; cerrado hasta justificar su activación y verificar controles |
| Administración → host | Preferir consola del proveedor con MFA; si se usa SSH real, interfaz o acceso privado dedicado y origen permitido, claves distintas y sin contraseñas. Puerto exacto por decidir; nunca compartir listener con Cowrie |
| Sensor → receptor | Solo identidad del sensor, destino y puerto exactos del transporte seleccionado; respuestas de conexiones establecidas permitidas |
| Sensor → DNS y tiempo | Solo resolvedores y fuente horaria aprobados, necesarios para operación; impedir consultas arbitrarias originadas por la emulación |
| Sensor → actualizaciones | Ventana de mantenimiento y destinos oficiales acotados; no salida general permanente |
| Cowrie → destinos solicitados por una sesión | Denegado: descargas salientes, proxy, forwarding, SMTP, túneles y conexiones arbitrarias; registrar el intento disponible |
| Sensor/receptor → redes privadas, link-local y metadatos del proveedor | Denegado, además de cualquier acceso a IP públicas de infraestructura doméstica/corporativa o personal; sin rol de nube innecesario |
| Internet/sensor → Wazuh | Denegado: panel, API, indexador, registro de agentes y recepción directa de eventos |

Cambiar el puerto de SSH administrativo no sustituye el control de acceso. Una respuesta SSH/Telnet al cliente pertenece al servicio del señuelo; no autoriza nuevas conexiones salientes hacia otros destinos. El bloqueo de salida debe impedir el uso de destinos permitidos de telemetría/DNS como relés genéricos: el receptor solo acepta datos, valida identidad y esquema, y no interpreta comandos.

## Contención de Cowrie y datos hostiles

- Usuario de servicio sin privilegios, entorno mínimo, permisos de archivos restrictivos y límites de CPU, memoria, sesiones, disco y transferencia. El método de aislamiento se seleccionará y comprobará en HP-1/HP-2; un contenedor por sí solo no demuestra contención.
- Emulación únicamente: sin shell real, backend proxy, QEMU conectado, forwarding, socket del runtime, montajes del host sensibles ni credenciales válidas. Desactivar integraciones automáticas con servicios externos y cualquier backend que envíe transcripciones.
- Deshabilitar recuperación automática de payloads y reforzarlo con egress. Si una carga o entrada queda almacenada, tratarla como objeto hostil en cuarentena privada, sin ejecución ni apertura automática. `noexec` será defensa adicional, no garantía frente a intérpretes.
- Transporte y recopilación con identidades separadas de la administración. Cowrie no debe leer claves del emisor. Una toma de control del host puede robarlas; limitar su alcance al depósito de telemetría de ese sensor y permitir revocación.
- JSON, comandos, nombres, secuencias de terminal y URL son datos no confiables: límites de tamaño/profundidad, escape al visualizar y sin interpolarlos en shell, HTML, consultas o nombres de archivo. Sin respuesta activa Wazuh automática basada en ese contenido.
- Presupuesto, retención y alertas de capacidad deben definirse antes de la exposición. La observación termina si faltan controles o no se puede mantener la seguridad del sensor.

## Riesgos y fallos

| Fallo o supuesto | Impacto y señal | Respuesta prevista |
| --- | --- | --- |
| Vulnerabilidad en Cowrie, runtime o host | Ejecución fuera de la emulación, cambios inesperados, conexiones ajenas a la política | Cerrar exposición desde el proveedor, revocar identidad de transporte y reconstruir |
| Receptor o clave comprometidos | Inyección, alteración o borrado de datos | Permiso de depósito mínimo, registros separados y revocación; marcar intervalo como integridad incierta |
| Certificado vencido, destino inaccesible o cola llena | Retraso o pérdida; la ausencia de eventos puede confundirse con calma | Reintentos limitados, cola con cuota y alarma; nunca fallback en claro ni apertura del SOC |
| Tráfico excesivo o abuso reportado | Agotamiento, costes, pérdida de paquetes o suspensión | Límites y aviso de proveedor, detener servicios públicos; conservar evidencia y registrar lagunas |
| Reloj incorrecto o reinicio | Correlación y duraciones erróneas | Comparar tiempos de evento/recepción, anotar desfase y nueva época del sensor |
| Errores de parsing o cambio de versión | Campos perdidos, tasas incorrectas | Cuarentena y contador de rechazos; revisar contrato antes de actualizar reglas |
| Sesiones y descargas bloqueadas | Visibilidad incompleta del comportamiento | Documentar limitación; no debilitar egress para obtener una historia más llamativa |
| Proveedor filtra antes del sensor | El host no ve todo el tráfico ni prueba un DDoS | Pedir evidencia al proveedor y declarar cobertura; no extrapolar el volumen ausente |
| Retención o publicación incorrectas | Exposición de credenciales e infraestructura | Almacenamiento privado, mínimo acceso y revisión de cada extracto |

La autenticación del emisor acredita qué identidad entregó datos, no su veracidad si el sensor está comprometido. Un inicio de sesión exitoso en Cowrie no prueba acceso al host. La reputación y GeoIP aportan contexto; sus [limitaciones](../enrichment/README.md) acompañarán las conclusiones.

## Recuperación

1. Registrar motivo, hora y alcance. Ante sospecha sobre el host, bloquear servicios públicos y egress desde el control del proveedor; usar consola independiente, no la sesión sospechosa.
2. Revocar credenciales del sensor/receptor que pudieran estar expuestas. Preservar únicamente evidencia necesaria en privado, con hashes, permisos y cadena de custodia; no trasladar ejecutables al SOC.
3. Registrar interrupción, costes, paquetes/eventos perdidos e integridad incierta. Contactar al proveedor por su procedimiento de abuso cuando corresponda.
4. Recrear desde una base conocida y parcheada, aplicar configuración revisada y nuevas claves. No restaurar payloads ni estado comprometido para reanudar el servicio.
5. Repetir comprobaciones de emulación, rutas, IPv6, egress, administración, transporte, tiempo y cuotas. Asignar una nueva época del sensor y documentar las discontinuidades antes de reabrir.

La [lista de despliegue](deployment-checklist.md) exige verificar AUP, ToS, abuso, límites de ancho de banda y cargos de tráfico. No se presupone autorización de ningún proveedor.
