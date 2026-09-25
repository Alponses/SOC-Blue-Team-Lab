# Instalación de SOC-WAZUH

**Estado: REQUIRES MANUAL EXECUTION.** No hay VM SOC-WAZUH registrada en el VirtualBox inspeccionado. Esta guía contiene pasos pendientes, no resultados. Véase [preflight observado](../evidence/deliverable-1/preflight.md) e [informe](deliverables/deliverable-1.md).

## Plataforma y versiones

Conservar `SOC-WAZUH`, Ubuntu Server **24.04 LTS x86_64**, `10.10.10.10/24`, **4 vCPU / 8 GiB / 80 GB** de disco virtual de la arquitectura. Los 80 GB superan el mínimo pedido y permiten algo de margen para logs; no garantizan retención. Solo un nodo con manager, indexer y dashboard; Filebeat completa el transporte al indexer.

Consulta oficial del **2026-09-25**: [Quickstart](https://documentation.wazuh.com/current/quickstart.html) admite Ubuntu 24.04 y publica el asistente de la rama 4.14; las [notas 4.14.8](https://documentation.wazuh.com/current/release-notes/release-4-14-8.html) y el instalador Windows consultado indican **4.14.8**. Es la versión de referencia consultada, **no una versión instalada**. Volver a comprobar Quickstart y las notas al ejecutar; si cambia la release, usar la vigente compatible para componentes centrales y agente, registrar URL, fecha, revisión y versión exacta. La [compatibilidad oficial](https://documentation.wazuh.com/current/upgrade-guide/index.html) exige versiones centrales idénticas, incluido patch, y manager igual o posterior al agente; para indexer 4.14.8 indica Filebeat-OSS 7.10.2.

## VM, red y snapshot previo

1. Usar los medios Ubuntu proporcionados por el propietario desde [Ubuntu Server](https://ubuntu.com/download/server), con checksum oficial verificado. Guardarlos fuera del repositorio. Registrar versión exacta de la ISO.
2. Crear la VM en VirtualBox con los recursos anteriores y adaptador **Host-Only Network SOC-LAB** existente; no recrear la red. No seleccionar red puente ni NAT Network. Comprobar el tipo real de adaptador en `VBoxManage showvminfo SOC-WAZUH --machinereadable`.
3. Configurar IP estática `10.10.10.10/24` en la interfaz del lab, sin gateway ni DNS externo. No apuntar a `10.10.10.20`: AD/DNS aún no existe. Utilizar consola y direcciones IP en esta etapa.
4. Si hace falta Internet para instalación/actualizaciones, añadir NAT temporal sin port forwarding. Anotar interfaz, rutas y horario. El tráfico Windows → Wazuh siempre usa las IP del lab. Retirar ese adaptador antes de la validación.
5. Instalar Ubuntu, actualizaciones y hora, comprobar CPU/RAM/disco. Crear `SOC-WAZUH-base-install` **antes** de instalar Wazuh. Usar [registro de snapshots](../evidence/deliverable-1/README.md#snapshots); un nombre sugerido no demuestra creación.

Comprobaciones a guardar sanitizadas, con fecha UTC:

```sh
date -u
hostnamectl
cat /etc/os-release
lscpu
free -h
df -h
ip -brief address
ip route
ip -6 route
timedatectl status
```

Comprobar además el reenvío IPv4/IPv6 en host e invitados, ausencia de Internet Sharing, rutas por VPN y port forwarding. La presencia de SOC-LAB no prueba aislamiento completo. Medir desfase horario respecto al host; sincronizar durante mantenimiento y comprobarlo tras cada snapshot. Registrar incertidumbre si se comparan relojes manualmente.

## Exposición mínima

Puertos contrastados con la [arquitectura oficial Wazuh](https://documentation.wazuh.com/current/getting-started/architecture.html). Todos TCP salvo donde se indica:

| Servicio | Puerto | Origen permitido en esta etapa | Tratamiento |
| --- | --- | --- | --- |
| Agente → manager | 1514 | SOC-WIN11 `10.10.10.30` | Permanente en la interfaz privada |
| Enrollment | 1515 | SOC-WIN11 `10.10.10.30` | Abrir solo para enrollment; cerrar después |
| Dashboard HTTPS | 443 | Host administrador `10.10.10.1` | Solo lab; confirmar primero la IP real del host |
| SSH opcional | 22 | Host administrador `10.10.10.1` | Solo si se usa; consola disponible |
| API manager | 55000 | Componentes dentro de SOC-WAZUH | Sin regla de acceso desde otras máquinas |
| API indexer | 9200 | Componentes dentro de SOC-WAZUH | Sin regla de acceso desde otras máquinas |
| Clúster manager / indexer | 1516 / 9300–9400 | Ninguno externo | No abrir; no desplegar clúster multinodo |
| Syslog / agente UDP | 514 TCP/UDP / 1514 UDP | Ninguno | No necesarios ni habilitados para esta ruta |

En la consola Ubuntu, identificar primero el nombre real de la interfaz privada mediante `ip -brief address`. Propuesta UFW para VM nueva, antes de instalar servicios; revisar reglas existentes, no ejecutar `ufw reset`:

```sh
read -r -p 'Interfaz verificada de SOC-LAB: ' lab_if
test -n "$lab_if" || exit 1
ip address show dev "$lab_if"
sudo ufw status verbose
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow in on "$lab_if" from 10.10.10.30 to 10.10.10.10 port 1514 proto tcp
sudo ufw allow in on "$lab_if" from 10.10.10.30 to 10.10.10.10 port 1515 proto tcp
sudo ufw allow in on "$lab_if" from 10.10.10.1 to 10.10.10.10 port 443 proto tcp
# Solo si se administrará por SSH; omitir si se usa consola:
# sudo ufw allow in on "$lab_if" from 10.10.10.1 to 10.10.10.10 port 22 proto tcp
sudo ufw enable
sudo ufw status verbose
```

Confirmar que UFW filtra IPv6 (`IPV6=yes`), ausencia de otras reglas amplias y ausencia de ruta externa durante pruebas. La salida temporal permitida facilita descargas; la retirada del NAT y del gateway devuelve el aislamiento previsto. No exponer ningún servicio por túneles públicos, router doméstico o reglas NAT. Registrar listeners con `sudo ss -lntup` y probar los accesos desde el origen autorizado, no asumir que UFW garantiza toda la topología.

## Instalación oficial

En directorio privado de SOC-WAZUH, fuera del checkout. Comprobar de nuevo la URL oficial. Estas órdenes representan la referencia vigente consultada; no son constancia de ejecución:

```sh
umask 077
mkdir -p "$HOME/wazuh-install-private"
cd "$HOME/wazuh-install-private"
curl --fail --show-error --location -o wazuh-install.sh https://packages.wazuh.com/4.14/wazuh-install.sh
sha256sum wazuh-install.sh
less wazuh-install.sh
sudo bash ./wazuh-install.sh -a
```

El hash local identifica el artefacto descargado; no equivale por sí solo a cotejar una firma del proveedor. Registrar la procedencia HTTPS y comprobar cualquier firma/checksum oficial disponible. No ejecutar el asistente en macOS, en otra VM ni sobre una instalación existente sin revisar su estado.

El instalador muestra credenciales y produce `wazuh-install-files.tar`. Conservarlos privados y con acceso restringido; no capturar la pantalla con contraseñas ni pegar la salida completa en Git. No ejecutar una orden que imprima contraseñas como evidencia. Revisar y cambiar credenciales iniciales mediante la guía oficial antes de uso continuado.

## Verificación posterior

```sh
dpkg-query -W -f='${Package}\t${Version}\n' wazuh-manager wazuh-indexer wazuh-dashboard filebeat
sudo /var/ossec/bin/wazuh-control info
systemctl is-active wazuh-manager wazuh-indexer wazuh-dashboard filebeat
sudo /var/ossec/bin/wazuh-control status
sudo ss -lntup
sudo ufw status verbose
sudo filebeat test config
sudo filebeat test output
```

Guardar versiones exactas y resultados de **cada** servicio; leer `journalctl -u <servicio>` y logs privados si falla. Abrir `https://10.10.10.10` desde el host por SOC-LAB, verificar la huella/cadena del certificado por consola y entrar privadamente. No usar desactivación permanente de validación TLS. Verificar salud del indexer desde la interfaz autenticada; en un nodo, un estado amarillo puede deberse a réplicas sin asignar: investigar, no equipararlo automáticamente a pérdida de ingestión ni cambiar réplicas sin comprobarlo.

Seguir la recomendación del Quickstart de deshabilitar únicamente el repositorio Wazuh tras instalar para evitar actualizaciones accidentales de componentes, conservando las actualizaciones de Ubuntu. Programar revisión y upgrades coordinados; no fijar una versión vulnerable indefinidamente.

Crear `SOC-WAZUH-wazuh-operational` solo tras comprobar servicios y acceso. Aplicar [archives temporales](../configs/wazuh/README.md), instalar/enrolar el [endpoint](windows11-installation.md) y verificar [las cinco fuentes](telemetry-validation.md). Una vez enrolado, retirar la regla 1515 correspondiente con `ufw delete` usando exactamente sus parámetros originales; comprobar que el agente sigue activo por 1514. Reabrir de forma limitada solo cuando se necesite reenrollment.

No publicar configuración completa de Filebeat, archivos del keystore, API, claves, certificados privados o exportaciones del manager. El [registro de evidencia](../evidence/deliverable-1/README.md) distingue configuración de servicio observado.
