# Enriquecimiento de indicadores

**Estado: diseño; consultas y resultados pendientes.** El enriquecimiento aporta contexto al análisis y no sustituye evidencia de comportamiento. Ninguna reputación por sí sola prueba actividad maliciosa, compromiso o coordinación.

## Fuentes y límites

| Contexto | Método preferido | Limitación que debe registrarse |
| --- | --- | --- |
| GeoIP | Base local versionada y con licencia compatible | Ubicación estimada; precisión/cobertura variables y datos ausentes |
| ASN | Base local con red y organización asociadas | Origen de red, no identidad de la persona; asignaciones pueden cambiar |
| Reverse DNS | Consulta opcional por resolvedor aprobado y caché | PTR puede faltar, cambiar o ser engañoso; DNS comunica el indicador al resolvedor |
| WHOIS/RDAP | Consulta opcional al registro correspondiente, preferentemente RDAP disponible | Describe registro/asignación; no identifica al operador de una sesión. Retirar datos personales |
| Threat reputation | Servicio opcional, consulta mínima de indicador público revisado | Cobertura, antigüedad, falsos positivos y criterio del proveedor; sin resultado no equivale a benigno |
| Known hosting provider | Relacionar ASN, prefijo e información de registro con fecha | Hosting no implica abuso; diferenciar proveedor, cliente y posible intermediario |
| First seen / last seen internally | Mínimo/máximo de tiempo observado en el periodo retenido y sensor definido | No equivale a primera/última actividad global ni fuera de retención |
| Frequency | Eventos/intentos/sesiones deduplicados en una ventana explícita | Unidad, denominador, cobertura y pérdida deben acompañar el valor |

GeoIP no es atribución. La dirección de origen puede representar VPN, proxy, Tor exit, cloud provider, botnet node, compromised device o NAT gateway. No inferir identidad, nacionalidad, domicilio ni coordinación por país/ASN compartido. [Referencia sobre precisión GeoIP](https://support.maxmind.com/knowledge-base/articles/maxmind-geolocation-accuracy).

> Geographic information represents the estimated location of the observed source IP address and does not establish the physical location or identity of an attacker.

## Procedimiento y privacidad

Consultar primero contexto interno y bases locales. Los servicios externos son opcionales y no bloquean una investigación: «no consultado» es un resultado de procedimiento válido con motivo. No habilitar envíos automáticos desde Cowrie o el SIEM; no subir archivos, credenciales, información privada, transcripts, URL con tokens ni hashes de archivos confidenciales.

Antes de una consulta externa, revisar el indicador mínimo, confidencialidad, condiciones del servicio, licencia, cuota y lo que la consulta revela. Usar IP pública observada o hash ya disponible y revisado cuando sea apropiado; no recuperar un payload ni visitar una URL para enriquecerlo. Consultar reputación no autoriza enviar muestras, reportar abuso ni solicitar un escaneo activo a terceros.

Enriquecer en privado antes de asignar alias para publicación. Separar datos nativos, datos calculados y resultados externos, conservando versiones y vigencia; no sustituir la evidencia original. Cachear con caducidad explícita y controlar fallos y límites de API. Texto devuelto por fuentes externas también es no confiable.

## Registro de enriquecimiento

| Evidencia / indicador revisado | Fuente y versión | Query date UTC | Result | Confidence | Limitation / vigencia | Información compartida y decisión |
| --- | --- | --- | --- | --- | --- | --- |
| Pendiente | Pendiente | Pendiente | NO DATA — DEPLOYMENT PENDING | Sin evaluar | Pendiente | No se han realizado consultas |

Justificar confianza alta/media/baja en función de evidencia, fecha y coherencia entre fuentes; no convertir un score de proveedor directamente en certeza analítica. Registrar contradicciones y resultados negativos. Los informes y el [mapa](../dashboards/attack-map/README.md) conservarán estas limitaciones y enlazarán las evidencias sanitizadas.
