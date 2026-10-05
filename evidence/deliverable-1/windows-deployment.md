# Despliegue observado de SOC-WIN11

**Evidence Origin: Controlled Simulation.** Evidencia de ingeniería y validación benigna del laboratorio; sin incidentes ni ataques. Continuación de la fase B el **2026-09-30**, desde `7124873`, en `feat/deliverable-1-wazuh-windows`, con árbol inicialmente limpio. La evidencia de la fase A se conserva.

**DELIVERABLE 1 — IN PROGRESS.** Instalación iniciada; aún no hay resultados de las cinco fuentes. Los resultados siguientes distinguen configuración del hipervisor de comprobaciones dentro de Windows.

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
| Secure Boot configurado | Microsoft KEK/DB y Oracle PK inscritos; `secureboot --enable` terminó con código 0; confirmación nativa Windows pendiente |
| Gráficos | VBoxSVGA, 128 MiB, aceleración 3D desactivada |
| NIC inicial | NIC 1 Host-Only Network `SOC-LAB`, Intel PRO/1000; NIC 2–8 `none` |
| Integración | Portapapeles y drag-and-drop desactivados; sin carpetas compartidas ni acceso público |

Windows Setup arrancó a `2026-09-30T19:33:26.818Z`. Se usa un archivo de respuestas privado para la instalación normal en el disco nuevo de esta VM. Contraseña aleatoria de la cuenta ficticia `socadmin`, medios auxiliares y originales se conservan fuera de Git, en directorios privados. El inicio automático está limitado a la preparación inicial y el postinstall lo desactiva y retira su contraseña del registro.

**Hallazgo previo a la ejecución:** la plantilla `win_nt6_unattended.xml` instalada con VirtualBox contiene comandos `LabConfig/Bypass*` en Windows PE y specialize. Se retiraron ambos bloques en una copia privada **antes** de generar el medio auxiliar. Se inspeccionaron también los archivos generados: sin excepciones de CPU, RAM, almacenamiento, TPM ni Secure Boot. No se modificó la plantilla global de VirtualBox. Se conservaron las protecciones estándar y `ProtectYourPC=1`.

Referencia del método y NVRAM: [manual oficial de VirtualBox 7.2](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/vboxmanage.html), consultado el 2026-09-30. Una consulta de `SecureBoot` antes del primer arranque devolvió `VERR_PATH_NOT_FOUND`; esto no se presenta como comprobación del estado efectivo. Se confirmará desde Windows mediante `Confirm-SecureBootUEFI`.

## Capacidad y estado inicial del servidor

Host observado: 16 GiB, cuatro cores físicos/ocho lógicos; 163 GiB disponibles al comienzo. SOC-WAZUH se encontró detenido en estado `aborted`, con cambio de estado `2026-09-30T00:53:07Z`. Sus recursos permanecen en 4 vCPU / 8192 MiB y sus dos snapshots siguen presentes. No se restauró ni recreó el servidor. Se mantiene detenido durante la instalación inicial de Windows; su salud debe comprobarse de nuevo antes de la ingestión.

Se recopilan muestras UTC de `kern.memorystatus_vm_pressure_level`, `vm.memory_pressure`, `vm.swapusage` y VM en ejecución. La muestra a `2026-09-30T19:33:30Z` indica nivel **1**, swap usado **9708.50 MiB**, con solo SOC-WIN11 encendido. Swap acumulado no equivale a presión grave actual; todavía no se ha validado la carga conjunta.

## Paquetes preparados

Descargas HTTPS oficiales, almacenadas fuera de Git; todavía **sin instalar ni comprobar firma dentro de Windows**:

| Paquete | Bytes | SHA-256 |
| --- | --- | --- |
| `wazuh-agent-4.14.8-1.msi` | 5 943 296 | `a696449694e797b70cc16eddc95e52ef53e6ef97ff65c0b0b2b4d6b9e23b0885` |
| `Sysmon.zip` | 2 938 038 | `00ecf1b46aec99299d3ae0bca79dc621458bd014b20b509d7c5c8e8c8611aa54` |
| `Sysmon64.exe` extraído | 3 203 368 | `83d31f2478dc6716cfdbf69e5c384bf043072b5f0d8d7b2eea365f709fda4352` |

Fuentes: [despliegue oficial de Wazuh para Windows](https://documentation.wazuh.com/current/installation-guide/wazuh-agent/wazuh-agent-package-windows.html) y [Microsoft Sysinternals Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon). La configuración de Sysmon será el [XML existente del repositorio](../../configs/windows/sysmon/sysmonconfig.xml).

## Validación pendiente

Windows edition/version/build, IP dentro del invitado, Defender, Firewall, agente, Sysmon, snapshots base/agente y las cinco cadenas de eventos siguen pendientes. No se marca PASS por la creación de la VM ni por descargar paquetes. Consultar la [matriz del entregable](../../docs/deliverables/deliverable-1.md#matriz-de-validación).
