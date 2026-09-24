# Lab Operations

Guía operativa para iniciar, verificar, utilizar y apagar el entorno
**SOC Blue Team Lab**.

> Este documento describe la operación del **Controlled Detection Lab**.
> No documenta el despliegue del futuro Internet Honeypot.

---

## 1. Propósito

El laboratorio utiliza virtualización local para ejecutar sistemas aislados
destinados a recopilación de telemetría, detección y análisis SOC.

Las máquinas físicas utilizadas para ejecutar VirtualBox funcionan únicamente
como **hosts de virtualización del laboratorio**.

No funcionan como servidores públicos.

Ningún servicio como Wazuh, Windows, Sysmon o futuros servicios internos del
laboratorio debe exponerse directamente a Internet desde la red doméstica.

La futura infraestructura pública del honeypot utilizará infraestructura
separada, como VPS o cloud, con controles independientes.

---

## 2. Modelo de despliegue

Topología prevista para el primer entregable:

```text
Host físico
    |
    └── VirtualBox
          |
          └── SOC-LAB
              10.10.10.0/24
                  |
                  ├── SOC-WAZUH
                  │   10.10.10.10
                  │
                  └── SOC-WIN11
                      10.10.10.30
```

### Función de cada sistema

| Sistema | Dirección | Función |
|---|---:|---|
| Host físico | `10.10.10.1` | Administración local del laboratorio |
| SOC-WAZUH | `10.10.10.10` | Wazuh Server, Indexer y Dashboard |
| SOC-DC01 | `10.10.10.20` | Reservado para Active Directory |
| SOC-WIN11 | `10.10.10.30` | Endpoint Windows monitorizado |
| SOC-LINUX | `10.10.10.40` | Reservado para endpoint Linux |
| SOC-SIM | `10.10.10.50` | Reservado para simulaciones controladas |

Solo `SOC-WAZUH` y `SOC-WIN11` forman parte del Entregable 1.

Los demás sistemas permanecen reservados hasta sus respectivos entregables.

---

## 3. Separación entre laboratorio local e infraestructura pública

El Controlled Detection Lab y el futuro Internet Honeypot son entornos
diferentes.

```text
CONTROLLED DETECTION LAB

Host físico
    |
    └── VirtualBox
          |
          └── SOC-LAB
              10.10.10.0/24
```

El laboratorio local no debe recibir conexiones iniciadas desde Internet.

El futuro honeypot utilizará un modelo separado:

```text
INTERNET
    |
    v
VPS / CLOUD
    |
    └── Honeypot
        |
        └── transporte controlado de evidencia
```

No se utilizará el siguiente modelo:

```text
INTERNET
    |
    v
Router doméstico
    |
    v
Host físico
    |
    v
Wazuh / Windows / laboratorio
```

No se configurarán port forwarding, DMZ doméstica ni exposición pública de
VirtualBox para publicar el laboratorio.

---

## 4. Red del laboratorio

La red privada del laboratorio es:

```text
Nombre:      SOC-LAB
Red:         10.10.10.0/24
Máscara:     255.255.255.0
Host:        10.10.10.1
```

VirtualBox utiliza una **Host-Only Network**.

Esto permite comunicación entre:

```text
Host <-> VM
VM   <-> VM
```

sin conectar directamente esa interfaz virtual a la red física externa.

### Configuración registrada en macOS

VirtualBox restringe por defecto determinados rangos utilizados por redes
Host-Only.

El rango utilizado por este laboratorio está autorizado mediante:

```text
/etc/vbox/networks.conf
```

Contenido:

```text
* 10.10.10.0/24
```

### Verificar la configuración

```bash
cat /etc/vbox/networks.conf
```

Resultado esperado:

```text
* 10.10.10.0/24
```

---

## 5. Verificar SOC-LAB

Ejecutar:

```bash
VBoxManage list hostonlynets
```

Debe existir una red equivalente a:

```text
Name:            SOC-LAB
State:           Enabled
NetworkMask:     255.255.255.0
LowerIP:         10.10.10.1
UpperIP:         10.10.10.9
VBoxNetworkName: hostonly-SOC-LAB
```

La red fue creada originalmente mediante:

