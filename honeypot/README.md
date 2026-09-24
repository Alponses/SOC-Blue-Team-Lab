# Internet Honeypot — Cowrie

**Estado: diseño del entregable 0.5. NO DATA — DEPLOYMENT PENDING.** No existe un sensor público ni telemetría recopilada.

El proyecto añade observación de actividad no solicitada de Internet al laboratorio controlado existente. El sensor será un VPS o equipo público dedicado, fuera de `10.10.10.0/24`, sin confianza ni rutas hacia la LAN doméstica, equipos personales o corporativos, AD o Windows del laboratorio. **Observed Internet activity does not imply compromise of a production environment.**

## Tecnología y propósito

Cowrie será el primer honeypot, exclusivamente con shell emulada. Su documentación distingue el modo emulado de los modos que conectan a otros sistemas; este proyecto excluye proxy, backends con shell real y ejecución de binarios recibidos. Cowrie ofrece registro JSON e interacción SSH/Telnet. [Referencia oficial de Cowrie](https://docs.cowrie.org/en/latest/README.html).

Se investigarán autenticaciones, usuarios intentados, sesiones, comandos, tiempos, direcciones de origen e intentos de descarga. La aceptación de credenciales por el señuelo describe una sesión emulada, no una intrusión en el sistema anfitrión. La política inicial bloqueará las descargas salientes; aun así, se conservará el intento observado cuando Cowrie lo registre. Cualquier archivo recibido permanecerá en cuarentena privada y nunca se ejecutará.

El resultado buscado es una cadena verificable: Cowrie → JSON → transporte seguro → ingestión Wazuh → parsing → normalización → detección → enriquecimiento → paneles → investigación → informe. Los recuentos por sí solos no constituyen un hallazgo SOC.

## Documentación de implementación futura

| Documento | Decisión o comprobación |
| --- | --- |
| [Modelo de seguridad](security-model.md) | Zonas, administración, cortafuegos, egress, riesgos y recuperación |
| [Flujo de telemetría](telemetry-pipeline.md) | Frontera de confianza, transporte y control de calidad |
| [Lista previa al despliegue](deployment-checklist.md) | Proveedor, controles, criterios de apertura y parada |
| [Visibilidad Suricata](suricata-visibility.md) | Interfaz, cobertura, EVE y límites del monitoreo volumétrico |
| [Configuraciones](../configs/honeypot/README.md) | Espacios reservados para Cowrie y Wazuh; sin configuración ejecutable |
| [Paneles](../dashboards/README.md) | Especificaciones, sin objetos importables ni métricas inventadas |
| [Enriquecimiento](../enrichment/README.md) | Contexto, fuentes y límites de atribución |
| [Investigaciones](../incidents/README.md) | SOC-011–SOC-015 pendientes de observaciones reales |
| [Informes](../reports/README.md) | Plantilla semanal reutilizable |

## Fases posteriores y T-Pot

Las fases HP-1 a HP-4 del [plan de implementación](../docs/implementation-checklist.md#fases-honeypot-posteriores) están pendientes y se ejecutarán después del entregable 1 y de cumplir sus requisitos. HP-1 resolverá infraestructura y transporte; HP-2 desplegará Cowrie y comprobará aislamiento; HP-3 validará la cadena analítica; HP-4 investigará observaciones reales y emitirá informes. Ninguna de ellas forma parte de 0.5.

T-Pot queda como una segunda fase **opcional**, posterior a demostrar Cowrie → telemetría → Wazuh → detección → investigación. Se evaluarán protocolos adicionales, visualización Elastic, Attack Map y otras fuentes de red. Requerirá revisar de nuevo recursos, aislamiento, proveedor, egress, licencias y separación de datos. No está instalado ni autorizado como parte de este refactor.
