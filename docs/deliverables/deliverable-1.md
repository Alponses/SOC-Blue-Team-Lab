# Entregable 1 — Wazuh y telemetría Windows

**DELIVERABLE 1 — IN PROGRESS**

Revisión: 2026-09-25. Configuraciones y procedimientos escritos en Git; infraestructura y telemetría **REQUIRES MANUAL EXECUTION**. No hay pruebas de ingestión ni versiones instaladas observadas. El entregable 0.5 sigue cerrado y su arquitectura se conserva.

**Continuación desde `23d9614`:** se revalidaron rama, commit y árbol limpio, VirtualBox y SOC-LAB. La [nueva comprobación de medios](../../evidence/deliverable-1/preflight.md#reanudación-desde-23d9614) no encontró ninguna de las dos ISO requeridas. Se detuvo la creación de ambas VM; ningún servicio, agente o snapshot nuevo existe como resultado de esta sesión. La validación futura seguirá Security → System → Sysmon → PowerShell → Defender, documentando el resultado de cada fuente antes de continuar. No se crea un commit de cierre sin despliegue y evidencia reales.

## Base y alcance

Se verificaron árbol limpio, rama `feat/deliverable-1-wazuh-windows` ya existente y HEAD exacto `1e9b9f1891534727b1ef87ee3bc882f0eb4dae96`, mensaje `docs: extend SOC lab with isolated Internet honeypot architecture`. No se trabajó en main ni se reescribió historia. Se prepara un commit de fundamento, no un cierre operativo.

Solo SOC-WAZUH + SOC-WIN11 + agente Wazuh + Sysmon + Defender + Security/System/PowerShell. No se desplegó honeypot, Linux endpoint, AD, Suricata, AWS ni Splunk. No se ejecutaron ataques, malware/EICAR, Atomic Red Team, phishing o fuerza bruta; no se añadieron detecciones ni se cerró SOC-001–SOC-015.

## Infraestructura

| Elemento | Diseño conservado | Estado observado |
| --- | --- | --- |
| Host | macOS x86_64, VirtualBox | Darwin 22.6.0; VBox 7.2.14r174565; 16 GiB RAM total, 4 cores físicos/8 lógicos, 228 GiB libres al inspeccionar |
| SOC-LAB | Host-only `10.10.10.0/24`, host reservado `.1` | Red registrada y Enabled; interfaz activa, dirección efectiva del host y aislamiento completo aún pendientes |
| SOC-WAZUH | `10.10.10.10`, Ubuntu Server 24.04 LTS, 4 vCPU / 8 GiB / 80 GB | VM no registrada en la instancia inspeccionada; SO/recursos/IP no aplicados ni observados |
| SOC-WIN11 | `10.10.10.30`, Windows 11 Enterprise evaluación, 2 vCPU / 4 GiB / 80 GB | VM no registrada; Windows/recursos/IP no aplicados ni observados |

Evidencia: [preflight real](../../evidence/deliverable-1/preflight.md). Hay recursos totales identificados, no una prueba de capacidad simultánea. Medios, compatibilidad Windows 11 y acceso a invitados pendientes. El propietario eligió usar medios/VM existentes, pero aún no proporcionó sus rutas. No se descargaron imágenes ni se crearon VM vacías.

## Versiones

| Componente | Referencia consultada o elección | Exacta instalada/observada |
| --- | --- | --- |
| Ubuntu Server | 24.04 LTS x86_64 | No instalada/observada; revisión ISO y kernel pendientes |
| Wazuh manager/indexer/dashboard | Documentación oficial consultada 2026-09-25: 4.14.8, asistente rama 4.14 | Ninguna; registrar paquete y revisión por componente al instalar |
| Filebeat | Versión compatible provista por instalación Wazuh | No observada |
| Windows 11 | Enterprise Evaluation 25H2 x64 solicitada; requisitos estándar | Build/edición exacta no observadas |
| Wazuh agente Windows | Referencia oficial consultada: 4.14.8-1 | No observado |
| Sysmon | Microsoft Sysinternals; referencia solicitada 15.22; XML schema 4.82 | Binario no observado; schema no es versión del producto |
| Defender | Debe permanecer activo | Estado, motor/plataforma/firmas no observados |

Fuentes/versionado en [instalación Wazuh](../wazuh-installation.md) y [Windows](../windows11-installation.md). Verificar release vigente al ejecutar; no confundir una consulta documental con instalación.

## Matriz de validación

`No verificado` significa que no se ejecutó la comprobación, no que se haya demostrado ausencia de eventos. Cada fuente usa `eventchannel`; ninguna ha sido aplicada en un agente real.

| Fuente | Evento local | Agente recoge | Manager recibe | Indexer/Discover | Campos validados | Estado / evidencia |
| --- | --- | --- | --- | --- | --- | --- |
| Security | No verificado | No verificado | No verificado | No verificado | Ninguno | REQUIRES MANUAL EXECUTION — [ficha](../../evidence/deliverable-1/security.md) |
| System | No verificado | No verificado | No verificado | No verificado | Ninguno | REQUIRES MANUAL EXECUTION — [ficha](../../evidence/deliverable-1/system.md) |
| Sysmon | No verificado | No verificado | No verificado | No verificado | Ninguno | REQUIRES MANUAL EXECUTION — [ficha](../../evidence/deliverable-1/sysmon.md) |
| PowerShell | No verificado | No verificado | No verificado | No verificado | Ninguno | REQUIRES MANUAL EXECUTION — [ficha](../../evidence/deliverable-1/powershell.md) |
| Defender | No verificado | No verificado | No verificado | No verificado | Ninguno | REQUIRES MANUAL EXECUTION — [ficha](../../evidence/deliverable-1/defender.md) |

La [guía de validación](../telemetry-validation.md) define actividad benigna, observación local, correlación por identidad del evento, recepción e índice/consulta. Archives será temporal y acotado para encontrar eventos normales sin requerir alertas; no se ha habilitado aún. No hay screenshots ni JSON observados de estas fuentes.

## Criterios de aceptación operativa

- [ ] SOC-WAZUH instalado con versión exacta de SO y paquetes registrada.
- [ ] Manager, indexer, dashboard y Filebeat funcionando; TLS/salud comprobados.
- [ ] Aislamiento de ambas VM y reglas de firewall verificadas; NAT retirado y enrollment cerrado tras uso.
- [ ] SOC-WIN11 operativo, build/hostname/recursos/IP verificados; Defender y Windows Firewall activos.
- [ ] Agente instalado, servicio corriendo, enrolado y Active en manager/dashboard con ID real.
- [ ] Sysmon instalado con XML aceptado, versión/configuración efectiva registradas y eventos locales/de Wazuh correlacionados.
- [ ] Security: evento local y documento Wazuh correlacionados.
- [ ] System: evento local y documento Wazuh correlacionados.
- [ ] PowerShell: política efectiva, comando benigno, evento local y documento Wazuh correlacionados.
- [ ] Defender: evento operacional local y documento Wazuh correlacionados.
- [ ] Campos, ausencias, tiempos/desfase, consultas y volumen observados documentados.
- [ ] Evidencia operativa sanitizada con hashes, snapshots reales y cierre de archives registrados.

Ningún criterio operativo se marca por tener un archivo de configuración escrito. Un agente Active tampoco completa la cadena.

## Cambios del repositorio

Archivos nuevos:

- `configs/windows/README.md`.
- `configs/windows/wazuh-agent/README.md` y `ossec.conf.example`.
- `configs/windows/sysmon/README.md` y `sysmonconfig.xml`.
- `configs/windows/powershell/logging.md`.
- `configs/wazuh/README.md`.
- `docs/wazuh-installation.md`, `docs/windows11-installation.md`, `docs/telemetry-validation.md` y este informe.
- `evidence/deliverable-1/README.md`, `preflight.md`, `security.md`, `system.md`, `sysmon.md`, `powershell.md` y `defender.md`.

Archivos existentes actualizados: `README.md`, `configs/README.md`, `docs/implementation-checklist.md` y `docs/lab-operations.md`, para enlazar el progreso real. Los documentos de cierre 0.5, arquitectura, honeypot, incidentes y reglas permanecen preservados.

## Validación del repositorio

Comprobaciones ejecutadas en macOS el 2026-09-25 sobre los cambios preparados:

| Comprobación | Resultado y alcance |
| --- | --- |
| `python3 scripts/validate_repository.py` | CORRECTO: 423 enlaces internos en 68 Markdown; incluye rutas y anclas |
| XML con `xml.etree.ElementTree` | Ambos archivos bien formados; cinco canales únicos `eventchannel`, manager privado TCP/1514 y filtros Sysmon acotados comprobados |
| Markdown | Enlaces y pares de bloques de código comprobados; no se ejecutó un linter externo ni se validó visualmente toda la representación |
| `git diff --check` y `git diff --cached --check` | Sin errores de whitespace |
| Revisión de secretos | Revisión manual y búsqueda de patrones en los 22 archivos cambiados: sin coincidencias de claves privadas, access keys AWS, tokens GitHub/JWT, credenciales en URL o secretos XML |
| Archivos nuevos y diff completo | Revisados; 18 archivos nuevos y cuatro modificados, solo texto UTF-8, ninguno mayor de 1 MiB |
| Artefactos y alcance | Sin binarios, ISO, discos/snapshots, logs completos ni credenciales añadidos; arquitectura, cierre 0.5, incidentes, honeypot y detecciones preservados |
| Git | Rama y base correctas; cambios preparados revisados antes del commit; sin merge, push ni modificación de historia previa |

La revisión de secretos es acotada al contenido preparado y sus patrones; no es una auditoría exhaustiva del historial ni de datos privados fuera de Git. La comprobación inicial, antes de editar, había pasado con 355 enlaces / 52 Markdown.

Las pruebas nativas de configuración Wazuh/Sysmon, servicios y PowerShell son **REQUIRES MANUAL EXECUTION**. Un parser XML en macOS solo confirma estructura y propiedades inspeccionadas; no valida el esquema del binario ni el funcionamiento del agente.

## Problemas encontrados

1. **No están registradas las dos VM requeridas.** Se comprobó por inventario VirtualBox; no se atribuye a un fallo de Wazuh o Windows. Hace falta proporcionar medios/VM existentes e instalar o registrar los invitados.
2. **No se localizaron medios adecuados en el alcance inspeccionado.** Solo apareció un medio registrado ajeno al entregable y archivos de otras VM. Se solicitaron rutas concretas; su ausencia impide avanzar al despliegue con la opción elegida por el propietario.

No se han encontrado errores de ingestión porque esa prueba no se ejecutó. Los diagnósticos de la guía son procedimientos, no incidentes fabricados.

## Pendientes y siguiente paso

Proporcionar rutas de medios/VM, verificar compatibilidad/capacidad efectiva, instalar las dos VM, aplicar configuraciones, crear snapshots y recoger evidencia de las cinco fuentes. Documentar versiones exactas y actualizar la matriz. Hasta entonces: **DELIVERABLE 1 — IN PROGRESS**.

Después de cerrar 1, el alcance propuesto de **Deliverable 2** sigue siendo SOC-LINUX `10.10.10.40`: Ubuntu, OpenSSH, agente Wazuh, autenticación/sudo/sistema y baseline FIM con actividad normal. La fuerza bruta corresponde a una etapa posterior. Deliverable 2 no se ha iniciado.
