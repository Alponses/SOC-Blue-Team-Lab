# Lista previa al despliegue público

**Estado: todo pendiente. Este documento no autoriza ni ejecuta despliegues.** Forma parte del diseño 0.5; se utilizará en HP-1/HP-2 del [plan](../docs/implementation-checklist.md#fases-honeypot-posteriores).

## Proveedor y alcance

- [ ] Identificar proveedor, región, responsable y presupuesto; verificar explícitamente **Acceptable Use Policy (AUP)** y **Terms of Service (ToS)** vigentes para honeypots, tráfico no solicitado y muestras potencialmente maliciosas. Registrar enlaces, fecha y cláusulas aplicables; solicitar aclaración al proveedor si no es concluyente.
- [ ] Verificar procedimientos de abuso, contacto, plazos de respuesta, suspensión y protección volumétrica disponible. No asumir que alquilar un VPS permite esta actividad.
- [ ] Verificar límites de ancho de banda, tráfico incluido, cargos de entrada/salida, límites de disco, almacenamiento de logs y costes del receptor/enriquecimiento. Definir alertas de gasto y condiciones de parada.
- [ ] Definir jurisdicción aplicable, tratamiento de IP/credenciales, permisos de acceso, retención y eliminación de datos; documentar la decisión sin publicar información privada.
- [ ] Delimitar sensor dedicado, sin servicios de producción, cuentas de trabajo ni acceso al hogar. Registrar SSH emulado y decisión sobre Telnet; no incorporar otros protocolos todavía.

## Antes de abrir puertos

- [ ] Elegir versión fijada, fuente oficial, sistema compatible, método de aislamiento y actualización; no depender de una etiqueta mutable sin registrar la revisión.
- [ ] Verificar shell emulada, ausencia de proxy/backends reales y forwarding; proceso sin privilegios y sin acceso a secretos, metadatos, montajes sensibles o socket del runtime.
- [ ] Separar administración y señuelo. Probar consola de recuperación y MFA, acceso administrativo restringido y claves independientes, sin reenviar agente SSH al sensor.
- [ ] Comprobar cortafuegos del proveedor y host, redirecciones, listeners y rutas IPv4/IPv6. No habrá ruta sensor/receptor → laboratorio, LAN doméstica, equipos personales/corporativos ni AD/Windows.
- [ ] Aplicar salida denegada por defecto y excepciones por servicio/identidad. Verificar bloqueo de descargas, forwarding, proxy y conexiones arbitrarias; nunca probar contra terceros.
- [ ] Elegir y documentar [transporte](telemetry-pipeline.md), receptor sin rutas al SOC, identidades, validación de destino, revocación, cola y acuses. Probar que una identidad inválida no pueda entregar datos.
- [ ] Definir transferencia local revisada, periodicidad y demora aceptable. Probar ingestión Wazuh sin exponer panel, API, indexador ni registro público de agentes.
- [ ] Definir valores concretos de cuotas, retención, rotación, duración de sesiones, capacidad, pérdida tolerable y parada por falta de telemetría; verificar alertas de salud por canal independiente.
- [ ] Desactivar enriquecimiento, envío de muestras y reportes de abuso automáticos a terceros. Registrar fuente horaria, desfase, sensor/época y política privada de evidencia.
- [ ] Evaluar [Suricata](suricata-visibility.md), interfaz y métricas de host/proveedor necesarias; registrar visibilidad no disponible.

## Aceptación y apertura futura

- [ ] Probar primero con tráfico inocuo y autorizado en entorno privado: autenticación, comando marcador, cierre, intentos de salida bloqueados, interrupción de transporte, rotación y recuperación. Etiquetar `Evidence Origin: Controlled Simulation`.
- [ ] Guardar muestras reales del software de esas pruebas, comprobar campos y fijar contrato. No mezclarlas con actividad no solicitada ni métricas operativas.
- [ ] Revisar el [modelo de seguridad](security-model.md), evidencia de las pruebas y procedimiento de recuperación. Registrar qué responsable abre únicamente los servicios aprobados y cuándo.
- [ ] Tras la apertura, distinguir pruebas administrativas de observaciones de Internet; supervisar capacidad, retraso, pérdida y costes. No generar ataques públicos para producir casos o validar umbrales.
- [ ] Detener exposición ante compromiso del host, pérdida de controles, aviso del proveedor, costes fuera del límite o incapacidad de supervisión. No bajar controles para mantener el conteo.

Las pruebas de carga serán limitadas, autorizadas y sobre una réplica privada aislada. Nunca se generará un DDoS público ni se hará carga contra infraestructura pública, incluido el VPS del proyecto.
