# Entregable 1 — Wazuh y telemetría Windows

**DELIVERABLE 1 — IN PROGRESS**

Revisión: **2026-09-30**. **Fase A: SOC-WAZUH instalado y comprobado**, con versiones, servicios, red aislada y snapshots observados. La [fase B de SOC-WIN11](../../evidence/deliverable-1/windows-deployment.md) está en ejecución: medio verificado, VM creada e instalación iniciada. Sus cinco fuentes siguen **NOT EXECUTED**. No hay prueba de ingestión Windows. El entregable 0.5 sigue cerrado y su arquitectura se conserva.

**Histórico:** la [comprobación desde `23d9614`](../../evidence/deliverable-1/preflight.md#reanudación-desde-23d9614) se detuvo por falta de medios. Posteriormente, el propietario proporcionó la ISO Ubuntu y autorizó únicamente la fase A desde `858c39c`. Se creó el commit separado `e574721` para exclusiones VirtualBox y se ejecutó el [despliegue real de SOC-WAZUH](../../evidence/deliverable-1/wazuh-deployment.md). La ISO Windows Consumer Editions fue excluida; no se creó SOC-WIN11. La futura validación seguirá Security → System → Sysmon → PowerShell → Defender. No se crea el commit de cierre del entregable mientras falten esas pruebas.

## Base y alcance

Al preparar el fundamento se verificaron árbol limpio, rama `feat/deliverable-1-wazuh-windows` ya existente y HEAD exacto `1e9b9f1891534727b1ef87ee3bc882f0eb4dae96`, mensaje `docs: extend SOC lab with isolated Internet honeypot architecture`. No se trabajó en main ni se reescribió historia. El fundamento quedó registrado en `23d9614`; esta continuación conserva esa historia e incorpora la fase B desde `7124873`.

Solo SOC-WAZUH + SOC-WIN11 + agente Wazuh + Sysmon + Defender + Security/System/PowerShell. No se desplegó honeypot, Linux endpoint, AD, Suricata, AWS ni Splunk. No se ejecutaron ataques, malware/EICAR, Atomic Red Team, phishing o fuerza bruta; no se añadieron detecciones ni se cerró SOC-001–SOC-015.

## Infraestructura

| Elemento | Diseño conservado | Estado observado |
| --- | --- | --- |
| Host | macOS x86_64, VirtualBox | VBox 7.2.14r174565; 16 GiB RAM total, 4 cores físicos/8 lógicos; 170 GiB libres al reanudar el 2026-09-29; presión normal con picos transitorios documentados |
| SOC-LAB | Host-only `10.10.10.0/24`, host `.1` | Red reutilizada; host `bridge100=10.10.10.1/24`, Ubuntu `lab0=10.10.10.10/24`; NAT retirado, sin ruta por defecto en el invitado; forwarding IPv4/IPv6 desactivado |
| SOC-WAZUH | `10.10.10.10`, Ubuntu Server 24.04 LTS, 4 vCPU / 8 GiB / 80 GB | Ubuntu 24.04.5 LTS instalado; 4 vCPU, 8192 MiB, VDI dinámico de 81920 MiB; IP privada verificada; servicios y checkpoints comprobados |
| SOC-WIN11 | `10.10.10.30`, Windows 11 Enterprise evaluación, 2 vCPU / 4 GiB / 80 GB | VM creada: 2 vCPU, 4096 MiB, VDI dinámico 81920 MiB, EFI64/TPM 2.0; Windows en instalación, IP nativa pendiente |

Evidencia: [preflight histórico](../../evidence/deliverable-1/preflight.md) y [despliegue de SOC-WAZUH](../../evidence/deliverable-1/wazuh-deployment.md). La ISO Ubuntu proporcionada se cotejó con SHA256SUMS oficial. No se descargaron imágenes. La capacidad simultánea con Windows y sus requisitos/medio siguen pendientes; una prueba con Wazuh no valida dos VM.

## Versiones

| Componente | Referencia consultada o elección | Exacta instalada/observada |
| --- | --- | --- |
| Ubuntu Server | 24.04 LTS x86_64 | `/etc/os-release`: 24.04.5 LTS; kernel `6.8.0-142-generic x86_64` |
| Wazuh manager/indexer/dashboard | Release oficial revalidada 2026-09-28: 4.14.8, asistente 4.14 | Los tres paquetes `4.14.8-1`; servicios `active (running)` y `enabled` |
| Filebeat | Versión compatible provista por instalación Wazuh | Paquete `7.10.2-2`; servicio activo; configuración y salida TLS comprobadas |
| Windows 11 | Enterprise Evaluation 25H2 x64 solicitada; requisitos estándar | Build/edición exacta no observadas |
| Wazuh agente Windows | Referencia oficial consultada: 4.14.8-1 | No observado |
| Sysmon | Microsoft Sysinternals; referencia solicitada 15.22; XML schema 4.82 | Binario no observado; schema no es versión del producto |
| Defender | Debe permanecer activo | Estado, motor/plataforma/firmas no observados |

Fuentes/versionado en [instalación Wazuh](../wazuh-installation.md) y [Windows](../windows11-installation.md). Verificar release vigente al ejecutar; no confundir una consulta documental con instalación.

## Matriz de validación

Las cinco fuentes siguen **NOT EXECUTED**, sin cambios en sus fichas. `No verificado` significa que no se ejecutó la comprobación, no que se haya demostrado ausencia de eventos. Cada fuente usa `eventchannel`; ninguna ha sido aplicada en un agente real.

| Fuente | Evento local | Agente recoge | Manager recibe | Indexer/Discover | Campos validados | Estado / evidencia |
| --- | --- | --- | --- | --- | --- | --- |
| Security | No verificado | No verificado | No verificado | No verificado | Ninguno | REQUIRES MANUAL EXECUTION — [ficha](../../evidence/deliverable-1/security.md) |
| System | No verificado | No verificado | No verificado | No verificado | Ninguno | REQUIRES MANUAL EXECUTION — [ficha](../../evidence/deliverable-1/system.md) |
| Sysmon | No verificado | No verificado | No verificado | No verificado | Ninguno | REQUIRES MANUAL EXECUTION — [ficha](../../evidence/deliverable-1/sysmon.md) |
| PowerShell | No verificado | No verificado | No verificado | No verificado | Ninguno | REQUIRES MANUAL EXECUTION — [ficha](../../evidence/deliverable-1/powershell.md) |
| Defender | No verificado | No verificado | No verificado | No verificado | Ninguno | REQUIRES MANUAL EXECUTION — [ficha](../../evidence/deliverable-1/defender.md) |

La [guía de validación](../telemetry-validation.md) define actividad benigna, observación local, correlación por identidad del evento, recepción e índice/consulta. Archives será temporal y acotado para encontrar eventos normales sin requerir alertas; no se ha habilitado aún. No hay screenshots ni JSON observados de estas fuentes.

## Criterios de aceptación operativa

- [x] SOC-WAZUH instalado con versión exacta de SO y paquetes registrada.
- [x] Manager, indexer, dashboard y Filebeat funcionando; TLS/salud comprobados.
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

Fundamento ya registrado en Git (archivos creados entonces):

- `configs/windows/README.md`.
- `configs/windows/wazuh-agent/README.md` y `ossec.conf.example`.
- `configs/windows/sysmon/README.md` y `sysmonconfig.xml`.
- `configs/windows/powershell/logging.md`.
- `configs/wazuh/README.md`.
- `docs/wazuh-installation.md`, `docs/windows11-installation.md`, `docs/telemetry-validation.md` y este informe.
- `evidence/deliverable-1/README.md`, `preflight.md`, `security.md`, `system.md`, `sysmon.md`, `powershell.md` y `defender.md`.

Archivos existentes actualizados: `README.md`, `configs/README.md`, `docs/implementation-checklist.md` y `docs/lab-operations.md`, para enlazar el progreso real. Los documentos de cierre 0.5, arquitectura, honeypot, incidentes y reglas permanecen preservados.

La fase A añade el registro y los artefactos sanitizados de SOC-WAZUH en `evidence/deliverable-1/`, actualiza este informe, la guía Wazuh y los enlaces de estado en README, operaciones y checklist. Configuraciones Windows, fichas de las cinco fuentes, arquitectura e incidentes permanecen sin cambios.

Inventario de esta continuación respecto de HEAD `e574721`:

- Seis archivos modificados: `README.md`, `docs/deliverables/deliverable-1.md`, `docs/implementation-checklist.md`, `docs/lab-operations.md`, `docs/wazuh-installation.md` y `evidence/deliverable-1/README.md`.
- Siete archivos nuevos bajo `evidence/deliverable-1/`: `wazuh-deployment.md`, `ubuntu-native-base.txt`, `wazuh-native-health.txt`, `wazuh-dashboard-check.json`, `wazuh-host-checks.json`, `wazuh-virtualbox.json` y `SHA256SUMS`.
- `.gitignore` ya quedó registrado por separado en `e574721`; ningún archivo de VM o medio se añadió al repositorio.

## Validación del repositorio

Comprobaciones históricas del fundamento, ejecutadas en macOS el 2026-09-25:

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

Comprobaciones de la fase A ejecutadas el **2026-09-29**:

| Comprobación | Resultado y alcance |
| --- | --- |
| Validador del repositorio | CORRECTO: **439 enlaces internos / 69 archivos Markdown**, rutas y anclas; sin comprobación de URL externas ni renderizado Mermaid |
| Markdown y JSON | Bloques de código cerrados en siete Markdown modificados/nuevos; tres JSON de evidencia legibles; sin linter externo ni revisión visual completa |
| Whitespace | `git diff --check` y `git diff --cached --check`: sin errores; índice sin cambios staged |
| Hashes publicados | Los cinco archivos de `SHA256SUMS` coinciden con sus SHA-256; `shasum` emitió aviso de locale y usó C, con los cinco resultados OK |
| Secretos y artefactos | 13 archivos modificados/nuevos revisados; cotejo con diez credenciales privadas conocidas y siete clases de patrones: cero hallazgos. Solo UTF-8, sin NUL ni archivos mayores de 1 MiB; sin ISO, VM, binarios o credenciales añadidos |
| Alcance y exclusiones | Ocho extensiones requeridas ignoradas; cinco fichas Windows, matriz y arquitectura idénticas a HEAD; revisión completa de diff y archivos nuevos |
| Historia y árbol | Rama `feat/deliverable-1-wazuh-windows`, HEAD `e5747210f381dd2705813b67a0fb11e55d652d20`; `1e9b9f1`, `23d9614` y `858c39c` conservados como ancestros. Seis archivos modificados y siete nuevos revisados, aún sin commit; sin merge ni push |

La revisión de secretos está limitada a estos cambios y a los valores/patrones comprobados; no acredita ausencia universal de secretos. No se crea el commit de cierre de Deliverable 1 porque falta Windows y la validación de las cinco fuentes.

Las comprobaciones nativas del servidor Wazuh ya se ejecutaron y se enlazan en su evidencia. Las pruebas del agente Windows, Sysmon y PowerShell siguen **REQUIRES MANUAL EXECUTION**. El parser XML del fundamento solo comprobó estructura; no validó el funcionamiento de un endpoint.

## Problemas encontrados

La falta inicial de Ubuntu quedó resuelta al recibir la ISO correcta. Durante el despliegue se corrigió el entrecomillado YAML del autoinstall, se observó una interrupción inicial de conectividad sin pérdida de la IP estática, y se recuperó un estado guardado VirtualBox no restaurable mediante copia privada y arranque desde disco. Hubo picos transitorios de presión de memoria; no se redujeron recursos. El [registro técnico](../../evidence/deliverable-1/wazuh-deployment.md#problemas-realmente-observados) conserva pruebas, límites y causas que no pudieron establecerse.

No se han encontrado errores de ingestión Windows porque esa prueba no se ejecutó. El certificado generado identifica loopback; la evidencia documenta su validación y la limitación del acceso directo por IP en navegador. El reloj sin salida NTP externa requiere volver a medirse antes de correlacionar Windows.

## Pendientes y siguiente paso

**La fase B está en ejecución.** Medio Enterprise verificado antes de crear SOC-WIN11; instalación iniciada sin bypass de requisitos. [Observaciones reales](../../evidence/deliverable-1/windows-deployment.md).

La continuación de Deliverable 1 requiere terminar Windows, comprobar capacidad conjunta, instalar agente, Sysmon y logging, y recoger evidencia local y Wazuh de cada fuente. No usar la ISO Consumer Editions. No hay cierre del entregable, ni merge ni push. **DELIVERABLE 1 — IN PROGRESS**.

Después de cerrar 1, el alcance propuesto de **Deliverable 2** sigue siendo SOC-LINUX `10.10.10.40`: Ubuntu, OpenSSH, agente Wazuh, autenticación/sudo/sistema y baseline FIM con actividad normal. La fuerza bruta corresponde a una etapa posterior. Deliverable 2 no se ha iniciado.
