# Instalación de SOC-WIN11

**Estado: REQUIRES MANUAL EXECUTION.** No hay SOC-WIN11 registrado en el hipervisor inspeccionado. No se han observado Windows, Defender, agente ni Sysmon. [Estado del entregable](deliverables/deliverable-1.md).

## Endpoint y red

Conservar **SOC-WIN11**, `10.10.10.30/24`, Windows 11 Enterprise de evaluación, **2 vCPU / 4 GiB RAM / 80 GB** de disco según la arquitectura. Mantener grupo de trabajo; no unir a AD. Obtener medio/licencia de evaluación desde el [Evaluation Center de Microsoft](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-11-enterprise). Verificar [requisitos de CPU, TPM 2.0 y UEFI/Secure Boot](https://www.microsoft.com/en-us/windows/windows-11-specifications) y soporte de Windows 11 en la versión instalada de VirtualBox; no eludir comprobaciones. Se conservan los 80 GB del diseño; Microsoft exige al menos 64 GB.

Usar la red **Host-Only Network SOC-LAB** existente. En la NIC privada: IP estática, prefijo 24, sin gateway ni DNS externo. NAT temporal solo para actualizaciones/descargas, sin port forwarding; retirarlo antes de validar. No asignar DNS `10.10.10.20` hasta que exista SOC-DC01. Comprobar `Get-NetIPConfiguration`, `Get-NetRoute -AddressFamily IPv4` y rutas IPv6. Confirmar dirección del host administrador antes de usar `10.10.10.1` como origen de firewall.

Crear una cuenta ficticia del laboratorio, guardar credenciales fuera de Git y completar actualizaciones. Mantener Defender, Firewall de Windows, UAC, Secure Boot y las protecciones estándar. No añadir exclusiones antivirus para los ejercicios. Crear `SOC-WIN11-clean-install` antes del agente y del cambio de logging.

Inventario real desde Windows PowerShell elevado, guardando solo campos necesarios:

```powershell
Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsName, OsVersion, OsBuildNumber, OsArchitecture, CsName, CsTotalPhysicalMemory
Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores, NumberOfLogicalProcessors
Get-Volume -DriveLetter C | Select-Object DriveLetter, Size, SizeRemaining
Get-NetIPConfiguration
Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction
Get-MpComputerStatus | Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled, AMRunningMode, AMProductVersion, AMEngineVersion, AntivirusSignatureVersion, AntivirusSignatureLastUpdated
Get-Date -Format o
w32tm /query /status
```

Defender debe estar activo en modo normal y protección en tiempo real habilitada. Una consulta de estado no prueba un evento Defender ingerido. Si aparece pasivo/deshabilitado, investigar la política o producto instalado sin debilitar controles. Registrar cualquier limitación de tiempo sin conexión y comparar UTC con host/manager.

## Instalación del agente

Consultar la [guía oficial Windows](https://documentation.wazuh.com/current/installation-guide/wazuh-agent/wazuh-agent-package-windows.html) en el momento de ejecución. Referencia consultada 2026-09-25: **4.14.8-1**; versión instalada: **pendiente**. Usar el agente compatible con la release verificada del manager. Descargar MSI desde el enlace oficial, fuera de Git, durante mantenimiento. Comprobar firma, editor y hash; no ejecutar si la firma es inválida o el origen inesperado.

Abrir enrollment 1515 únicamente desde `10.10.10.30` en el manager. Para este único endpoint en red aislada, usar enrollment automático limitado por firewall durante la ventana inicial; documentar esta decisión y cerrar 1515 al terminar. Si el manager requiere contraseña/certificado, conservar esa protección y usar el mecanismo privado soportado; no incluir secretos en esta guía, comandos registrados o evidencias. Nunca mostrar `client.keys`.

Ejemplo **pendiente de ejecución**, desde la carpeta del MSI de la release ya verificada; [variables oficiales del instalador](https://documentation.wazuh.com/current/user-manual/agent/agent-enrollment/deployment-variables/deployment-variables-windows.html):

```powershell
$msi = (Resolve-Path '.\wazuh-agent-4.14.8-1.msi').Path
Get-AuthenticodeSignature -FilePath $msi | Select-Object Status, SignerCertificate
Get-FileHash -LiteralPath $msi -Algorithm SHA256
$install = Start-Process msiexec.exe -ArgumentList @('/i', ('"{0}"' -f $msi), '/qn', '/norestart', 'WAZUH_MANAGER="10.10.10.10"', 'WAZUH_REGISTRATION_SERVER="10.10.10.10"', 'WAZUH_AGENT_NAME="SOC-WIN11"') -Wait -PassThru
if ($install.ExitCode -notin @(0, 3010)) { throw "MSI falló: $($install.ExitCode)" }
# Si devuelve 3010, reiniciar normalmente y volver a abrir PowerShell.
Start-Service WazuhSvc
Get-Service WazuhSvc
Get-CimInstance Win32_Service -Filter "Name='WazuhSvc'" | Select-Object Name, State, StartMode, PathName
$agentRoot = 'C:\Program Files (x86)\ossec-agent'
(Get-Item "$agentRoot\wazuh-agent.exe").VersionInfo | Select-Object ProductVersion, FileVersion
Test-NetConnection 10.10.10.10 -Port 1514
```

Comprobar ruta del servicio antes de asumir `agentRoot`. El código MSI aceptado y un TCP abierto no demuestran enrollment. Revisar `ossec.log` privadamente, `sudo /var/ossec/bin/agent_control -l` en el manager y el endpoint `SOC-WIN11` en la lista de agentes del dashboard; conservar ID asignado real, versión, estado **Active** y último keepalive. No inventar `001` ni otro ID. Capturar pantalla sanitizada con su explicación. Cerrar la regla 1515 y comprobar continuidad por 1514.

El agente inicia tráfico **saliente** hacia 1514 y, durante enrollment, 1515. No necesita un listener entrante en Windows. Mantener todos los perfiles del firewall activos. Si la política local bloquea salida, añadir solo una excepción saliente TCP al manager privado para esos puertos, limitada al perfil/interfaz del lab y al binario instalado; retirar 1515 al terminar. No abrir 55000, 9200 ni desactivar firewall por fallos de conectividad.

Crear `SOC-WIN11-wazuh-agent`. Instalar/configurar [Sysmon](../configs/windows/sysmon/README.md), habilitar [PowerShell Script Block Logging](../configs/windows/powershell/logging.md) y fusionar [los cinco canales](../configs/windows/wazuh-agent/README.md). Conservar baseline de Security: inspeccionar `auditpol /get /category:*`; solo si falta auditoría de inicio de sesión exitoso, habilitar **Success** en Advanced Audit Policy → Logon/Logoff → Audit Logon mediante política local y registrar antes/después. No generar fallos de autenticación ni habilitar todas las subcategorías.

Verificar localmente los canales y crear el checkpoint `SOC-WIN11-sysmon-configured` después de que Sysmon acepte el XML. Hacer la [validación](telemetry-validation.md) con NAT retirado y archives listo. La snapshot final `SOC-WIN11-deliverable-1-validated` queda prohibida como afirmación de cierre hasta tener pruebas de las cinco fuentes.
