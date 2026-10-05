# Sysmon para SOC-WIN11

**Estado: configuración escrita; instalación y aceptación por Sysmon pendientes — REQUIRES MANUAL EXECUTION.** Se usa Microsoft Sysinternals Sysmon, con [sysmonconfig.xml](sysmonconfig.xml) propio y pequeño. No se ha importado una configuración comunitaria. La referencia es la [documentación oficial de Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon).

## Selección de telemetría

Los ID siguientes son referencias del proveedor, **no eventos observados**.

| Categoría | ID de referencia | Selección y motivo | Límite |
| --- | --- | --- | --- |
| ProcessCreate | 1 | Todos los procesos, SHA-256, línea de comandos y padre | Puede contener secretos en argumentos; medir volumen |
| NetworkConnect | 3 | Destino IPv4 `10.10.10.0/24` | Solo conexiones al lab; no acredita cobertura de Internet, IPv6 ni todo el tráfico entrante |
| FileCreate | 11 | Solo `C:\SOC-Lab\Validation\` | Creación de archivo benigno, no vigilancia completa del disco |
| RegistryEvent | 12–14 | Rutas Run/RunOnce, incluidas variantes WOW6432Node | Visibilidad acotada de autoarranque; no se modifican para probarlas |
| DnsQuery | 22 | Consultas del endpoint | Sin resolvedor local desplegado, validación DNS pendiente; no usar DNS público para pruebas |
| ImageLoad | 7 | No seleccionado | Alto volumen; hashes de ProcessCreate cubren el ejecutable principal, no módulos |
| ProcessAccess | 10 | No seleccionado | Sin caso de uso y baseline aún; no probar acceso a procesos sensibles |
| Otras categorías filtrables declaradas | Varios | `include` vacío | No recopilar archivos borrados, portapapeles ni ruido adicional en esta etapa |

`DnsLookup=false` evita resolución inversa adicional de Sysmon; es independiente de DnsQuery. No se altera Defender. Los eventos internos de servicio, configuración o error de Sysmon pueden existir aunque una categoría filtrable esté vacía. Inspeccionar el esquema real antes de instalar; el formato 4.82 no fija una versión del ejecutable ni promete cobertura de categorías futuras.

## Instalación y comprobación

Descargar el paquete vigente desde Microsoft en la ventana de mantenimiento; guardar ZIP/binarios fuera de Git. Comprobar firma Authenticode válida y firmante Microsoft, versión y SHA-256 del binario y del XML. Copiar la configuración a `C:\SOC-Lab\Config\sysmonconfig.xml`. Desde PowerShell elevado en el directorio del binario x64:

```powershell
Get-AuthenticodeSignature .\Sysmon64.exe | Select-Object Status, SignerCertificate
(Get-Item .\Sysmon64.exe).VersionInfo | Select-Object FileVersion, ProductVersion
Get-FileHash .\Sysmon64.exe -Algorithm SHA256
Get-FileHash C:\SOC-Lab\Config\sysmonconfig.xml -Algorithm SHA256
.\Sysmon64.exe -s
Get-Service -Name '*Sysmon*'
```

Crear primero `SOC-WIN11-wazuh-agent`. Si no hay Sysmon instalado, revisar/aceptar la licencia Sysinternals y ejecutar con el archivo explícito:

```powershell
.\Sysmon64.exe -accepteula -i C:\SOC-Lab\Config\sysmonconfig.xml
if ($LASTEXITCODE -ne 0) { throw 'Sysmon no aceptó la instalación; revisar salida' }
.\Sysmon64.exe -c
Get-Service -Name '*Sysmon*'
wevtutil gl Microsoft-Windows-Sysmon/Operational
Get-WinEvent -LogName 'Microsoft-Windows-Sysmon/Operational' -MaxEvents 5
```

Si ya existe Sysmon, guardar configuración actual y snapshot; actualizar con `Sysmon64.exe -c C:\SOC-Lab\Config\sysmonconfig.xml`, sin reinstalar a ciegas. Confirmar configuración activa y ausencia de errores antes de `SOC-WIN11-sysmon-configured`. Conservar salida real de aceptación: el análisis XML en macOS no sustituye esta prueba.

Ejecutar la [actividad benigna y correlación](../../../docs/telemetry-validation.md) después de arrancar el agente. Registrar campos presentes y ausentes por evento; los campos de red no se esperan en ProcessCreate ni los hashes en todos los tipos. Ante rechazo del XML, revisar el esquema del binario y cambiar una opción cada vez; no sustituirlo por captura global.
