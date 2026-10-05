# Despliegue observado de SOC-WAZUH

**Evidence Origin: Controlled Simulation.** Evidencia de ingeniería del laboratorio, sin incidente ni simulación de ataque. Recopilación del **2026-09-26 al 2026-09-29**, con horas en UTC.

**SOC-WAZUH instalado y comprobado en SOC-LAB, sin NAT.** Manager, indexer, dashboard y Filebeat activos; indexer y dashboard devuelven `green`. Al cierre de esta fase A (2026-09-29), las fuentes Windows estaban **NOT EXECUTED**. Es un registro histórico. La [validación del 2026-10-05](README.md) completa las cinco cadenas y documenta el estado actual.

## Procedencia y Git

Se continuó en `feat/deliverable-1-wazuh-windows` desde `858c39c74e26e179ad9f92347495b2f1c3462bbb`, con árbol limpio y la historia anterior conservada. Se añadieron únicamente `*.vbox`, `*.vbox-prev` y `*.sav` al `.gitignore` mediante el commit separado `e5747210f381dd2705813b67a0fb11e55d652d20`, `chore: ignore VirtualBox runtime artifacts`. Las exclusiones de ISO y discos virtuales ya existían; se verificaron con `git check-ignore --no-index`. Al reanudar el 28 de septiembre, HEAD seguía en ese commit y el árbol estaba limpio.

Los originales, archivos de autoinstall, credenciales, claves SSH, logs completos, medios y VM permanecen fuera del repositorio. Los resultados publicados se limitan a extractos revisados; no se publican contraseñas ni claves privadas. Se conserva el [preflight histórico](preflight.md).

## Medio autorizado

