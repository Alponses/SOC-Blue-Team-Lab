# Plan de implementación y avance

**Punto actual:** entregable 0 terminado. La estructura, la arquitectura y las plantillas están listas. El siguiente paso es comprobar los recursos disponibles y desplegar Wazuh con Windows 11. Todavía no hay infraestructura instalada ni investigaciones ejecutadas.

Las etapas pendientes **requieren ejecución manual** en el laboratorio. Cada una se cerrará con sus archivos, pruebas, evidencias, problemas pendientes y siguiente paso documentados.

## Criterios de trabajo

- Completar y validar una etapa antes de avanzar sobre sus dependencias.
- Registrar las alertas esperadas que no aparezcan como **brecha de detección (Detection Gap)**, conservando el resultado y revisando recopilación, interpretación de campos, reglas, tiempos y supresiones.
- Crear una instantánea antes de cambiar el estado de un sistema; delimitar equipos e intentos y verificar la limpieza posterior.
- Relacionar cada conclusión con evidencias y cada mejora con una prueba.
- Revisar los archivos preparados para Git y guardar cambios coherentes en commits separados.

## Entregable 0 — Estructura y arquitectura

- [x] Revisar el directorio de trabajo y comprobar si existía un repositorio Git.
- [x] Crear `SOC-Blue-Team-Lab` sin sobrescribir archivos ajenos.
- [x] Preparar README, arquitectura y diagrama Mermaid.
- [x] Definir exclusiones de archivos y manejo de evidencias para publicación.
- [x] Crear plantillas de informe de incidente y procedimiento SOC.
- [x] Organizar espacios para casos, configuraciones, detecciones, procedimientos, consultas y capturas.
- [x] Definir el orden de implementación.
- [x] Validar enlaces internos y revisar los cambios.
- [x] Registrar las comprobaciones y crear el commit inicial.

**Resultado:** base documental y repositorio local listos. Las comprobaciones están en el [informe del entregable 0](deliverables/deliverable-0.md).

## Entregable 1 — Wazuh, Windows y Sysmon

**Siguiente etapa.** Crear la red aislada y desplegar únicamente SOC-WAZUH y SOC-WIN11, con agente Wazuh, Sysmon y Defender activo. El objetivo es demostrar la llegada de eventos normales antes de ejecutar escenarios de investigación.

- [ ] Comprobar RAM, disco y CPU disponibles, hipervisor compatible, requisitos de invitados, medios de evaluación y acceso a las máquinas. Confirmar que la subred propuesta no esté en uso.
- [ ] Registrar versiones, descargas oficiales y sumas de verificación cuando se proporcionen, recursos, nombres de equipos y recuperación. Mantener instaladores y credenciales fuera de Git.
- [ ] Crear la red solo anfitrión; revisar adaptadores, rutas IPv4/IPv6, reenvío, administración y exposición. Documentar la retirada del NAT temporal de actualización.
- [ ] Desplegar Wazuh todo en uno en `10.10.10.10` y Windows 11 en `10.10.10.30`; comprobar servicios y crear instantáneas de referencia.
- [ ] Registrar el agente Windows guardando las credenciales de forma privada. Configurar Security, System, PowerShell Operational, Sysmon Operational y Defender Operational.
- [ ] Ajustar auditoría de Windows y registro de PowerShell; configurar eventos de creación de procesos, conexiones acotadas y DNS en Sysmon. Documentar filtros y motivo.
- [ ] Verificar sincronización horaria, conversión a UTC, desfase, eventos locales, envío del agente, recepción del servidor y búsqueda en el SIEM.
- [ ] Generar eventos inocuos: inicio de sesión normal, comando o script con un marcador y actividad local de red/DNS cuando exista el servicio necesario. Recoger un evento normal de System y Defender manteniendo la protección activa.
- [ ] Mostrar al menos un evento de cada canal a través de toda la cadena de recopilación. Distinguir las alertas de los eventos consultados mediante una ruta de archivo temporal y limitada. Dejar pendiente cualquier cobertura de Sysmon que aún no pueda comprobarse.
- [ ] Registrar consultas, ID de fuente/evento, tiempos, campos, retraso de ingestión observado, datos ausentes, volumen y retención.
- [ ] Guardar fragmentos revisados, configuraciones sin secretos y unas pocas capturas con descripción. Validar enlaces y cerrar el informe de la etapa en Git.

**Archivos previstos:** documentación de instalación y comprobaciones en `docs/`, configuraciones en `configs/wazuh/` y `configs/windows/`, capturas seleccionadas y `docs/deliverables/deliverable-1.md`.

