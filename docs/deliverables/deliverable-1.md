# Entregable 1 — Wazuh y telemetría Windows

**DELIVERABLE 1 — COMPLETE**

Revisión operativa: **2026-10-05**. SOC-WAZUH y SOC-WIN11 funcionan en SOC-LAB; el agente `001` está ACTIVE en manager y Dashboard. Se ejecutó **Security → System → Sysmon → PowerShell → Defender**, con eventos benignos reales, identidad local correlacionada en manager y documentos consultables mediante el Dashboard. Las [cinco fichas](../../evidence/deliverable-1/README.md) contienen extractos observados, consultas, comparaciones y límites.

## Base y alcance

Se partió de `origin/main` actualizado, `de0d8b8` (PR #1 mergeado, incluye `1df7bf9`), con árbol limpio, y se creó `fix/complete-deliverable-1`. El mensaje anterior `DELIVERABLE 1 COMPLET` no se tomó como aceptación. Ningún commit previo se revirtió o modificó; no se reescribió historia. El [preflight histórico](../../evidence/deliverable-1/preflight.md), la preparación de Windows del 2026-09-30 y el [despliegue previo Wazuh](../../evidence/deliverable-1/wazuh-deployment.md) permanecen como antecedentes fechados.

Solo se trabajó en SOC-WAZUH y SOC-WIN11. No se desplegó SOC-LINUX, AD, honeypot, Suricata, AWS o Splunk. No se ejecutaron ataques, Atomic Red Team, malware ni EICAR. No se abrieron ni cerraron incidentes SOC-001–SOC-015.

## Infraestructura

| Elemento | Estado real |
| --- | --- |
| Host | macOS x86_64, VirtualBox 7.2.14r174565, 16 GiB; ambas VM operaron simultáneamente. Presión de memoria y swap observados, sin afirmar capacidad para más equipos |
| SOC-WAZUH | Ubuntu Server 24.04.5; `10.10.10.10/24`, 4 vCPU / 8192 MiB / 80 GiB; manager, indexer, dashboard y Filebeat activos |
| SOC-WIN11 | Windows 11 Enterprise Evaluation 25H2, `26200.6584`, hostname SOC-WIN11; `10.10.10.30/24`, 2 vCPU / 4096 MiB / 80 GiB GPT |
| Aislamiento | NIC 1 SOC-LAB; NIC 2 `none`; sin ruta externa por defecto ni port forwarding; comunicación privada TCP/1514 verificada |
| Protecciones | TPM 2.0 preparado, Secure Boot true, UAC habilitado, Firewall Domain/Private/Public y Defender/RTP activos |
| Enrollment | ID `001`; registro real y fila active en Dashboard; TCP/1515 cerrado y authd deshabilitado después de enrollment |

Evidencia: [Windows](../../evidence/deliverable-1/windows-deployment.md), [inventario nativo](../../evidence/deliverable-1/windows-native-checks.json), [revisión final Windows](../../evidence/deliverable-1/windows-final-checks.json), [revisión final Wazuh/host](../../evidence/deliverable-1/operational-final-checks.json) y [captura del agente](../../evidence/deliverable-1/windows-agent-dashboard.png). El mantenimiento temporal NAT de Windows terminó antes de validar. Windows fue activado oficialmente y Defender actualizado; no se habilitaron excepciones de requisitos o antivirus.

## Versiones

| Componente | Instalada/observada |
| --- | --- |
| Ubuntu Server | 24.04.5 LTS, kernel `6.8.0-142-generic` |
| Wazuh manager/indexer/dashboard | `4.14.8-1` |
| Filebeat | `7.10.2-2` |
| Wazuh Agent Windows | MSI `4.14.8-1`, binario/servicio `4.14.8` |
| Sysmon | `15.22`, Authenticode Valid, Running/Auto; acepta XML schema `4.82` y anuncia soporte `4.91` |
| Windows PowerShell | `5.1.26100.6584`, Script Block Logging habilitado; 4104 real |
| Defender | Plataforma `4.18.26080.4`, motor `1.1.26080.3`, firmas `1.459.565.0`; protección activa |

El ProductName heredado del registro y la marca de agua de evaluación no sustituyen Caption/build nativos. El XML Sysmon original se conserva byte por byte: SHA-256 `cfbf327432a53d8edb3f18b281e233a47e62e5c41276f4395bee1482ea71cbdf`. [Aceptación](../../evidence/deliverable-1/sysmon-install-observed.txt) y [configuración efectiva](../../evidence/deliverable-1/sysmon-effective-observed.txt).

## Matriz de validación

| Fuente | Windows local | Agente | Manager | Documento consultable | Evidencia |
| --- | --- | --- | --- | --- | --- |
| Security | PASS — 4624/6609 | PASS — ID 001 | PASS | PASS — `_search` | [Ficha](../../evidence/deliverable-1/security.md) / [JSON](../../evidence/deliverable-1/security-event.json) |
| System | PASS — 7001/824 | PASS — ID 001 | PASS | PASS — `_search` | [Ficha](../../evidence/deliverable-1/system.md) / [JSON](../../evidence/deliverable-1/system-event.json) |
| Sysmon | PASS — 1/530 | PASS — ID 001 | PASS | PASS — `_search` | [Ficha](../../evidence/deliverable-1/sysmon.md) / [JSON](../../evidence/deliverable-1/sysmon-event.json) |
| PowerShell | PASS — 4104/2109 | PASS — ID 001 | PASS | PASS — `_search` | [Ficha](../../evidence/deliverable-1/powershell.md) / [JSON](../../evidence/deliverable-1/powershell-event.json) |
| Defender | PASS — 1001/394 | PASS — ID 001 | PASS | PASS — `_search` | [Ficha](../../evidence/deliverable-1/defender.md) / [JSON](../../evidence/deliverable-1/defender-event.json) |

Sysmon también pasó NetworkConnect `3/554`, destino privado `.10:1514`: [segunda correlación](../../evidence/deliverable-1/sysmon-network-event.json). Las búsquedas se ejecutaron mediante `_search` autenticado a través del Dashboard; no se afirma una revisión visual de cada fuente en Discover.

## Criterios de aceptación operativa

- [x] Ambas VM operativas, aisladas, con recursos/SO/red/protecciones verificados.
- [x] Agente oficial compatible, servicio Running, enrollment/ID/conexión y ACTIVE en manager/Dashboard.
- [x] Sysmon instalado con XML original aceptado; servicio, canal y configuración efectiva comprobados.
- [x] Security, System, Sysmon, PowerShell y Defender: evento local → agente → manager → documento buscable.
- [x] Comparaciones, ausencias y diferencias de representación registradas sin reconstruir campos.
- [x] Ventana archives cerrada, enrollment cerrado, cinco canales del agente conservados.
- [x] Evidencia mínima sanitizada con hashes y checkpoints reales, sin secretos ni medios/VM en Git.
- [x] Documentación actualizada y comprobaciones finales registradas.

## Ventana y límites de cobertura

La [sesión real](../../evidence/deliverable-1/telemetry-session.json) registra inicio/fin, espacio, volumen, consultas, relojes y restauración de `logall_json=no` / Filebeat archives false. Duración de 23 min 40 s y espacio superior a 10 GiB. El muestreo de espacio tuvo un intervalo máximo de 7 min 43 s, superior al objetivo de cinco minutos; se preservan sus marcas reales y no se afirma monitoreo continuo. El patrón `wazuh-archives-*` usa `timestamp`; los documentos seleccionados siguen consultables después del cierre.

Los nuevos eventos benignos sin alerta ya no se indexan como archives tras cerrar la ventana. Los cinco canales permanecen activos y las alertas siguen su ruta habitual. La retención sostenida no quedó implementada: revisión propuesta a siete días, `2026-10-12`, sin programar borrados ni usar comodines destructivos.

Seis campos de identidad coinciden exactamente por evento. Las fichas/JSON conservan campos EventData ausentes y diferencias de escapes o espacios; PASS acredita ingestión del evento, no igualdad de todos los campos, una alerta, cobertura total del canal ni una detección de ataque. Los nombres de usuario y SIDs se compararon en privado y se omitieron de los extractos.

Windows usa UTC−07:00 en esta fecha; la correlación utiliza SystemTime UTC original. Los relojes estaban retrasados respecto del host y se registraron intervalos de desfase medidos. Las diferencias recepción−evento no son una latencia precisa; no se corrigieron retroactivamente los eventos. La red aislada carece de ruta NTP externa. DNS, FileCreate y RegistryEvent de Sysmon quedan sin correlación validada en esta sesión.

## Problemas encontrados

- Wazuh manager superó el timeout inicial de 45 s durante arranque conjunto; se aplicó `TimeoutStartSec=180` y se confirmó el servicio activo.
- Una suspensión del host interrumpió las VM y produjo desfase; se registró la recuperación y la lectura de relojes. Se evitó el reposo durante el resto de la sesión.
- Windows requirió activación y actualización de Defender. `Update-MpSignature` devolvió `0x80070652`; la comprobación posterior verificó las versiones actualizadas, sin convertir aquella orden fallida en PASS.
- La envoltura inicial Sysmon se detuvo por su banner stderr antes de instalar; la ejecución corregida comprobó códigos de retorno y aceptación del XML.
- Un fallo incidental al introducir la contraseña no se usó como prueba. Se excluyó una sesión auxiliar Advapi y se seleccionó el ingreso normal User32 para Security.
- System no tenía SCM/7036 en la ventana; se validó Winlogon/7001 realmente existente. No fue una brecha de ingestión del canal.
- El certificado del Dashboard identifica loopback. API/curl validó CA/identidad loopback mediante conexión privada; el navegador limitó la excepción al pin de clave pública del certificado observado.

## Evidencia, recuperación y validación del repositorio

[Índice y snapshots](../../evidence/deliverable-1/README.md#snapshots), [inventario de checkpoints](../../evidence/deliverable-1/deliverable-1-snapshots.json) y [SHA256SUMS](../../evidence/deliverable-1/SHA256SUMS). Los checkpoints finales se tomaron con apagado limpio, sin RAM guardada, después de comprobar las cinco cadenas y cerrar archives. Los originales, claves, contraseñas, instaladores, ISO y discos/snapshots permanecen fuera de Git. La tarea temporal SYSTEM y sus scripts se retiraron antes del checkpoint final de Windows.

[Resultados de revisión estática](../../evidence/deliverable-1/repository-validation.json): validador del repositorio/enlaces Markdown, XML, JSON/hashes, whitespace, secretos conocidos/patrones, medios/VM artifacts y diff completo. La búsqueda de secretos está limitada a los cambios revisados y sus patrones/valores; no acredita una auditoría universal del historial.

Se crea un commit nuevo de cierre. No se mergea automáticamente. **Deliverable 2 no se inició.**