| Propiedad | Observación |
| --- | --- |
| Archivo proporcionado | `ubuntu-24.04.5-live-server-amd64.iso` |
| Tamaño observado | 4 080 486 400 bytes |
| SHA-256 calculado | `97f3d7ffb032c3eb3b23d2c8be9cc76e60c2c1f2c0146ba5ba9fe01cafae0fd8` |
| Cotejo | Coincide con el archivo y hash publicados en [SHA256SUMS oficial de Ubuntu 24.04](https://releases.ubuntu.com/24.04/SHA256SUMS), consultado el 2026-09-26 |
| Procedencia local | ISO del directorio Downloads indicado por el propietario; ruta personal omitida de la evidencia pública |

Se utilizó esa ISO sin moverla ni modificarla. VirtualBox generó un medio auxiliar privado con respuestas de instalación. No se descargaron ISO alternativas. La comparación se hizo contra el listado oficial obtenido por HTTPS; no se presenta como verificación de una firma GPG.

## VM y Ubuntu observados

| Propiedad | Valor observado |
| --- | --- |
| Hipervisor | VirtualBox `7.2.14r174565` |
| VM / UUID | `SOC-WAZUH` / `84dacd9b-058d-4ae1-a37d-09d3b364cb0f` |
| CPU / RAM | 4 vCPU / 8192 MiB, sin reducción |
| Disco | VDI `Standard`, asignación dinámica, capacidad VirtualBox 81920 MiB (80 GiB); `lsblk` devuelve `80G` |
| SO instalado | `/etc/os-release`: `Ubuntu 24.04.5 LTS`; no inferido del nombre de la ISO |
| Arquitectura / kernel | `uname -r -m`: `6.8.0-142-generic x86_64` |
| Hostname | `hostname`: `SOC-WAZUH` |
| NIC 1 | Host-Only Network existente `SOC-LAB`; interfaz Ubuntu `lab0`, MAC `08:00:27:ee:62:1f` |
| IP del lab | `10.10.10.10/24`, estática por Netplan; persistió tras reiniciar |
| Host administrador | `bridge100`, `10.10.10.1/24`, observado al arrancar la VM |
| NIC 2 durante instalación | NAT temporal, sin port forwarding; Ubuntu `uplink0`, `10.0.3.15/24` por DHCP |

La instalación desatendida usó el disco de esta VM nueva. No se modificaron otras VM ni SOC-LAB. Se mantuvieron clipboard y drag-and-drop desactivados. La administración por SSH usa clave pública, `PasswordAuthentication no` y cuenta `socadmin`; la contraseña de consola/sudo está en almacenamiento privado. Root quedó bloqueado.

`apt-get update`, `apt-get -y upgrade` y `apt-get check` finalizaron con código 0 el 2026-09-26. No había reinicio requerido; se realizó apagado limpio para el snapshot base y se arrancó de nuevo. `systemctl --failed --no-pager` mostró cero unidades fallidas. La hora del invitado estaba sincronizada, zona `Etc/UTC`.

## Red y firewall

Se verificó `10.10.10.10/24` dentro del invitado, además de la configuración VirtualBox. `lab0` no tiene gateway ni DNS externo. La ruta por defecto durante descargas pertenece exclusivamente al adaptador NAT temporal.

UFW observado: **active**, política de entrada **deny**, salida **allow**, tráfico enrutado **disabled**, `IPV6=yes`. Reglas aplicadas en `lab0`:

| Destino | Origen permitido | Motivo |
| --- | --- | --- |
| `10.10.10.10:22/TCP` | `10.10.10.1` | Administración SSH desde el host |
| `10.10.10.10:443/TCP` | `10.10.10.1` | Dashboard desde el host |
| `10.10.10.10:1514/TCP` | `10.10.10.30` | Comunicación del futuro agente Windows; sin agente desplegado todavía |

No se abrió 1515: el enrollment queda pendiente de Windows. Tampoco se abrieron 55000, 9200, puertos de clúster ni syslog. Reenvío IPv4/IPv6 observado en **0 tanto en Ubuntu como en macOS**.

El **2026-09-29** se retiró el adaptador NAT (`nic2="none"`) con la VM apagada y se comprobó el arranque. La única ruta IPv4 del invitado es `10.10.10.0/24 dev lab0 ... src 10.10.10.10`; no hay ruta por defecto. IPv6 solo tiene loopback y link-local, sin ruta por defecto. No se configuró port forwarding ni interfaz puente hacia la red física.

Listeners observados: SSH `22`, dashboard `443`, manager `1514`, enrollment `1515` y API `55000`; estos últimos siguen sujetos a UFW. Indexer `9200` y transporte interno `9300` escuchan en loopback. No se desplegó un clúster multinodo. Las pruebas TCP desde `10.10.10.1`, con límite de tres segundos y sin payload de aplicación, conectaron a **22/443** y obtuvieron **TIMEOUT en 1514/1515/55000/9200/9300**. Un timeout por sí solo no demuestra la causa: aquí se contrasta con listeners, reglas y rutas. No se probó 1514 desde Windows porque ese endpoint no existe.

## Instalación Wazuh

El [Quickstart oficial](https://documentation.wazuh.com/current/quickstart.html) y las [releases oficiales](https://documentation.wazuh.com/current/release-notes/index.html), comprobados nuevamente el 2026-09-28, mantienen **4.14.8** como referencia consultada. Se ejecutó el asistente all-in-one de `https://packages.wazuh.com/4.14/wazuh-install.sh` con `-a`, sin clúster multinodo.

Hash observado del asistente descargado por HTTPS, idéntico en host e invitado: `9adb693c474317644358fef74e629b0fab782bcb9c1a411e967a8348e3830bc1`. Este hash identifica el archivo utilizado; no se presenta como firma del proveedor. Inicio observado: `2026-09-28T17:43:42Z`.

El asistente terminó con **código 0 a `2026-09-28T17:56:31Z`**. Las comprobaciones siguientes se ejecutaron independientemente de ese resultado, y se repitieron después del arranque sin NAT.

| Componente | Versión de paquete observada con `dpkg-query` | Servicio |
| --- | --- | --- |
| Wazuh Manager | `4.14.8-1` | `active (running)`, `enabled` |
| Wazuh Indexer | `4.14.8-1` | `active (running)`, `enabled` |
| Wazuh Dashboard | `4.14.8-1` | `active (running)`, `enabled` |
| Filebeat | `7.10.2-2` | `active (running)`, `enabled` |

Se ejecutaron `systemctl status --no-pager --lines=0` y `systemctl is-active` para los cuatro servicios. `wazuh-control info` devuelve `WAZUH_VERSION="v4.14.8"`, `WAZUH_REVISION="rc2"` y `WAZUH_TYPE="server"`; se conserva ese metadato literalmente, además de la versión del paquete oficial. No se deduce la versión instalada de la guía ni del resultado HTTP de compatibilidad.

`filebeat test config` devolvió `Config OK` y `filebeat test output` confirmó conexión, validación de cadena TLS, handshake TLSv1.2 y comunicación con el indexer. El `7.10.2` que devuelve esa prueba es la respuesta de compatibilidad del servidor, no la versión del paquete Wazuh Indexer.

La consulta local autenticada con certificado administrativo a `/_cluster/health` devolvió **green**, **un nodo** y **cero shards sin asignar**. El dashboard respondió a una consulta HTTP autenticada a `/api/status` desde el host por SOC-LAB con **HTTP 200 / green**. Su respuesta identifica el núcleo OpenSearch Dashboards `2.19.6`; el paquete Wazuh Dashboard es `4.14.8-1`. Esto prueba la respuesta de la aplicación; no se presenta como captura visual ni como agente Windows activo.

`wazuh-control status` devuelve **1** porque también comprueba procesos opcionales no ejecutándose: clusterd, maild, agentlessd, integratord y csyslogd. Se verificó `cluster/disabled=yes`, `email_notification=no` y ausencia de secciones agentless, integration y syslog_output. Los procesos centrales están en ejecución; no se activaron funciones fuera de alcance para convertir ese código en 0. `systemctl --failed` no mostró unidades fallidas. `agent_control -l` mostró únicamente **ID 000, SOC-WAZUH, Active/Local**: es el propio servidor, no un endpoint Windows.

El log del asistente, su archivo de credenciales y certificados privados permanecen fuera de Git. Se deshabilitó únicamente la entrada APT de Wazuh, conforme al Quickstart, para realizar upgrades coordinados; las fuentes y mecanismos de actualización de Ubuntu se conservaron. Al no haber salida a Internet, las próximas actualizaciones y sincronización externa requieren una ventana de mantenimiento con NAT temporal controlado. No se habilitaron archives ni reglas personalizadas.

## TLS y reloj

El certificado efectivo procede de `/etc/wazuh-dashboard/certs/wazuh-dashboard.pem`, obtenido de la configuración instalada. SAN observado: **127.0.0.1**. Huella SHA-256: `adc44d0d936d2513d6a0ec517dad064f22392751c73002f2a9dba23da2fa66b8`.

Se copió únicamente la CA pública al almacenamiento privado del host por SSH con clave de servidor verificada. `curl --cacert ... --connect-to 127.0.0.1:443:10.10.10.10:443` conectó por la IP del lab, validando la CA y la identidad incluida en el certificado; devolvió `ssl_verify_result=0`. Otra conexión TLS verificó la cadena y permitió comparar la huella del certificado recibido con la calculada dentro del invitado: **coinciden**. No se utilizó `curl -k`, ni se desactivó TLS permanentemente.

El acceso directo en navegador a `https://10.10.10.10` presenta la limitación real del certificado de laboratorio: CA privada y SAN de loopback. Se debe comprobar la huella antes de una excepción específica del navegador, como contempla el Quickstart. No se instaló confianza global en el host ni se afirma haber emitido un certificado para `10.10.10.10`.

Después de retirar NAT se comparó el reloj UTC de Ubuntu con el punto medio de una consulta SSH desde macOS: **invitado − host = −1.634 s**, incertidumbre aproximada **±0.379 s**, recopilado a `2026-09-29T17:00:04.176584+00:00`. Es una medición del desfase, no una garantía de sincronización futura. Registrar nuevamente el desfase y sincronizar durante mantenimiento antes de correlacionar eventos Windows; no se añadió un gateway para mantener NTP externo durante aislamiento.

## Snapshots confirmados

| Nombre | UUID | UTC | Estado y alcance |
| --- | --- | --- | --- |
| `SOC-WAZUH-base-install` | `e0d50517-8586-4723-9224-28e68578d9ee` | `2026-09-26T19:44:39Z` | VM apagada limpiamente; Ubuntu actualizado, IP/firewall observados, antes de instalar Wazuh; incluye NAT temporal |
| `SOC-WAZUH-wazuh-operational` | `914fc1c2-0c02-41c4-980e-b8c8481217ab` | `2026-09-29T17:01:25Z` | VM apagada limpiamente tras comprobar servicios, TLS, aplicación y red; NAT retirado; sin estado de RAM guardado |

Existencia confirmada con `VBoxManage snapshot SOC-WAZUH list --machinereadable`; timestamps contrastados con el registro de snapshots de VirtualBox. No se creó el checkpoint de entregable validado. Restaurar el checkpoint base también restaura su configuración con NAT temporal y sin Wazuh: no confundirlo con el checkpoint operativo.

Después del snapshot operativo se arrancó la VM y se volvió a comprobar salud nativa a `2026-09-29T17:04:52Z`: cuatro servicios activos, indexer green y cero unidades fallidas. El dashboard autenticado respondió nuevamente HTTP 200 / green a `2026-09-29T17:11:39.618773+00:00`, con TLS y huella comprobados. A `2026-09-29T17:12:12.276321+00:00`, VirtualBox indicó `running`, NIC 2–8 `none` y SOC-WIN11 no registrado.

## Artefactos publicados

Todos son texto, **Evidence Origin: Controlled Simulation**, sin incidente asociado. Horas originales y de recopilación en UTC; el invitado estaba sincronizado en el registro base y el desfase posterior al aislamiento se midió por separado. Los originales privados se conservan fuera de Git. No se publicaron capturas.

| Archivo / localizador | Recopilación UTC | Método y transformación |
| --- | --- | --- |
| [ubuntu-native-base.txt](ubuntu-native-base.txt) | `2026-09-26T19:44:13Z` | Salidas nativas de SO, hostname, kernel, CPU, memoria, disco y reloj antes de Wazuh. Selección de bloques completos del inventario Ubuntu; red temporal y bloques ajenos al objetivo omitidos; espacios finales retirados. |
| [wazuh-native-health.txt](wazuh-native-health.txt) | `2026-09-29T17:04:52Z` | Comandos y códigos de salida dentro de SOC-WAZUH, por SSH con clave de host verificada. `systemctl status` limitado a unidad, Loaded, Active, Process y Main PID; omitidos CGroup, argumentos JVM y contadores accesorios. Encabezado de `dpkg-query` normalizado para mostrar escapes/comillas; resultados intactos; espacios finales retirados. |
| [wazuh-dashboard-check.json](wazuh-dashboard-check.json) | `2026-09-29T17:11:39.618773+00:00` | Consulta autenticada `/api/status` desde host; selección de versión del núcleo y estado, sin respuesta completa ni credenciales. `curl_verification` contiene, en orden, HTTP status, `ssl_verify_result` e IP local. Huella del certificado recibido cotejada con el certificado nativo; CA y nombre validados como se explica en TLS. |
| [wazuh-host-checks.json](wazuh-host-checks.json) | `2026-09-29T17:00:04.176584+00:00` | Resultados TCP sobre puertos requeridos y comparación de reloj por SSH desde host, después de retirar NAT y antes del snapshot. No es prueba desde Windows ni prueba de ingestión. |
| [wazuh-virtualbox.json](wazuh-virtualbox.json) | `2026-09-29T17:12:12.276321+00:00` | Selección de `showvminfo`, `showmediuminfo`, snapshots, presencia de SOC-WIN11 y contadores sysctl del host. Fechas de snapshots leídas del XML VirtualBox; rutas personales y nombres de otras VM omitidos. |

[SHA256SUMS](SHA256SUMS) identifica exactamente estas cinco copias publicadas, después de sanitizar. Verificación desde este directorio: `shasum -a 256 -c SHA256SUMS`. Los hashes permiten detectar cambios en los extractos; no certifican por sí solos su procedencia. Las versiones de herramientas y componentes están registradas arriba y en los archivos correspondientes.

## Problemas realmente observados

1. **Autoinstall rechazó tres comandos UFW.** YAML interpretó `on` sin comillas como booleano. Se entrecomilló ese argumento en las tres listas, se reinició el instalador y la validación/instalación continuaron. El medio auxiliar fue reinsertado después de su expulsión por Ubuntu al apagar; la ISO original permaneció intacta.
2. **SSH inicialmente inaccesible después del reinicio.** El 2026-09-28 la consola mostró `lab0` configurada y enrutable con la IP correcta. Un ping desde Ubuntu a `10.10.10.1` devolvió 3/3 respuestas; después, macOS resolvió ARP y SSH funcionó. No se cambiaron Netplan ni UFW. La causa subyacente no quedó demostrada; no se atribuye a Wazuh, aún sin instalar en ese momento.
3. **VM encontrada en estado `aborted` al reanudar.** VirtualBox registró `SIGTERM (15)` en la ejecución anterior; no se determinó quién originó la terminación. Se arrancó la VM existente, sin restaurar ni recrear el disco. Ubuntu no mostró unidades fallidas en la comprobación posterior.
4. **Advertencia de postinst de AppArmor durante actualización.** Se observó `Illegal number: yes`; la actualización y `dpkg --audit` terminaron sin paquetes pendientes de configurar, `apparmor` estaba activo y `aa-status --enabled` devolvió 0. No se deshabilitó AppArmor ni se atribuyó una causa no comprobada.
5. **Estado guardado de VirtualBox no restaurable el 2026-09-29.** La VM estaba `saved`; tanto headless como GUI fallaron con `VERR_SSM_DATA_UNIT_FORMAT_CHANGED` al cargar `vga`, con la misma versión VirtualBox y VMSVGA/16 MiB. Antes de retirar ese estado de la VM activa se clonaron por APFS configuración, discos y `.sav` en almacenamiento privado: nueve archivos con tamaños e inodos independientes comprobados, y hashes coincidentes de `.sav`/`.vbox`. Se conservó esa copia, se arrancó desde el disco existente y Wazuh volvió a pasar las comprobaciones. No se reinstaló Ubuntu ni Wazuh. Se prefiere apagado limpio y snapshots sin RAM mientras no se resuelva la causa del error de restauración; no se atribuye a presión de memoria.

El lector Python HTTPS del host no pudo verificar la cadena del servidor al descargar una copia de referencia del asistente; `/usr/bin/curl` sí completó la descarga con validación TLS. Posteriormente, el verificador estricto de Python rechazó la CA privada generada por Wazuh por falta de extensión Key Usage; la comprobación con curl y LibreSSL validó cadena, identidad y huella como se describe arriba. No se desactivó TLS para descargar software ni para validar el dashboard. Una consulta inicial del certificado usó un nombre de archivo incorrecto; se corrigió leyendo la ruta efectiva del dashboard.

## Capacidad y límites

Se conservaron los 8 GiB de la VM. Se observaron niveles normales **1** y picos transitorios **2** de `kern.memorystatus_vm_pressure_level`; durante la instalación hubo un timeout SSH que desapareció en la siguiente comprobación. A `2026-09-29T17:00:04Z` el nivel era **1** y swap usado **7333.75 MiB**. No se redujeron recursos ni se cerraron aplicaciones del propietario sin identificar su uso. Estas lecturas corresponden a **una** VM; no validan la carga conjunta de Wazuh y Windows. El indicador `vm.memory_pressure` y swap son medidas auxiliares, no sustituyen el nivel de presión del sistema.

La última muestra publicada del host, a `2026-09-29T17:12:12.276321+00:00`, mantuvo nivel **1**, con swap usado **6201.00 MiB**. Son mediciones puntuales, no una prueba de capacidad simultánea ni garantía de presión futura.

Requisito pendiente al 2026-09-29: Windows 11 Enterprise Evaluation 25H2 x64 ISO path still required. Fue resuelto en la fase B enlazada arriba.

Estado histórico al 2026-09-29: no se había creado SOC-WIN11 ni usado la ISO Consumer Editions; las cinco fuentes estaban sin ejecutar y el entregable IN PROGRESS. El [cierre real del 2026-10-05](../../docs/deliverables/deliverable-1.md) registra Windows y la telemetría completados.