**Criterio de cierre:** las dos máquinas funcionan y están aisladas; Windows está registrado y cada canal requerido llega por una ruta documentada, con sus limitaciones de campos identificadas. Un agente conectado por sí solo no cumple este criterio. Si falta acceso al hipervisor o a un invitado, la instalación seguirá pendiente de ejecución manual.

Ubuntu, el simulador, las investigaciones de ataque, Active Directory, Suricata, phishing, AWS, Splunk y la publicación en GitHub quedan para sus etapas correspondientes.

## Entregable 2 — Ubuntu y telemetría de autenticación

- [ ] Desplegar SOC-LINUX en `10.10.10.40` con OpenSSH, agente Wazuh y registros de auditoría y sistema acotados.
- [ ] Identificar las fuentes reales del diario del sistema y rsyslog; evitar duplicados y comprobar SSH, autenticación, sudo, sistema y aplicaciones seleccionadas con operaciones normales.
- [ ] Comprobar campos de usuarios, procesos y origen; documentar los límites de atribución de red.
- [ ] Reservar un archivo o directorio de prueba sin datos sensibles para FIM; establecer la referencia y los requisitos de auditoría o who-data para identificar al actor más adelante.

**Criterio de cierre:** evidencia desde el origen hasta el SIEM, consultas, tiempos precisos, rutas de registros, configuración revisada y notas de recursos y retención. La fuerza bruta se ejecutará en la siguiente etapa.

## Entregable 3 — SOC-001: fuerza bruta SSH

- [ ] Preparar SOC-SIM en `10.10.10.50`, objetivos permitidos, cuenta de prueba, frecuencia y número máximo de intentos, posibles bloqueos, instantáneas y limpieza.
- [ ] Generar fallos SSH limitados contra SOC-LINUX; revisar origen, cuenta, recuento, intervalo y cualquier acceso exitoso posterior.
- [ ] Registrar alertas e ID de reglas reales o la brecha de detección; completar evidencias, línea de tiempo, ATT&CK, severidad, clasificación y decisión.

**Criterio de cierre:** primera investigación completa con intentos, eventos y alertas reconciliados, conclusión respaldada y limpieza verificada.

## Entregable 4 — SOC-002: autenticación Windows

- [ ] Generar fallos controlados teniendo en cuenta la política de bloqueo y el contexto local o de dominio.
- [ ] Identificar ID de eventos Security, estado y subestado, cuenta, origen disponible y eventos relacionados en el SIEM; construir la línea de tiempo.
- [ ] Completar el informe con resultado observado, criterios de escalamiento y limpieza.

**Criterio de cierre:** las evidencias de autenticación sostienen la clasificación; los campos ausentes se reconocen como limitaciones.

## Entregable 5 — SOC-003: PowerShell y Sysmon

- [ ] Ejecutar una simulación PowerShell inocua, revisada y con marcador, objetivo, límites y limpieza definidos.
- [ ] Correlacionar proceso y padre, comandos, usuario, equipo, hora, bloque de script y conexiones solo cuando se hayan observado.
- [ ] Documentar el resultado de la detección, la correspondencia con ATT&CK y las mejoras derivadas de la investigación.

**Criterio de cierre:** evidencia correlacionada entre fuentes y clasificación coherente con el contexto de simulación autorizada.

## Entregable 6 — Suricata e investigaciones de red

- [ ] Instalar Suricata en SOC-LINUX y enviar la salida EVE seleccionada a Wazuh; comprobar primero la visibilidad de la interfaz.
- [ ] Completar SOC-005 mediante un escaneo acotado de SOC-LINUX, con patrón de puertos y tiempos, registros de flujos/IDS e inspección de paquetes si aporta evidencia.
- [ ] Completar SOC-006 mediante una conexión inocua desde Windows hacia un servicio local, correlacionando proceso, direcciones y puertos; detener el servicio al terminar.
- [ ] Iniciar SOC-007 con un resolvedor local y un dominio reservado. Si depende del DNS de AD, registrarlo y finalizarlo en la etapa 7.
- [ ] Documentar respuesta DNS, equipo solicitante, método de consulta de reputación, límites del cifrado, cobertura, falsos positivos y brechas.

**Criterio de cierre:** casos 005 y 006 completos con tráfico observado. SOC-007 se cerrará únicamente con evidencia de consulta y respuesta. Cualquier ampliación de visibilidad del sensor deberá estar demostrada.

## Entregable 7 — Active Directory e identidades

- [ ] Desplegar SOC-DC01 en `10.10.10.20`, AD DS y DNS local para `soc.test`; configurar comunicaciones y políticas de auditoría.
- [ ] Crear usuarios ficticios normales, una identidad administradora separada y grupos de seguridad; unir Windows 11 al dominio.
- [ ] Verificar autenticación en controlador y estación, sincronización horaria y SOC-007 si estaba pendiente.
- [ ] Completar SOC-004: crear una cuenta, modificar pertenencia a grupos o privilegios, identificar actor/cuenta/privilegio/equipo/hora, comprobar autorización y restaurar el estado.