```bash
VBoxManage hostonlynet add \
  --name=SOC-LAB \
  --netmask=255.255.255.0 \
  --lower-ip=10.10.10.1 \
  --upper-ip=10.10.10.9 \
  --enable
```

No es necesario volver a crearla cada vez que se inicia el laboratorio.

Antes de recrearla se debe verificar siempre si ya existe.

---

# Operación diaria

## 6. Antes de iniciar el laboratorio

### 6.1 Verificar VirtualBox

```bash
VBoxManage --version
```

La versión utilizada durante la creación inicial del laboratorio fue:

```text
7.2.14
```

Una versión diferente no implica automáticamente un problema, pero cualquier
cambio importante de versión deberá registrarse si afecta el funcionamiento
del laboratorio.

---

### 6.2 Verificar las máquinas disponibles

```bash
VBoxManage list vms
```

Una vez terminado el Entregable 1 deberán aparecer:

```text
SOC-WAZUH
SOC-WIN11
```

---

### 6.3 Verificar máquinas actualmente encendidas

```bash
VBoxManage list runningvms
```

Si el laboratorio está completamente apagado, el comando no debería mostrar
ninguna de sus VMs.

---

### 6.4 Verificar SOC-LAB

```bash
VBoxManage list hostonlynets
```

Confirmar que exista:

```text
SOC-LAB
```

y que esté habilitada.

---

## 7. Orden de encendido

El orden normal será:

```text
1. Host físico
2. VirtualBox / SOC-LAB
3. SOC-WAZUH
4. SOC-WIN11
5. Verificación de telemetría
```

El SIEM se inicia antes que los endpoints para que pueda recibir la
telemetría producida durante su arranque.

---

## 8. Encender SOC-WAZUH

Cuando la máquina exista:

```bash
VBoxManage startvm "SOC-WAZUH" --type headless
```

El modo `headless` permite ejecutar Wazuh sin mantener abierta una ventana
gráfica de VirtualBox.

Comprobar que esté ejecutándose:

```bash
VBoxManage list runningvms
```

Debe aparecer:

```text
SOC-WAZUH
```

---

## 9. Verificar SOC-WAZUH

Una vez instalado Wazuh deberán comprobarse:

```text
Wazuh Server
Wazuh Indexer
Wazuh Dashboard
```

Desde el propio servidor también se deberán comprobar sus servicios antes
de considerar disponible el SIEM.

Desde el host de administración:

```text
https://10.10.10.10
```

El Dashboard deberá ser accesible únicamente desde redes autorizadas del
laboratorio.

No debe publicarse directamente a Internet.

---

## 10. Encender SOC-WIN11

Cuando Wazuh esté disponible:

```bash
VBoxManage startvm "SOC-WIN11"
```

Windows se inicia con interfaz gráfica porque se utilizará como endpoint de
trabajo y análisis.

Comprobar:

```bash
VBoxManage list runningvms
```

Resultado esperado:

```text
SOC-WAZUH
SOC-WIN11
```

---

# Verificación del laboratorio

## 11. Verificar conectividad

Desde `SOC-WIN11`:

```powershell
ping 10.10.10.10
```

Desde `SOC-WAZUH`, cuando sea necesario:

```bash
ping 10.10.10.30
```

La respuesta ICMP dependerá también de las reglas de firewall configuradas.

La ausencia de respuesta ICMP no deberá utilizarse por sí sola como prueba de
que un servicio está caído.

---

## 12. Verificar agente Wazuh

Una vez instalado el agente de Windows, comprobar en el Wazuh Dashboard:

```text
Agents
└── SOC-WIN11
    └── Status: Active
```

Un agente con estado `Active` demuestra conectividad del agente, pero no
demuestra por sí solo que todos los canales requeridos estén siendo
recopilados.

---

## 13. Fuentes requeridas

El Entregable 1 deberá demostrar la llegada de información procedente de:

```text
SOC-WIN11
    |
    ├── Windows Security
    ├── Windows System
    ├── PowerShell Operational
    ├── Sysmon Operational
    └── Defender Operational
          |
          v
      Wazuh Agent
          |
          v
      SOC-WAZUH
```

