# Despliegue observado de SOC-WIN11

**Evidence Origin: Controlled Simulation.** Evidencia de ingeniería y validación benigna del laboratorio; sin incidentes ni ataques. La instalación comenzó el **2026-09-30**, desde `7124873`. Se reanudó el **2026-10-05**, en `fix/complete-deliverable-1`, desde `origin/main` actualizado (`de0d8b8`, que incluye `1df7bf9` y el PR #1), con árbol inicialmente limpio. La evidencia anterior se conserva; el nombre del commit de cierre anterior no acredita aceptación.

**DELIVERABLE 1 — COMPLETE.** Windows operativo y cinco fuentes con Local PASS + Wazuh PASS. Los antecedentes del 2026-09-30 describen la preparación; las observaciones nativas del 2026-10-05 describen el estado efectivo.

## Medio comprobado antes de crear la VM

| Propiedad | Observación |
| --- | --- |
| Archivo autorizado | `26200.6584.250915-1905.25h2_ge_release_svc_refresh_CLIENTENTERPRISEEVAL_OEMRET_x64FRE_en-us.iso` |
| Tamaño | 7 092 807 680 bytes |
| SHA-256 calculado | `a61adeab895ef5a4db436e0a7011c92a2ff17bb0357f58b13bbc4062e535e7b9` |
| Fin de verificación | `2026-09-30T19:32:17.853378+00:00` |
| Exclusión Git | `git check-ignore -v --no-index <nombre>` confirmó `.gitignore:29:*.iso` |
| Detección del medio | `VBoxManage unattended detect`: `Windows11_64`, `EnterpriseEval`, `10.0.26200.6584`, `en-US`, índice 1; instalación soportada |

La ISO permanece en Downloads, fuera del árbol de trabajo. El hash identifica el archivo proporcionado; no se ha cotejado con un hash firmado por Microsoft. La detección del medio no demuestra la edición/build finalmente instalada. No se utilizaron las ISO Consumer Editions ni Arch Linux.

## VM y método de instalación

| Propiedad | Observación en VirtualBox |
| --- | --- |
| Hipervisor | `7.2.14r174565` |
| Nombre / UUID | `SOC-WIN11` / `ade8db56-b2af-4370-af8a-abfa3de861bf` |
| CPU / memoria | 2 vCPU / 4096 MiB |
| Disco | VDI dinámico, capacidad 81920 MiB (80 GiB), UUID `aa01b5c7-a3c8-4a74-890e-ee2e56714db1` |
| Firmware / TPM configurados | EFI64 / TPM 2.0 |
| Secure Boot configurado | Microsoft KEK/DB y Oracle PK inscritos; `secureboot --enable` terminó con código 0; preparación histórica del 2026-09-30; confirmación nativa Windows true el 2026-10-05 |
| Gráficos | VBoxSVGA, 128 MiB, aceleración 3D desactivada |
| NIC inicial | NIC 1 Host-Only Network `SOC-LAB`, Intel PRO/1000; NIC 2–8 `none` |
| Integración | Portapapeles y drag-and-drop desactivados; sin carpetas compartidas ni acceso público |

Windows Setup arrancó a `2026-09-30T19:33:26.818Z`. Se usa un archivo de respuestas privado para la instalación normal en el disco nuevo de esta VM. Contraseña aleatoria de la cuenta ficticia `socadmin`, medios auxiliares y originales se conservan fuera de Git, en directorios privados. El inicio automático está limitado a la preparación inicial y el postinstall lo desactiva y retira su contraseña del registro.

**Hallazgo previo a la ejecución:** la plantilla `win_nt6_unattended.xml` instalada con VirtualBox contiene comandos `LabConfig/Bypass*` en Windows PE y specialize. Se retiraron ambos bloques en una copia privada **antes** de generar el medio auxiliar. Se inspeccionaron también los archivos generados: sin excepciones de CPU, RAM, almacenamiento, TPM ni Secure Boot. No se modificó la plantilla global de VirtualBox. Se conservaron las protecciones estándar y `ProtectYourPC=1`.

Referencia del método y NVRAM: [manual oficial de VirtualBox 7.2](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/vboxmanage.html), consultado el 2026-09-30. Una consulta de `SecureBoot` antes del primer arranque devolvió `VERR_PATH_NOT_FOUND`; esto no se presenta como comprobación del estado efectivo. Se confirmará desde Windows mediante `Confirm-SecureBootUEFI`.

## Capacidad y estado inicial del servidor

Host observado: 16 GiB, cuatro cores físicos/ocho lógicos; 163 GiB disponibles al comienzo. SOC-WAZUH se encontró detenido en estado `aborted`, con cambio de estado `2026-09-30T00:53:07Z`. Sus recursos permanecen en 4 vCPU / 8192 MiB y sus dos snapshots siguen presentes. No se restauró ni recreó el servidor. Durante la instalación inicial permaneció detenido. En la continuación del 2026-10-05 se verificó su salud junto con Windows antes de la ingestión.

Se recopilaron muestras UTC de `kern.memorystatus_vm_pressure_level`, `vm.memory_pressure`, `vm.swapusage` y VM en ejecución. La muestra a `2026-09-30T19:33:30Z` indica nivel **1**, swap usado **9708.50 MiB**, con solo SOC-WIN11 encendido. Swap acumulado no equivale a presión grave actual; en esa fecha no se había validado la carga conjunta.

## Paquetes preparados

Preparación histórica del 2026-09-30: descargas HTTPS oficiales almacenadas fuera de Git. Las firmas e instalaciones reales del 2026-10-05 se registran más abajo:

| Paquete | Bytes | SHA-256 |
| --- | --- | --- |
| `wazuh-agent-4.14.8-1.msi` | 5 943 296 | `a696449694e797b70cc16eddc95e52ef53e6ef97ff65c0b0b2b4d6b9e23b0885` |
| `Sysmon.zip` | 2 938 038 | `00ecf1b46aec99299d3ae0bca79dc621458bd014b20b509d7c5c8e8c8611aa54` |
| `Sysmon64.exe` extraído | 3 203 368 | `83d31f2478dc6716cfdbf69e5c384bf043072b5f0d8d7b2eea365f709fda4352` |

Fuentes: [despliegue oficial de Wazuh para Windows](https://documentation.wazuh.com/current/installation-guide/wazuh-agent/wazuh-agent-package-windows.html) y [Microsoft Sysinternals Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon). La configuración aplicada de Sysmon es el [XML existente del repositorio](../../configs/windows/sysmon/sysmonconfig.xml).

## Continuación observada el 2026-10-05

Se arrancaron las dos VM existentes, sin restaurarlas ni reinstalar Windows. Las comprobaciones se ejecutaron dentro del invitado con Windows PowerShell 5.1 elevado mediante UAC y una tarea temporal SYSTEM. UAC permanece habilitado; las credenciales se leen desde archivos privados del host y no se publican.

| Propiedad | Observación nativa |
| --- | --- |
| Edición | `Microsoft Windows 11 Enterprise Evaluation`; `EditionID=EnterpriseEval` |
| Versión / build | `25H2`, `10.0.26200`, UBR `6584`: `26200.6584` |
| Hostname | `SOC-WIN11` |
| CPU / RAM | Dos procesadores lógicos; CPU expuesta `Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz`; memoria física visible `4274917376` bytes; VirtualBox conserva 2 vCPU / 4096 MiB |
| Disco | GPT, `VBOX HARDDISK`, `85899345920` bytes |
| TPM | Presente, listo, habilitado y activado; `SpecVersion=2.0, 0, 1.83` |
| Secure Boot | `Confirm-SecureBootUEFI=True` |
| UAC / instalación | `EnableLUA=1`, `ConsentPromptBehaviorAdmin=5`; sin `LabConfig`; `AutoAdminLogon=0` |
| SOC-LAB | `10.10.10.30/24`, estado `Preferred`; loopback `127.0.0.1/8`; sin ruta IPv4 por defecto tras retirar NAT |
| Conectividad | Dos respuestas ICMP de `10.10.10.10` (3 y 15 ms); TCP/1514 accesible desde Windows |
| Firewall | Domain, Private y Public habilitados; ninguna protección se desactivó |
| Defender | Servicio, antivirus y protección en tiempo real activos; plataforma `4.18.26080.4`, motor `1.1.26080.3`, firmas `1.459.565.0`, actualizadas a `2026-10-05T05:59:12Z` |
| Licencia | Activación oficial completada; `LicenseStatus=1`, `GracePeriodRemaining=129594` minutos en la observación de mantenimiento |
| Wazuh Agent | MSI `4.14.8-1`, instalación con exit 0; producto/binarios `4.14.8`; servicio `WazuhSvc` Running/Auto; enrollment confirmado, ID `001`, ACTIVE en manager y Dashboard; conexión privada a TCP/1514 |
| Sysmon | Instalado `15.22`, Authenticode Valid; `Sysmon64` Running/Auto, Operational habilitado, configuración efectiva con SHA-256 idéntico al XML del repositorio |
| Zona de Windows | `Pacific Standard Time`, offset efectivo observado `-420` minutos; XML de eventos se correlacionó mediante `SystemTime` UTC, sin inferirlo desde el log local del agente |

`ProductName` del registro conserva el texto `Windows 10 Enterprise Evaluation`; la identificación de Windows 11 usa el Caption de `Win32_OperatingSystem`, la edición y el build observados. No se trata el texto heredado del registro como un cambio de sistema operativo.

La evaluación se encontró sin activar y Defender tenía firmas antiguas. Se habilitó NIC 2 NAT temporal después de un apagado limpio para la activación oficial y las actualizaciones de Microsoft. `Update-MpSignature` devolvió `0x80070652`; la comprobación posterior mostró la plataforma/motor/firmas actualizados y ningún proceso de mantenimiento seleccionado en ejecución. No se afirma que la orden fallida fuera exitosa. NIC 2 volvió a `none`, sin port forwarding. El medio auxiliar de instalación fue desmontado; originales, instaladores y credenciales siguen fuera de Git. No había reboot pendiente de CBS ni Windows Update en la comprobación de paquetes.

Wazuh MSI y Sysmon64 tienen firma Authenticode `Valid` y los SHA-256 de la tabla de paquetes. El XML copiado a Windows conserva exactamente el SHA-256 `cfbf327432a53d8edb3f18b281e233a47e62e5c41276f4395bee1482ea71cbdf` del archivo existente del repositorio. El formato XML no se usa como versión del binario.

Se creó, con Windows apagado limpiamente y sin RAM guardada, `SOC-WIN11-base-install`: UUID `90bb1641-7025-49a2-a5b0-5ba3ac260f2a`, `2026-10-05T19:09:50Z`. Representa Windows activado, protecciones comprobadas, SOC-LAB y NAT retirado, antes del agente y Sysmon. Después se confirmó `SOC-WIN11-wazuh-agent` (`73e66ce8-02f9-4241-836c-414246c5d18c`) con el agente ACTIVE observado antes de Sysmon. El registro completo de checkpoints está en el [índice de evidencia](README.md#snapshots).

SOC-WAZUH volvió a comprobarse con manager, indexer, dashboard y Filebeat activos. Dos arranques del manager agotaron su límite de 45 segundos; un override `TimeoutStartSec=180` permitió arrancarlo, sin cambiar versiones ni RAM. La suspensión del host pausó ambas VM (`HostSuspend`); se reanudaron y se corrigió el desfase observado del reloj Ubuntu antes de la ventana de eventos. La carga conjunta se ha observado con niveles de presión del host 1 y 2; son muestras puntuales, sin garantía de capacidad sostenida.

Las cinco cadenas tienen eventos locales y documentos Wazuh correlacionados, según sus fichas. Consultar la [matriz del entregable](../../docs/deliverables/deliverable-1.md#matriz-de-validación).

## Agente y Sysmon observados

El Dashboard mostró la fila `001`, `SOC-WIN11`, `10.10.10.30`, `v4.14.8`, `active` a `2026-10-05T19:35:30Z`: [captura original](windows-agent-dashboard.png) y [observación](windows-agent-dashboard.json). `agent_control` muestra dirección de enrollment `any`, mientras la fila y el peer TCP muestran `.30`; no son una prueba de cambio de IP. Se retiró la regla temporal de TCP/1515 y `<auth><disabled>yes</disabled>` quedó aplicado; TCP/1514 permanece limitado a Windows.

A `2026-10-05T19:41:52Z`, Sysmon confirmó servicio/canal y versión. El [resultado de instalación](sysmon-install-observed.txt) acepta schema `4.82`; el binario anuncia soporte `4.91`. El [volcado efectivo](sysmon-effective-observed.txt) registra el hash original, SHA256, ProcessCreate y NetworkConnect limitado a `10.10.10.`. Se transcodificó la salida nativa UTF-16LE a UTF-8 sin cambiar su contenido. El comentario de ejecución pendiente que conserva el XML es histórico; la evidencia efectiva está aquí. El primer intento de la envoltura PowerShell se detuvo por un banner en stderr antes de instalar; la ejecución corregida comprobó los códigos de salida.

El agente fusionó los cinco `localfile` únicos como `eventchannel`, `only-future-events=yes`, sin XPath, conservando Application, active-response y los demás módulos. Configuración efectiva SHA-256: `74bbb6bbc891147f076d4137fd15f1ffb36ac3c07141c544acc75b270a66a903`. El log mostró las cinco suscripciones y conexión al manager a `2026-10-05T19:42:28Z` (hora local Windows `12:42:28`, UTC−07:00). Esto prepara la cadena; la recepción por evento se comprobó en las fichas.

## Cierre operativo

Se ejecutaron Security → System → Sysmon → PowerShell → Defender, todas con evento local y documento Wazuh correlacionado. PowerShell Script Block Logging quedó habilitado; el Quick Scan de Defender terminó manteniendo RTP activo. [Revisión final Windows](windows-final-checks.json), [salud conjunta](operational-final-checks.json) y [sesión archives cerrada](telemetry-session.json). Las cinco suscripciones se conservan; la tarea SYSTEM y scripts auxiliares temporales se retiraron.

[Snapshots reales](deliverable-1-snapshots.json): base, agente, Sysmon y checkpoints finales de ambas VM. Todos se crearon con apagado limpio, sin RAM guardada; ningún disco/ISO/snapshot se añade a Git. Tras arrancar se volvió a comprobar la salud y el agente ACTIVE.
