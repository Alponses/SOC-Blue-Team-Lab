# Preflight observado del host

Recopilación: **2026-09-25**, referencia de reloj observada `2026-09-25T19:13:42Z` mediante `date -u`. Resume comandos ejecutados en el host macOS de este checkout durante la misma sesión. No representa estado de invitados ni eventos Windows. Se omiten UUID, rutas personales y nombres de VM ajenas al entregable; no se modificaron esas VM.

| Comando ejecutado | Resultado observado | Límite |
| --- | --- | --- |
| `git status --porcelain=v1` | Sin salida antes de cambios | Árbol inicial limpio |
| `git branch --show-current` | `feat/deliverable-1-wazuh-windows` | Rama ya existente; no se recreó |
| `git rev-parse HEAD` | `1e9b9f1891534727b1ef87ee3bc882f0eb4dae96` | Base exacta de Deliverable 0.5 |
| `git show --no-patch 1e9b9f1` | `docs: extend SOC lab with isolated Internet honeypot architecture` | Commit confirmado; no modificado |
| `uname -srm` | `Darwin 22.6.0 x86_64` | Kernel/arquitectura del host |
| `VBoxManage --version` | `7.2.14r174565` | CLI disponible |
| `VBoxManage list vms` | Dos VM ajenas al alcance; ninguna SOC-WAZUH/SOC-WIN11 | No prueba ausencia de archivos sin registrar en todo el disco |
| `VBoxManage list runningvms` | Sin salida | Ninguna VM de esta instancia en ejecución |
| `VBoxManage list hostonlynets` | SOC-LAB Enabled, máscara 255.255.255.0, LowerIP 10.10.10.1, UpperIP 10.10.10.9, hostonly-SOC-LAB | Reserva de host; no son leases ni IP de invitados observadas |
| `VBoxManage list hostonlyifs` | Sin salida | Host-Only Network registrada; interfaz activa/IP del host por verificar al conectar invitados |
| `VBoxManage list dhcpservers` | Un DHCP para vboxnet0 en otra subred; ninguno SOC-LAB listado | No se cambió la red ajena; verificar DHCP efectivo al desplegar |
| `VBoxManage list dvds` | Solo medio registrado ajeno a Ubuntu/Windows | Medios necesarios todavía no proporcionados |
| `sysctl hw.memsize hw.physicalcpu hw.logicalcpu` | 17179869184 bytes, 4 cores físicos, 8 lógicos | 16 GiB totales; no RAM libre medida |
| `sysctl net.inet.ip.forwarding` | 0 | Reenvío IPv4 del host desactivado; no acredita todo el aislamiento |
| `df -h .` | 228 GiB disponibles en volumen del checkout | Fotografía de capacidad, no reserva de espacio |
| `python3 scripts/validate_repository.py` antes de cambios | CORRECTO: 355 enlaces, 52 Markdown | Enlaces locales; no infraestructura |
| `git diff --check` antes de cambios | Sin errores | Sin cambios todavía |

Se buscaron medios/VM por extensión en el directorio del lab, Downloads y VirtualBox VMs; no se encontró Ubuntu Server 24.04, Windows 11 ni las dos VM requeridas en ese alcance. No se afirma que no existan en otros lugares. Se solicitaron al propietario las rutas de medios/VM existentes; no se recibieron rutas durante la preparación inicial.

## Consecuencia operativa

La asignación prevista consume 12 GiB de los 16 GiB de RAM total y 160 GB virtuales, antes de overhead/snapshots. Cerrar cargas no necesarias y medir memoria libre/presión antes de arrancar ambas VM. La compatibilidad CPU/TPM/UEFI de Windows 11, medios/licencia y capacidad efectiva siguen pendientes; no se ha probado que la combinación funcione.

No se iniciaron instalaciones, snapshots, pruebas de conectividad a los invitados ni pruebas de eventos. Las IP `10.10.10.10` y `.30` son asignaciones documentadas, no direcciones comprobadas en hosts operativos. **REQUIRES MANUAL EXECUTION** para despliegue y validación.

## Reanudación desde 23d9614

Nueva comprobación del **2026-09-25**, referencia UTC observada `2026-09-25T20:49:12Z`. Conserva los resultados históricos anteriores; los siguientes corresponden a la continuación del entregable.

| Comprobación ejecutada | Resultado observado |
| --- | --- |
| Git antes de editar | Árbol limpio; rama `feat/deliverable-1-wazuh-windows`; HEAD `23d96144fe71e07502190fc867b26d59ebe69fba`; `1e9b9f1` conservado |
| Documentación/scripts | Revisadas guías existentes, informe, evidencia y `scripts/validate_repository.py`; no hay scripts de instalación de VM en el alcance revisado |
| VirtualBox | `7.2.14r174565`; ninguna VM ejecutándose; SOC-WAZUH y SOC-WIN11 siguen sin registrar |
| SOC-LAB | Enabled, máscara `255.255.255.0`, rango reservado del host `.1–.9`; no se modificó |
| Medios registrados | Solo una ISO ajena a Ubuntu/Windows |
| Búsqueda local | `rg --files --hidden --no-ignore` por extensiones ISO/VM en Downloads, Desktop, Documents y VirtualBox VMs; comprobación adicional de directorios convencionales ISO/ISOs/isos/VMs y `/Users/Shared` cuando existen: ningún medio requerido encontrado |
| Volúmenes montados | Solo `Macintosh SSD` listado; no apareció un volumen externo de medios |
| Recursos | 16 GiB RAM total, 4 cores físicos/8 lógicos y 228 GiB de disco disponibles |
| Memoria sin invitados | `sysctl vm.memory_pressure` devolvió `0`; `vm_stat` mostró 480419 páginas de 4096 bytes ocupadas por el compresor; no se probó carga conjunta de las VM |
| Forwarding IPv4 del host | `net.inet.ip.forwarding: 0` |
| Validador antes de editar | 423 enlaces internos / 68 Markdown, sin errores; `git diff --check` sin errores |

**Bloqueo confirmado:** faltan ambas ISO dentro del alcance inspeccionado. Se detuvo la creación de infraestructura de ambas VM por instrucción del propietario. No se descargaron ISO, crearon discos/VM/snapshots ni ejecutaron instalaciones o pruebas de telemetría. No se afirma ausencia de los medios en ubicaciones no inspeccionadas.

Medios que se requieren, sin ruta local conocida:

- **Ubuntu Server 24.04 LTS AMD64, Live Server ISO**, desde [releases oficiales de Ubuntu 24.04](https://releases.ubuntu.com/24.04/); seleccionar la imagen server AMD64 y cotejar `SHA256SUMS` del proveedor.
- **Windows 11 Enterprise Evaluation 25H2 x64 ISO**, desde [Microsoft Evaluation Center](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-11-enterprise); seleccionar Enterprise 25H2 x64, no Arm64 ni LTSC.

El [índice oficial Wazuh](https://documentation.wazuh.com/current/release-notes/index.html) consultado sigue encabezado por 4.14.8 y el [Quickstart](https://documentation.wazuh.com/current/quickstart.html) mantiene el asistente 4.14. No hay versión instalada que registrar. La referencia Sysmon 15.22 indicada por el propietario tampoco es una versión instalada observada.

La presión de memoria debe medirse nuevamente antes y durante la validación real; esta lectura sin VM no demuestra capacidad suficiente. Se mantienen los 8 GiB de SOC-WAZUH y 4 GiB de SOC-WIN11. No se prepara commit de cierre mientras falte evidencia operativa.