Debe localizarse al menos un evento válido procedente de cada fuente.

---

## 14. Pruebas de telemetría

Antes de ejecutar escenarios ofensivos se utilizarán únicamente eventos
inocuos.

Ejemplos:

### Inicio de sesión

Realizar un inicio de sesión normal en Windows y comprobar el evento
correspondiente.

### PowerShell

```powershell
Write-Output "SOC-LAB-TEST-001"
```

### DNS

Cuando exista un resolvedor disponible:

```powershell
nslookup example.test
```

### Sistema

Identificar un evento normal generado por Windows System.

### Defender

Verificar un evento operacional legítimo manteniendo Microsoft Defender
habilitado.

No se utilizarán malware, exploits ni técnicas de evasión para completar
esta etapa.

---

# Acceso a Internet

## 15. Política de conectividad

La interfaz principal del laboratorio será:

```text
SOC-LAB
10.10.10.0/24
```

Esta red deberá mantenerse aislada.

Cuando una máquina necesite Internet exclusivamente para:

```text
actualizaciones
instalación de paquetes
descarga de dependencias oficiales
```

podrá utilizar temporalmente una segunda interfaz configurada con NAT.

Ejemplo conceptual:

```text
VM
├── NIC laboratorio -> SOC-LAB
└── NIC temporal    -> NAT
```

NAT no sustituye la interfaz SOC-LAB.

---

## 16. NAT temporal

Antes de habilitar acceso temporal:

1. verificar el estado de la VM;
2. documentar por qué necesita acceso;
3. comprobar que SOC-LAB continúa conectada;
4. realizar únicamente las descargas o actualizaciones necesarias;
5. comprobar servicios después de la actualización;
6. retirar o deshabilitar NAT cuando ya no sea necesario;
7. verificar nuevamente SOC-LAB.

La configuración exacta de los adaptadores se documentará durante el
despliegue de cada máquina virtual.

No se utilizará Bridged Networking para publicar servicios del laboratorio.

---

# Snapshots y recuperación

## 17. Cuándo crear snapshots

Crear snapshots antes de modificaciones relevantes como:

```text
instalación de Wazuh
instalación del agente
configuración de Sysmon
cambios relevantes de auditoría
cambios de reglas
actualizaciones importantes
simulaciones posteriores
```

---

## 18. Convención de nombres

Ejemplos:

```text
SOC-WAZUH-base-install
SOC-WAZUH-wazuh-operational
SOC-WIN11-clean-install
SOC-WIN11-wazuh-agent
SOC-WIN11-sysmon-configured
```

Los nombres deben representar claramente el estado recuperable.

---

## 19. Crear snapshot mediante CLI

Ejemplo:

```bash
VBoxManage snapshot "SOC-WAZUH" take "SOC-WAZUH-base-install"
```

Windows:

```bash
VBoxManage snapshot "SOC-WIN11" take "SOC-WIN11-clean-install"
```

---

## 20. Consultar snapshots

```bash
VBoxManage snapshot "SOC-WAZUH" list
```

o:

```bash
VBoxManage snapshot "SOC-WIN11" list
```

---

## 21. Uso de snapshots

Un snapshot no sustituye un backup.

Su objetivo dentro del laboratorio es permitir regresar rápidamente a un
estado conocido durante pruebas controladas.

Antes de restaurar uno:

1. identificar qué información se perderá;
2. detener la VM;
3. registrar el motivo;
4. restaurar el snapshot;
5. comprobar servicios;
6. comprobar fecha y hora;
7. comprobar conectividad;
8. comprobar nuevamente telemetría.

---

# Orden de apagado

## 22. Secuencia normal

El orden normal será:

```text
1. SOC-WIN11
2. SOC-WAZUH
3. VirtualBox
4. Host físico
```

Primero se apagan los endpoints.

El SIEM permanece disponible durante su apagado para recibir los últimos
eventos generados.

---

## 23. Apagar SOC-WIN11

Método preferido desde el propio Windows:

```text
Inicio
-> Encendido
-> Apagar
```

También puede solicitarse un apagado ACPI desde el host:

```bash
VBoxManage controlvm "SOC-WIN11" acpipowerbutton
```

Comprobar:

```bash
VBoxManage list runningvms
```

Esperar hasta que `SOC-WIN11` ya no aparezca.

---

## 24. Apagar SOC-WAZUH

El método preferido es realizar un apagado limpio desde Linux:

```bash
sudo shutdown -h now
```

Si se administra desde el host:

```bash
VBoxManage controlvm "SOC-WAZUH" acpipowerbutton
```

Después:

```bash
VBoxManage list runningvms
```

El laboratorio estará apagado cuando ninguna de sus máquinas aparezca.

---

## 25. Evitar apagados forzados

No utilizar normalmente:

```bash
VBoxManage controlvm "SOC-WAZUH" poweroff
```

ni:

```bash
VBoxManage controlvm "SOC-WIN11" poweroff
```

`poweroff` equivale conceptualmente a cortar la alimentación del equipo.

Puede ocasionar:

```text
corrupción de archivos
índices inconsistentes
eventos incompletos
problemas con el sistema operativo
```

Solo debe considerarse si una VM no puede apagarse limpiamente y la situación
requiere recuperación.

---

# Comprobaciones posteriores al arranque

## 26. Checklist rápido

Después de iniciar el laboratorio:

```text
[ ] VirtualBox funciona
[ ] SOC-LAB existe
[ ] SOC-WAZUH está encendido
[ ] SOC-WAZUH tiene 10.10.10.10
[ ] Wazuh Server está operativo
[ ] Wazuh Indexer está operativo
[ ] Wazuh Dashboard está operativo
[ ] SOC-WIN11 está encendido
[ ] SOC-WIN11 tiene 10.10.10.30
[ ] SOC-WIN11 alcanza los servicios necesarios de Wazuh
[ ] Wazuh Agent aparece Active
[ ] Security genera eventos
[ ] System genera eventos
[ ] PowerShell genera eventos
[ ] Sysmon genera eventos
[ ] Defender genera eventos
[ ] Los eventos pueden localizarse en Wazuh
```

Hasta que la telemetría no esté comprobada, el laboratorio no se considerará
listo para generar investigaciones.

---

# Comprobaciones antes del apagado

## 27. Checklist de cierre

Antes de terminar una sesión:

```text
[ ] Guardar consultas útiles
[ ] Guardar únicamente evidencias necesarias
[ ] Revisar que no existan credenciales en las evidencias
[ ] Registrar problemas encontrados
[ ] Registrar Detection Gaps si existen
[ ] Comprobar cambios pendientes en Git
[ ] Apagar SOC-WIN11 limpiamente
[ ] Apagar SOC-WAZUH limpiamente
[ ] Confirmar que no quedan VMs ejecutándose
```

---

# Git y evidencias

## 28. Qué puede almacenarse

Puede almacenarse:

```text
configuraciones sanitizadas
documentación
consultas
reglas de detección
capturas seleccionadas
informes
scripts propios
resultados sanitizados
```

---

## 29. Qué no debe almacenarse

No subir:

```text
passwords
tokens
API keys
claves privadas
credenciales Wazuh
credenciales Windows
ISOs
discos virtuales
snapshots
raw logs con información sensible
payloads recibidos de Internet
malware
datos personales
```

Antes de cada commit:

```bash
git status
```

y revisar manualmente los archivos añadidos.

---

# Diagnóstico básico

## 30. VirtualBox no encuentra una VM

```bash
VBoxManage list vms
```

Verificar que el nombre utilizado coincida exactamente con:

```text
SOC-WAZUH
SOC-WIN11
```

---

## 31. Una VM no aparece encendida

```bash
VBoxManage list runningvms
```

Consultar información:

```bash
VBoxManage showvminfo "SOC-WAZUH"
```

o:

```bash
VBoxManage showvminfo "SOC-WIN11"
```

---

## 32. SOC-LAB no aparece

```bash
VBoxManage list hostonlynets
```

Después verificar:

```bash
cat /etc/vbox/networks.conf
```

Debe contener:

```text
* 10.10.10.0/24
```

No recrear automáticamente la red sin investigar primero por qué desapareció.

---

## 33. Windows no aparece Active en Wazuh

Revisar en este orden:

```text
1. SOC-WIN11 está encendido
2. SOC-WIN11 conserva 10.10.10.30
3. SOC-WAZUH conserva 10.10.10.10
4. existe conectividad entre ambas máquinas
5. Wazuh Server está operativo
6. Wazuh Agent está ejecutándose
7. la configuración del agente apunta al servidor correcto
8. firewall no bloquea la comunicación necesaria
9. hora de ambas máquinas es coherente
10. logs del agente y del servidor
```

No reinstalar automáticamente el agente antes de identificar el fallo.

---

# Estado actual

## 34. Entregable 1

Estado al iniciar esta etapa:

```text
Repositorio                  OK
Rama de trabajo              OK
VirtualBox                   OK
SOC-LAB                      OK

SOC-WAZUH                    PENDIENTE
Wazuh Server                 PENDIENTE
Wazuh Indexer                PENDIENTE
Wazuh Dashboard              PENDIENTE

SOC-WIN11                    PENDIENTE
Wazuh Agent                  PENDIENTE
Sysmon                       PENDIENTE

Security telemetry           PENDIENTE
System telemetry             PENDIENTE
PowerShell telemetry         PENDIENTE
Sysmon telemetry             PENDIENTE
Defender telemetry           PENDIENTE
```

No cambiar un elemento a `OK` hasta disponer de evidencia verificable.

---

# Criterio operativo de cierre

## 35. Entregable 1 terminado

El entorno podrá considerarse operativo únicamente cuando pueda demostrarse:

```text
SOC-WIN11
    |
    ├── Security ------------------┐
    ├── System --------------------|
    ├── PowerShell ----------------|----> WAZUH
    ├── Sysmon --------------------|
    └── Defender ------------------┘
```

y exista evidencia de:

```text
Windows event
    |
    v
Wazuh Agent
    |
    v
Wazuh Server
    |
    v
Wazuh Indexer
    |
    v
consulta reproducible
```

Un agente en estado `Active` por sí solo **no completa el Entregable 1**.

---

# Alcance de seguridad

## 36. Principios operativos

Durante esta etapa:

- no ejecutar malware;
- no realizar ataques contra sistemas públicos;
- no abrir servicios del laboratorio a Internet;
- no configurar port forwarding doméstico;
- no exponer Wazuh Dashboard públicamente;
- no utilizar Bridged Networking para publicar las VMs;
- no desplegar todavía Cowrie;
- no desplegar todavía T-Pot;
- no desplegar todavía Suricata;
- no realizar brute force;
- no realizar simulaciones ofensivas antes de validar la telemetría.

Toda simulación posterior se limitará a sistemas propios creados
específicamente para este laboratorio.

---

# Internet Honeypot

## 37. Fuera del alcance de este documento

El honeypot público será desplegado posteriormente en infraestructura
separada.

Conceptualmente:

```text
Internet
   |
   v
VPS / Cloud
   |
   v
Cowrie
   |
   v
evidencia
   |
   v
pipeline de ingestión controlado
   |
   v
SOC
```

No existirá una ruta directa:

```text
Internet -> honeypot -> red doméstica
```

ni:

```text
Internet -> honeypot -> SOC-LAB
```

Los mecanismos exactos de transporte, autenticación, filtrado, almacenamiento,
retención y aislamiento se definirán en las fases HP correspondientes.

---

# Resumen operativo

## Encender

```text
Verificar VirtualBox
        ↓
Verificar SOC-LAB
        ↓
Encender SOC-WAZUH
        ↓
Esperar servicios Wazuh
        ↓
Encender SOC-WIN11
        ↓
Verificar agente
        ↓
Verificar telemetría
```

## Apagar

```text
Guardar evidencia necesaria
        ↓
Apagar SOC-WIN11
        ↓
Esperar apagado
        ↓
Apagar SOC-WAZUH
        ↓
Esperar apagado
        ↓
Confirmar que no quedan VMs activas
```

---

## Referencias oficiales

La configuración se basa en la documentación oficial de:

- Oracle VirtualBox 7.2
- Wazuh
- Microsoft Windows / Sysmon

Las versiones exactas utilizadas y cualquier cambio relevante se registrarán
durante cada entregable.