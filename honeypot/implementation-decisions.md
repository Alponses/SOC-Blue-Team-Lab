# Decisiones de implementación del honeypot

**Estado: diseño 0.5; todas las decisiones operativas siguen pendientes.** Este registro se completará en HP-1 con la infraestructura disponible, después del entregable 1. No selecciona proveedor, crea recursos, fija secretos ni autoriza apertura de puertos.

Se mantiene como decisión de arquitectura Cowrie con shell emulada local, sensor público separado, telemetría saliente hacia un receptor externo sin rutas al SOC e importación de lotes revisados sin conexión de red. El protocolo concreto se elegirá entre las [alternativas de transporte](telemetry-pipeline.md#decisión-de-transporte-pendiente). La latencia de ese diseño debe ser aceptada explícitamente; si se necesita monitoreo continuo, se revisará la arquitectura antes de implementarlo.

## Registro pendiente de HP-1

Cada decisión requiere responsable, fecha, alternativas consideradas, elección, motivo, evidencia verificable, limitaciones y criterio de revisión. Publicar alias y referencias revisadas; guardar IP de infraestructura, cuentas, credenciales y anexos sensibles en privado.

| ID | Decisión pendiente | Evidencia necesaria para resolverla |
| --- | --- | --- |
| HP-D01 | Proveedor, región y alcance permitido | AUP, ToS, procedimiento de abuso, límites de banda, cargos de tráfico y fecha de revisión; aclaración del proveedor si el permiso no es concluyente |
| HP-D02 | Capacidad, presupuesto, retención y responsables | Cuotas de CPU/RAM/disco/sesiones/cola, tráfico y almacenamiento; plazos de eliminación; salud, canal de aviso y condiciones de parada con valores concretos |
| HP-D03 | Versión Cowrie, aislamiento y servicios | Versión fijada y procedencia, shell local emulada, cuenta sin privilegios, SSH inicial, decisión Telnet, puertos/listeners y bloqueo de descargas/ejecución |
| HP-D04 | Management plane y firewall | Identidades independientes, MFA/consola, acceso restringido; matriz IPv4/IPv6, NAT y egress por proceso/servicio, sin rutas de confianza hacia sistemas privados |
| HP-D05 | Transporte sensor → receptor | Una alternativa seleccionada; endpoints/puertos privados documentados, autenticación de ambos extremos, cifrado, permisos mínimos, revocación, cuotas, acuses, reintentos y recuperación |
| HP-D06 | Transferencia receptor → SOC | Estación/medio dedicados, sin doble conexión ni reenvío; manifiestos, validación y minimización antes de importar, custodio, frecuencia, demora máxima aceptable y corte de ingestión |
| HP-D07 | Suricata y métricas de red | Interfaz/punto de captura real, cobertura demostrable, EVE seleccionado, fuente de tasas/SYN/estados/impacto, pérdida, recursos y limitaciones upstream |
| HP-D08 | Enriquecimiento y mapa | Fuentes/licencias/actualización GeoIP/ASN, resolución y desconocidos; consultas externas opcionales fuera del SOC, revisión de datos compartidos y backend del mapa |
| HP-D09 | Recuperación y criterios de apertura | Responsable, consola independiente, cierre desde proveedor, revocación, preservación privada, reconstrucción y repetición de pruebas de aislamiento e ingestión |

No basta elegir «VPN» o «HTTPS»: HP-D05 debe explicar qué identidad puede entregar qué datos a qué receptor y demostrar que no obtiene acceso al laboratorio. El receptor no es un bastión hacia Wazuh. Las excepciones para direcciones privadas de un túnel, si se necesitan, serán exclusivas del servicio externo y no incluirán subredes del analista.

## Criterios entre fases

| Fase | Resultado exigido | Límite |
| --- | --- | --- |
| HP-1 | Decisiones resueltas, configuraciones revisables y pruebas de aceptación definidas | Sin exponer un sensor por haber elegido proveedor o protocolo |
| HP-2 | Controles probados en privado y un lote minimizado recibido por Wazuh; apertura solo tras completar la lista previa | Las pruebas del operador son Controlled Simulation; no acreditan actividad de Internet |
| HP-3 | Contrato basado en eventos inspeccionados, detecciones, correlación temporal, consultas, enriquecimiento y paneles comprobados | Un transporte que funciona no demuestra parsing, métricas o reglas correctos |
| HP-4 | Investigaciones e informes respaldados por comportamiento observado suficiente | Los casos sin evidencia siguen pendientes; no fabricar sesiones ni DDoS |

Seguir la [lista previa al despliegue](deployment-checklist.md) y el [plan de implementación](../docs/implementation-checklist.md#fases-honeypot-posteriores). T-Pot sigue siendo opcional después de demostrar la cadena Cowrie y una investigación completa.