**Criterio de cierre:** informe de cambios de identidad, evidencia de recopilación del dominio/DNS, autenticación exitosa y fallida, y actividad administrativa autorizada.

## Entregable 8 — Detecciones, FIM y procedimientos SOC

- [ ] Crear o ajustar detecciones justificadas por los casos previos en Wazuh, Sigma cuando sean portables y Suricata cuando corresponda.
- [ ] Documentar objetivo, fuente, lógica, ATT&CK, verdaderos positivos esperados, falsos positivos, pruebas, resultados y brechas.
- [ ] Verificar controles positivos y negativos y límites de umbral; registrar versiones, campos y requisitos de interpretación de eventos.
- [ ] Completar SOC-008 con modificación controlada, estado anterior y posterior, evidencia FIM, actor si puede demostrarse y restauración verificada.
- [ ] Redactar los ocho procedimientos del índice y enlazar consultas y casos reales. Revisar los de phishing y AWS después de ejecutar sus investigaciones.

**Criterio de cierre:** detecciones probadas, caso FIM completo y procedimientos utilizables. La validación de Sigma debe indicar el motor de destino; una regla convertida sin ejecutar no está validada en ese motor.

## Entregable 9 — SOC-009: phishing

- [ ] Preparar un correo sintético identificado como tal o una muestra segura de entrenamiento con procedencia documentada.
- [ ] Revisar confianza de los encabezados, From, Reply-To, Return-Path, Received, SPF, DKIM, DMARC, URL no navegables, dominios, hashes y metadatos de adjuntos.
- [ ] Registrar los resultados de enriquecimiento obtenidos o el motivo de no realizar las consultas, manteniendo la confidencialidad.
- [ ] Completar resumen ejecutivo, evidencias, tabla de IOC, línea de tiempo, conclusión, acciones y secciones del informe; validar el procedimiento de phishing.

**Criterio de cierre:** análisis reproducible que diferencia datos sintéticos de pruebas verificadas de entrega y autenticación.

## Entregable 10 — SOC-010: AWS CloudTrail

- [ ] Definir cuenta propia de laboratorio, acceso seguro, regiones y recursos permitidos, costes, retención y limpieza antes de generar cambios.
- [ ] Configurar y comprobar IAM, cobertura de CloudTrail y entrega a CloudWatch. Generar actividad limitada de identidad/API/recursos, incluido el contexto de uso de claves de acceso cuando corresponda, conservando las claves de forma privada.
- [ ] Reconstruir quién hizo qué, cuándo, desde dónde, contra qué recurso, qué cambió y cuál fue el resultado. Verificar retirada de recursos y permisos de prueba.
- [ ] Publicar muestras sin datos sensibles, limitaciones, informe y procedimiento AWS validado.

**Criterio de cierre:** los eventos reales sostienen la reconstrucción y la limpieza está verificada, sin credenciales ni identificadores de infraestructura real en Git.

## Entregable 11 — Splunk y SPL

- [ ] Incorporar Splunk Enterprise después de validar las investigaciones con Wazuh; registrar versión, recursos, tipos de fuente, correspondencia de campos, interpretación de tiempos y recuento de importación.
- [ ] Importar datos del laboratorio revisados, reconciliar recuentos y documentar transformaciones.
- [ ] Crear y ejecutar las siete consultas del índice, con objetivo, campos, intervalo, comportamiento esperado, resultados y limitaciones.
- [ ] Documentar la práctica como Splunk Enterprise y SPL. Enterprise Security solo se incluirá si llega a utilizarse y existe evidencia.

**Criterio de cierre:** consultas reproducibles sobre datos del laboratorio, con resultados observados y límites conocidos.

## Entregable 12 — Revisión final del portafolio

- [ ] Actualizar avance del README, arquitectura, versiones, enlaces, resultados y habilidades respaldadas por casos.
- [ ] Seleccionar pocas capturas con descripción y mantener los registros, las consultas y el razonamiento como evidencias principales.
- [ ] Comprobar la estructura de todos los informes y la justificación de clasificación, severidad y decisión.
- [ ] Revisar enlaces, tamaño, archivos e historial, secretos, privacidad, licencias, metadatos de autor y brechas pendientes.
- [ ] Verificar que el objetivo, la infraestructura, los casos y las conclusiones se entiendan en 2–3 minutos.

**Criterio de cierre:** repositorio revisado y preparado para publicación. La creación del repositorio remoto y la publicación se realizarán después de esa revisión.
