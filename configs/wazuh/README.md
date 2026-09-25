# Wazuh todo en uno: ventana de validación

**REQUIRES MANUAL EXECUTION.** La [instalación](../../docs/wazuh-installation.md) conserva manager, indexer y dashboard en SOC-WAZUH. Filebeat lleva los eventos al indexer. No hay clúster multinodo ni cambios de reglas.

## Archives temporales

Un evento normal puede no aparecer en `wazuh-alerts-*`. Para probar ingestión completa, habilitar JSON archives durante una sesión de **hasta 30 minutos**, con espacio libre verificado antes y cada cinco minutos. Detener la generación y cerrar la ventana si quedan menos de 10 GiB libres o crece demasiado rápido. Son límites operativos propuestos, no valores medidos.

Después del snapshot y backup privado de `/var/ossec/etc/ossec.conf`, fusionar **dentro del bloque global existente**, sin duplicarlo:

```xml
<logall_json>yes</logall_json>
```

Conservar `jsonout_output`, `alerts_log` y los demás valores existentes. No activar `logall` de texto si no se necesita. En el bloque `filebeat.modules` existente de `/etc/filebeat/filebeat.yml`, módulo `wazuh`, mantener alertas y cambiar solo archives:

```yaml
filebeat.modules:
  - module: wazuh
    alerts:
      enabled: true
    archives:
      enabled: true
```

Es un **fragmento**, no reemplaza hosts, TLS, keystore ni el resto de Filebeat. Reiniciar manager, ejecutar `sudo filebeat test config` y `sudo filebeat test output`, luego reiniciar Filebeat. Revisar estado y logs privados. Crear el patrón `wazuh-archives-*` con campo de tiempo `timestamp` en Dashboard Management → Index patterns; consultar en Explore → Discover. No crear visualizaciones personalizadas.

Fuente: [archivado e indexación oficiales](https://documentation.wazuh.com/current/user-manual/manager/event-logging.html). Seguir solo las secciones de archivado; sus ejemplos de ataque no forman parte del laboratorio en esta etapa.

## Cierre y conservación

Registrar inicio/fin UTC, crecimiento, conteos, rango temporal, consultas y archivos seleccionados. Confirmar que las últimas evidencias llegaron al indexer antes de cerrar. Restaurar `logall_json` y `archives.enabled` a sus valores previos y reiniciar los servicios afectados. Mantener los cinco canales del agente activos. La desactivación del archivado no borra datos ya almacenados.

Los originales quedan en almacenamiento privado durante la revisión, propuesta inicial: siete días. La rotación de archivos no es una política de borrado de índices. Registrar fecha/responsable de eliminación o extensión justificada tanto para archivos como índices. No ejecutar borrados con comodines desde esta guía. Exportar y verificar hashes de la evidencia antes de cualquier eliminación.

Tras cerrar la ventana, los eventos sin alerta dejarán de ser consultables como nuevos archives; anotarlo como límite de la ruta de validación. Una etapa posterior decidirá la retención sostenida con mediciones reales. Consultar [validación](../../docs/telemetry-validation.md) antes de marcar alguna fuente como recibida.
