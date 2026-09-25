# Validación de telemetría Windows → Wazuh

**REQUIRES MANUAL EXECUTION.** No se ha ejecutado ninguna prueba en Windows o Wazuh. [Matriz real](deliverables/deliverable-1.md#matriz-de-validación) e [inventario de evidencias](../evidence/deliverable-1/README.md). El objetivo es disponibilidad de datos; no se crean incidentes, reglas ni simulaciones de ataque.

## Preparación de la ventana

1. Verificar ambas VM, recursos, versiones exactas, [snapshots](../evidence/deliverable-1/README.md#snapshots), configuración aplicada y agent ID real.
2. Retirar NAT; comprobar que solo SOC-LAB conecta las VM, sin gateway externo, red puente, forwarding IPv4/IPv6 ni servicios publicados. Actualizaciones y descargas deben terminar antes.
3. Comparar UTC del host, Windows y Ubuntu, anotar fuente y desfase. Registrar inicio/fin de la prueba, zona original e incertidumbre; no restar timestamps de relojes sin comprobarlos.
4. Activar la [ventana de archives](../configs/wazuh/README.md). Confirmar Filebeat e indexer y medir espacio. No cambiar el umbral global de alertas ni añadir una regla para forzar eventos normales a `wazuh-alerts-*`.
5. Revisar la configuración efectiva del canal en curso y reiniciar el agente si se modificó, **antes** de generar datos. `only-future-events=yes` impide dar por supuesto que un evento antiguo se reenvíe. Al terminar, verificar que permanecen los cinco canales.

## Orden obligatorio y rendimiento

Procesar **Security → System → Sysmon → PowerShell → Defender**, una fuente por vez. Para cada una: localizar/generar evento benigno, comprobarlo localmente, confirmar canal/configuración del agente y conectividad, encontrar el mismo evento en Wazuh y guardar evidencia/resultado. No cambiar otra fuente hasta conocer el resultado de la actual; si falla, documentar y diagnosticar una capa por vez. No marcar PASS sin evidencia. La instalación/configuración de Sysmon y la política de PowerShell se aplican al llegar a su paso.

En el host, observar Memory Pressure en Activity Monitor y guardar mediciones UTC de `sysctl vm.memory_pressure`, `sysctl vm.swapusage` y `vm_stat` antes de arrancar, después de cada VM y durante cada fuente. Los contadores acumulados de swap no representan por sí solos presión actual. Si la presión grave sostenida o la paginación impide validar, detener la sesión, documentar el impacto y apagar limpiamente los invitados; no reducir arbitrariamente la RAM asignada. Aún no se ha ejecutado esta prueba con ambas VM.

## Estado local y actividad benigna

Desde **Windows PowerShell 5.1 elevado** en SOC-WIN11:

```powershell
# Comenzar con Security; cambiar solo al canal de la siguiente etapa
# después de registrar el resultado completo de la etapa actual.
$channel = 'Security'
Get-Service WazuhSvc
Get-WinEvent -ListLog $channel |
    Select-Object LogName, IsEnabled, RecordCount, MaximumSizeInBytes, LogMode
$since = Get-Date
$since.ToUniversalTime().ToString('o')
```

Guardar el inicio; repetirlo si se cambia la configuración y explicar por qué. Un canal inexistente, deshabilitado, sin eventos o inaccesible requiere diagnóstico; no equivale a éxito.

| Fuente / proveedor | Canal | Actividad y selección local | ID de referencia, no observado |
| --- | --- | --- | --- |
| Windows Security Auditing | Security | Inicio de sesión normal exitoso con cuenta del lab; conservar sesión/configuración y seleccionar un evento nuevo | 4624 si la auditoría y el inicio de sesión lo producen |
| Proveedor real del evento de sistema | System | Evento nuevo natural de servicio/sistema; puede usarse el reinicio normal del agente durante configuración | Usar el ID que realmente aparezca |
| Microsoft-Windows-Sysmon | Microsoft-Windows-Sysmon/Operational | PowerShell, cmd, Notepad y conexión TCP al manager privado | 1 y 3; 11 opcional |
| Microsoft-Windows-PowerShell | Microsoft-Windows-PowerShell/Operational | Nueva sesión y comando benigno tras habilitar logging | 4104 |
| Microsoft-Windows-Windows Defender | Microsoft-Windows-Windows Defender/Operational | Evento natural reciente o QuickScan normal | 1000/1001 si se observan inicio/fin |

En la etapa Sysmon, después del inicio de su ventana, abrir procesos normales y una conexión privada, sin bucles, escaneos de puertos ni autenticaciones fallidas:

```powershell
Start-Process "$env:WINDIR\System32\WindowsPowerShell\v1.0\powershell.exe" -ArgumentList '-NoProfile', '-Command', 'Get-Date; Write-Output "SOC-D1-BENIGN"'
Start-Process "$env:WINDIR\System32\cmd.exe" -ArgumentList '/c', 'echo SOC-D1-BENIGN'
Start-Process "$env:WINDIR\System32\notepad.exe"
Test-NetConnection -ComputerName 10.10.10.10 -Port 1514
# Opcional: archivo de texto propio dentro del filtro FileCreate.
New-Item -ItemType Directory -Path C:\SOC-Lab\Validation -Force | Out-Null
Set-Content -LiteralPath C:\SOC-Lab\Validation\benign.txt -Value 'SOC-D1-BENIGN'
```

En la etapa PowerShell, tras aplicar la política y abrir una nueva sesión, ejecutar `Get-Date` y seleccionar el evento local correspondiente antes de buscarlo en Wazuh. En la etapa Defender, usar un evento normal nuevo o, solo si falta, ejecutar:

```powershell
# Solo si falta un evento Defender reciente:
Start-MpScan -ScanType QuickScan
```

Esperar a los eventos de scan; una orden que retorna sin error no prueba que el scan haya finalizado. No usar EICAR ni desactivar Defender. No lanzar DNS contra Internet: DnsQuery está configurado, pero su ejercicio puede esperar al DNS local. No tocar Run keys ni procesos sensibles para producir categorías opcionales de Sysmon.

Referencias de ID: [logon 4624](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4624), [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon), [PowerShell](../configs/windows/powershell/logging.md) y [Defender](https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus). No confundir documentación del proveedor con evidencia.

## Selección de evidencia local

```powershell
Get-WinEvent -FilterHashtable @{LogName=$channel; StartTime=$since} -MaxEvents 10 |
    Select-Object TimeCreated, MachineName, ProviderName, LogName, Id, RecordId, Message
```

Elegir un registro real por canal y, para Sysmon, al menos proceso y conexión. Inspeccionar `ToXml()` del evento seleccionado para obtener `EventData` completo; el texto renderizado puede omitir campos. Exportar XML/EVTX originales fuera del repositorio en almacenamiento privado. No limpiar los canales. Si se usó logon/logout y se perdió `$since`, reconstruir el inicio desde la hora registrada; no usar una ventana desconocida.

Anotar por cada selección: hostname, proveedor, canal, Event ID, EventRecordID, UTC original y archivo privado. Capturar usuario, proceso y datos específicos solo si están presentes. Para Sysmon 1: `Image`, `CommandLine`, `ParentImage`, `User`, `ProcessId`, `ProcessGuid`, `Hashes`; para Sysmon 3: `Image`, `ProcessId`, `ProcessGuid`, IP/puertos origen/destino y protocolo. Anotar ausencias o sustituciones por separado; no trasladar campos de otro evento como si fueran del seleccionado.

## Agente y recepción en manager

1. Guardar un extracto sanitizado de los cinco `localfile` efectivos, hash de configuración aplicada, servicio `WazuhSvc` activo y mensajes relevantes de `ossec.log` sobre suscripciones/conexión o errores. No exportar claves, tokens ni todo el log. El estado Active acredita conexión, no cada canal.
2. En SOC-WAZUH ejecutar `sudo /var/ossec/bin/agent_control -l`; registrar ID, nombre, estado y versión real. Comprobar conectividad privada por 1514 y logs de recepción/error del manager. Un socket establecido por sí solo no acredita el contenido del evento.
3. Buscar el registro correlacionado en `/var/ossec/logs/archives/archives.json`. Si la ventana cruzó rotación, revisar el archivo correspondiente a la fecha, sin asumir ausencia. Si se usa `jq`, instalarlo desde el repositorio Ubuntu durante mantenimiento. Consulta inicial, **ejemplo pendiente**:

   ```sh
   sudo jq -c 'select(.agent.name == "SOC-WIN11") | {timestamp, agent, location, data}' /var/ossec/logs/archives/archives.json
   ```

4. Inspeccionar el esquema de un evento real: los campos habituales son `data.win.system.channel`, `eventID`, `eventRecordID`, `computer`, `systemTime`, `providerName` y `data.win.eventdata`. Ajustar solo a lo observado. Filtrar al canal y RecordID seleccionado; conservar el JSON mínimo sanitizado junto con la consulta exacta. No publicar la salida masiva del ejemplo.
5. Correlacionar **canal + proveedor + equipo + EventRecordID + Event ID + hora** entre XML local y JSON del manager. Si hay reinicios/limpieza de logs, RecordID solo no basta. Usar ProcessGuid o marcador cuando exista. La coincidencia de un ID común sin más contexto no prueba la cadena.

No todos los agentes exponen una confirmación individual por evento en su log. La configuración efectiva, el servicio activo y la coincidencia del evento en archives bajo el agent ID correcto permiten respaldar la recogida; registrar esta inferencia y sus límites, sin inventar un ACK del agente.

## Indexer y dashboard

Abrir el dashboard privado desde el host; comprobar el endpoint en **Agents/Endpoints** (nombre exacto de menú según versión), agent ID, versión y Active con hora reciente. Guardar una captura explicada, sin credenciales. Después, en **Explore → Discover**, seleccionar `wazuh-archives-*`, usar `timestamp` y fijar el intervalo UTC real. Las rutas de interfaz se verifican al ejecutar.

Consultas de partida para el esquema esperado; **ninguna se ha ejecutado**:

```text
agent.name:"SOC-WIN11" AND data.win.system.channel:"Security"
agent.name:"SOC-WIN11" AND data.win.system.channel:"System"
agent.name:"SOC-WIN11" AND data.win.system.channel:"Microsoft-Windows-Sysmon/Operational"
agent.name:"SOC-WIN11" AND data.win.system.channel:"Microsoft-Windows-PowerShell/Operational"
agent.name:"SOC-WIN11" AND data.win.system.channel:"Microsoft-Windows-Windows Defender/Operational"
```

Añadir mediante filtros el agent ID, EventRecordID y Event ID **observados**. Expandir el documento: guardar `_index`, `_id`, `timestamp`, datos correlacionados y la consulta/ventana, con captura o JSON sanitizado. El documento del indexer debe coincidir con la evidencia local y del manager. Una captura del conteo general no demuestra la fuente seleccionada. Si se usa `wazuh-alerts-*` para un evento que produjo una alerta integrada, registrar índice y regla reales; no exigir una alerta para aprobar ingestión.

La marca `timestamp` del manager no debe presentarse automáticamente como hora exacta de indexación. Registrar también cuándo se encontró en Discover; expresar latencia como aproximación o cota según la precisión disponible. Medir conteo por canal y duración; calcular volumen solo con datos reales.

## Cierre de la sesión

Actualizar las cinco fichas de [evidencia](../evidence/deliverable-1/README.md), la matriz y versiones solo con observaciones. Conservar originales privados y hashes, publicar mínimos revisados. Cerrar archives según su procedimiento, cerrar enrollment y comprobar agente/Defender/firewall. Eliminar únicamente el archivo benigno propio y cerrar aplicaciones abiertas durante la prueba si corresponde; no borrar evidencias. Registrar limpieza real.

Crear snapshots finales solo después de verificar todos los criterios. Si falta cualquier canal o etapa de la cadena, conservar **DELIVERABLE 1 — IN PROGRESS**. Una comprobación estática de este repositorio no cambia ese estado.

## Diagnóstico sistemático, aún no ejecutado

Esta secuencia es un procedimiento; no una lista de problemas que hayan ocurrido:

1. ¿Existe un evento nuevo local? Revisar horario, auditoría, política de PowerShell, instalación Sysmon y scan Defender.
2. ¿Existe y está habilitado el canal? Consultar `Get-WinEvent -ListLog`/`wevtutil gl` y permisos sin deshabilitar controles.
3. ¿Corre WazuhSvc? Revisar servicio y log, versión y hora.
4. ¿Está configurado una sola vez? Revisar nombre exacto, `eventchannel`, XPath, configuración central y `only-future-events`.
5. ¿Alcanza Windows `10.10.10.10:1514`? Revisar NIC, rutas y reglas precisas; 1515 solo para enrollment.
6. ¿Recibe el manager al agent ID correcto? Revisar `agent_control`, conexión y logs; no extraer claves.
7. ¿Existe el JSON en archives? Revisar `logall_json`, rotación, parser y luego Filebeat/TLS/indexer.
8. ¿Se encuentra en Discover? Revisar patrón archives, intervalo, zona horaria, permisos, filtros y mapeo real.

Cambiar una sola variable, registrar antes/después y repetir el mismo control. No modificar varias capas simultáneamente ni añadir detecciones para ocultar fallos de transporte. Los [problemas realmente encontrados](deliverables/deliverable-1.md#problemas-encontrados) se registran aparte.
