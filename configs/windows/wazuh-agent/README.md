# Canales del agente Windows

**Estado: plantilla escrita; REQUIRES MANUAL EXECUTION.** [ossec.conf.example](ossec.conf.example) es un fragmento con raíz XML para revisión; no es una exportación de un agente instalado ni una configuración completa.

La [documentación de Wazuh](https://documentation.wazuh.com/current/user-manual/capabilities/log-data-collection/configuration.html) incluye Security, System y Application por defecto. No añadir otra entrada de los canales ya existentes. Inspeccionar primero `C:\Program Files (x86)\ossec-agent\ossec.conf` y la configuración central de los grupos asignados; verificar la ruta real con el servicio si difiere.

## Aplicación en SOC-WIN11

1. Crear el checkpoint previo y guardar una copia privada de la configuración instalada, con fecha UTC. Puede contener datos que no deben publicarse.
2. Enumerar las entradas actuales desde Windows PowerShell elevado:

   ```powershell
   $agentRoot = 'C:\Program Files (x86)\ossec-agent'
   [xml]$agentConfig = Get-Content -LiteralPath "$agentRoot\ossec.conf" -Raw
   $agentConfig.ossec_config.localfile |
       Select-Object location, log_format, query, 'only-future-events'
   $agentConfig.ossec_config.localfile |
       Group-Object location | Where-Object Count -gt 1
   ```

3. Fusionar el servidor `10.10.10.10:1514/TCP` en el bloque `client` existente, conservando las opciones de enrollment. Editar Security y System en su sitio. Añadir Sysmon, PowerShell y Defender solamente si faltan. Mantener Application, inventario, SCA, FIM y protecciones instaladas.
4. Para esta validación, retirar del bloque de cada canal requerido los filtros `query` que excluirían eventos normales. Registrar el XPath anterior y la decisión; la plantilla recoge los cinco canales sin filtro durante una ventana medida. Si existe configuración central, resolverla allí o retirar solo la duplicación de estos canales; no borrar grupos enteros.
5. Comprobar XML, canales únicos y configuración efectiva desde el dashboard/API interna; reiniciar `Restart-Service WazuhSvc`. Leer los errores y mensajes de suscripción en `ossec.log`. Un XML bien formado no prueba que Wazuh lo acepte.
6. Crear eventos **después** del reinicio y de habilitar archives en el manager. La [opción only-future-events](https://documentation.wazuh.com/current/user-manual/reference/ossec-conf/localfile.html) está en `yes`: no asumir reenvío de registros anteriores o generados durante una parada.
7. Seguir la [validación por fuente](../../../docs/telemetry-validation.md). Ante un error, restaurar la copia privada, reiniciar el agente y revisar su estado. No restaurar `client.keys` desde Git ni publicar ese archivo.

Security/System no necesitan un agente adicional. Todas las entradas usan `eventchannel`. No se añaden decoders, reglas personalizadas ni respuestas activas.
