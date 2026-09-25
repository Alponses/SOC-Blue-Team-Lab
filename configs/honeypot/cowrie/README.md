# Cowrie — requisitos de configuración

**Estado: NO DATA — DEPLOYMENT PENDING.** No hay `cowrie.cfg`, despliegue ni registros de este sensor. Se fijará versión y se revisarán sus opciones antes de redactar configuración ejecutable.

| Área | Requisito y evidencia futura |
| --- | --- |
| Backend | Shell emulada local; verificar ausencia de proxy, backend real, backend LLM/externo, forwarding y ejecución en el host |
| Servicios | SSH como primer servicio; Telnet opcional. Registrar puertos público y de escucha efectivos, redirección y separación de administración |
| Salida | JSON estructurado con rotación y permisos privados; verificar ruta real y un registro de cada tipo disponible |
| Identidad | Alias del sensor y época de despliegue, tiempo UTC y configuración versionada; identidad de transporte asignada fuera del contenido recibido |
| Autenticación | Usuarios ficticios de emulación, sin credenciales del host; registrar qué política acepta sesiones para interpretar el resultado |
| Comandos y archivos | Registrar comandos e intentos; impedir descargas salientes y ejecución automática; cuarentena de archivos recibidos, cuotas y sin binarios en Git |
| Recursos | Límites concretos de sesiones, CPU, memoria, disco, retención y cola; probar rotación, reinicio y condiciones de parada |
| Integraciones | Sin envío automático de transcripciones, URL, credenciales, muestras ni reportes a terceros |

La configuración distribuida de Cowrie es una referencia para localizar opciones de la versión elegida; no se asumirá que sus valores predeterminados cumplen esta política. [Configuración oficial de referencia](https://github.com/cowrie/cowrie/blob/main/src/cowrie/data/etc/cowrie.cfg.dist).

Conservar muestras privadas de la fuente y fragmentos revisados antes de definir [campos y reglas Wazuh](../wazuh/README.md). Los ensayos del operador serán `Controlled Simulation`, aunque utilicen Cowrie; solo la actividad no solicitada será `Observed Honeypot Telemetry`. Aplicar la [lista de despliegue](../../../honeypot/deployment-checklist.md).
