# Global Honeypot Activity

**Estado: NO DATA — DEPLOYMENT PENDING.** Especificación para el futuro mapa; no contiene puntos ni recuentos de demostración.

> Geographic information represents the estimated location of the observed source IP address and does not establish the physical location or identity of an attacker.

Una IP observada puede corresponder a VPN, proxy, salida Tor, proveedor de nube, nodo de botnet, dispositivo comprometido o NAT. Un marcador no identifica a una persona ni su ubicación física. El país de registro de una organización tampoco equivale a la ubicación estimada del origen de red. La precisión de GeoIP tiene límites y no identifica domicilios. [Limitaciones del proveedor de GeoIP](https://support.maxmind.com/knowledge-base/articles/maxmind-geolocation-accuracy).

## Datos y vista

| Elemento | Diseño y cálculo pendiente de campos validados |
| --- | --- |
| Filtros superiores | Ventana UTC, sensor/época, origen observado, protocolo/servicio, país estimado, ASN y tipo de evento |
| Mapa | Agrupar coordenadas estimadas de IP observadas, con tamaño por eventos o fuentes únicas mediante selector explícito; nunca etiquetar «ubicación del atacante» |
| Ficha de origen | IP privada visible para el analista, país estimado, ciudad si existe con precisión razonable, ASN, red/proveedor y fecha/fuente del enriquecimiento |
| Tabla asociada | IP o alias público, país, ciudad disponible, ASN, network/provider, servicio destino, event count, first seen y last seen en la ventana |
| Contexto histórico | First/last seen internos en todo el periodo retenido, separados de los de la ventana actual; sin afirmar antigüedad global |
| Cobertura | Orígenes geolocalizados / orígenes válidos únicos; desconocidos, errores y datos vencidos por separado |

Usar IP de conexión validada; el puerto destino público se derivará del inventario de redirección comprobado, sin confundirlo con el puerto interno o una URL solicitada. La geolocalización se realizará sobre el indicador real en privado **antes** de sustituir IP por alias en un extracto. Nunca consultar GeoIP sobre IP ficticias y presentar el resultado como real.

Si falta ciudad o precisión, mostrar país/región estimados o «desconocido»; no inventar coordenadas, fijarlas en la capital ni colocar desconocidos en 0,0. Cuando la fuente ofrezca radio de precisión, mostrarlo y limitar zoom. Para publicar, preferir agregación por país/ASN o supresión de coordenadas detalladas según revisión.

## Interacción y aceptación futura

Seleccionar un área o red filtrará la tabla y la serie temporal sin cambiar la procedencia. Desde una fila se podrá abrir evidencia revisada o el caso asociado; no lanzar consultas externas ni abrir URL de sesiones automáticamente. El texto de limitación será visible junto al mapa y en exportaciones.

Validar deduplicación, first/last seen, tratamiento de desconocidos y coherencia con [SOC Overview](../soc-overview/README.md). Registrar versión de base GeoIP/ASN, licencia, fecha de consulta y [limitaciones de enriquecimiento](../../enrichment/README.md). La tecnología concreta del mapa y sus tipos de indexación se elegirán cuando exista Wazuh y un contrato real de campos.
