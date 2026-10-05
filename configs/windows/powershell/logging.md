# Windows PowerShell Script Block Logging

**Estado: procedimiento preparado — REQUIRES MANUAL EXECUTION.** Destino: Windows PowerShell 5.1 de SOC-WIN11 y canal `Microsoft-Windows-PowerShell/Operational`. PowerShell 7 usa otra configuración/canal y no sustituye esta comprobación.

## Configuración

Tras el snapshot previo, inspeccionar y guardar privadamente la política existente. En `gpedit.msc`: Computer Configuration → Administrative Templates → Windows Components → Windows PowerShell → **Turn on PowerShell Script Block Logging: Enabled**. Dejar sin marcar el registro de inicio/fin de invocaciones. No activar transcripción ni Module Logging para esta base. No cambiar ExecutionPolicy.

Alternativa de registro soportada para el endpoint autónomo, desde Windows PowerShell elevado; usar **una** vía de administración y registrar cuál se eligió:

```powershell
$policyPath = 'HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging'
if (Test-Path $policyPath) { Get-ItemProperty -LiteralPath $policyPath }
# Guardar el estado anterior antes de ejecutar las dos líneas siguientes.
New-Item -Path $policyPath -Force | Out-Null
New-ItemProperty -Path $policyPath -Name EnableScriptBlockLogging -PropertyType DWord -Value 1 -Force
Get-ItemProperty -LiteralPath $policyPath -Name EnableScriptBlockLogging
wevtutil gl Microsoft-Windows-PowerShell/Operational
```

Si el canal está deshabilitado, registrar el estado anterior y habilitarlo con `wevtutil sl Microsoft-Windows-PowerShell/Operational /e:true`. Abrir una **nueva** sesión de Windows PowerShell. Generar únicamente `Get-Date`, `Get-Process` o el marcador de la [guía de validación](../../../docs/telemetry-validation.md). Buscar el ID de referencia **4104** y el texto real; todavía no hay un 4104 observado. La salida de `Get-Date` en consola no prueba que exista el evento.

Fuentes: [registro de Windows PowerShell](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_logging?view=powershell-5.1) y [política ADMX](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowspowershell).

## Volumen y privacidad

Se registrará el contenido de bloques de script, incluidos argumentos que podrían contener credenciales. Usar exclusivamente cuentas y datos ficticios. Los originales quedan privados, tanto en Windows como en archives/indexer; revisar cada extracto antes de Git. La invocación detallada genera más volumen y no se necesita aquí. Medir eventos/minuto y crecimiento durante la ventana; no estimar una tasa como si fuera observada.

Protected Event Logging se evaluó: el cifrado puede requerir descifrado privado antes de analizar el texto. Esta etapa diagnóstica aislada utiliza contenido benigno sin secretos y no habilita esa integración ni afirma validarla. Antes de usar scripts reales o sensibles, diseñar el manejo de certificados y verificar su compatibilidad con el pipeline; nunca guardar claves privadas en Git.

Registrar tamaño máximo/retención del canal con `Get-WinEvent -ListLog 'Microsoft-Windows-PowerShell/Operational'`. No borrar registros para bajar volumen. Para revertir un cambio fallido, restaurar el valor previo mediante la misma vía (política o registro); si no existía, retirar solo el valor creado. No eliminar toda la rama PowerShell ni una política administrada.
