# Entregable 0 — Estructura y arquitectura

**Fecha de cierre:** 24 de septiembre de 2026. **Estado:** completado.

## Objetivo de la etapa

Dejar preparada la base del proyecto: organización del repositorio, arquitectura del laboratorio, orden de implementación y formato de las investigaciones. Esta etapa permite comenzar la instalación con un alcance definido y criterios claros para comprobar los resultados.

## Trabajo realizado

Se creó `SOC-Blue-Team-Lab` en un directorio de trabajo vacío y se inicializó Git en la rama `main`. Quedaron definidos los equipos y direcciones propuestos, las fuentes de telemetría, los límites de visibilidad del sensor y los criterios de publicación de evidencias.

También se prepararon diez fichas de investigación, plantillas reutilizables y espacios para configuraciones, detecciones, consultas y capturas. El repositorio continúa siendo local y la infraestructura está pendiente de despliegue.

## Archivos preparados

| Ubicación | Contenido |
| --- | --- |
| [README](../../README.md) | Objetivo, avance, topología Mermaid, entorno, flujo SOC y casos previstos |
| [.gitignore](../../.gitignore) | Exclusiones de secretos, archivos locales, imágenes, binarios, registros completos y capturas |
| [Arquitectura](../architecture.md) | Direcciones y recursos previstos, aislamiento, visibilidad, telemetría y dependencias |
| [Plan de implementación](../implementation-checklist.md) | Entregables 0–12, avance y criterios de cierre |
| [Manejo de evidencias](../evidence-handling.md) | Procedencia, retirada de datos sensibles y revisión antes de publicar |
| [Plantilla de incidente](../../templates/incident-report.md) | Secciones de investigación, resumen ejecutivo y procedencia de evidencias |
| [Plantilla SOC](../../templates/soc-playbook.md) | Comprobaciones, registros, enriquecimiento, escalamiento, cierre y validación |
| [Índice de investigaciones](../../incidents/README.md) | Diez casos planificados, incluidos phishing y CloudTrail |
| [Detecciones](../../detections/README.md) | Directorios Wazuh, Sigma y Suricata, y criterios de documentación |
| [Procedimientos SOC](../../playbooks/README.md) | Alcance de ocho procedimientos para analistas |
| [Consultas Splunk](../../queries/splunk/README.md) | Siete búsquedas previstas y alcance de Enterprise/SPL |
| [Configuraciones](../../configs/README.md) | Seis directorios reservados mediante `.gitkeep` |
| [Capturas](../../screenshots/README.md) | Criterios para seleccionar y describir imágenes de evidencia |
| [Validador](../../scripts/validate_repository.py) e [instrucciones](../../scripts/README.md) | Comprobación local de enlaces y anclas |
| Este informe | Resultado de la etapa, comprobaciones, pendientes y siguiente paso |

## Comprobaciones al cerrar la etapa

Estos resultados corresponden a la estructura inicial guardada en el commit `193e902`. La documentación se ha revisado y traducido posteriormente; el validador permite comprobar los enlaces de la versión actual.

| Comprobación | Resultado registrado |
| --- | --- |
| Enlaces internos | 112 enlaces válidos en 27 archivos Markdown, incluidas rutas y anclas |
| Control negativo del validador en un repositorio temporal | Rechazó un archivo inexistente y un encabezado inexistente; aceptó los enlaces corregidos |
| Exclusiones mediante `git check-ignore --stdin` | 28 rutas sensibles, de datos completos o binarios excluidas; 9 rutas previstas para fuentes y fragmentos revisados permitidas |
| Plantilla de informe | Presentes las 13 secciones requeridas, además del resumen ejecutivo |
| Estado de los casos | Las diez fichas indicaban que los escenarios estaban pendientes de ejecución |
| Inventario de archivos | 35 archivos de texto UTF-8 o vacíos, incluidos 27 Markdown; todos menores de 1 MiB |
| `git diff --cached --check` | Sin errores de espacios en los archivos preparados para el commit |
| Revisión de cambios | Solo archivos nuevos del proyecto, sin modificaciones ajenas |
| Git | Rama local `main`, sin remoto configurado |

El commit inicial utiliza el autor genérico `SOC Lab Maintainer` y la dirección reservada `soc-lab@example.invalid` para evitar datos personales en el historial.

Estas comprobaciones cubren la documentación y la organización local. No validan el funcionamiento del laboratorio, las reglas de detección, la representación visual de Mermaid, los enlaces externos ni la ausencia de secretos mediante un analizador especializado. Las referencias de arquitectura están enlazadas en el documento correspondiente.

## Evidencias disponibles

La evidencia de esta etapa consiste en los archivos del repositorio, el historial Git y los resultados de las comprobaciones documentales. Los registros operativos, alertas, capturas, resultados de detección e informes de incidentes se recopilarán durante las siguientes etapas.

## Pendientes

- Comprobar capacidad del equipo, hipervisor, compatibilidad de invitados, medios de instalación y acceso a las máquinas.
- Ejecutar y validar instalación, aislamiento, cortafuegos y recopilación. Estas tareas **requieren ejecución manual**.
- Verificar la cobertura de Suricata cuando se instale; el diseño inicial solo contempla tráfico visible en SOC-LINUX.
- Disponer de un resolvedor local para SOC-007 o completar el caso después de instalar AD DNS.
- Revisar visualmente el diagrama en GitHub cuando se publique.
- Revisar archivos, historial y secretos antes de crear el repositorio público.

## Revisión de la documentación

La documentación se mantiene en español, con nombres de productos, comandos, rutas y campos técnicos conservados para facilitar su uso. El README presenta el objetivo y el punto actual del proyecto; cada caso indica su propósito, sus requisitos y las evidencias que faltan.

## Siguiente etapa

**Entregable 1 — Wazuh, Windows y Sysmon.** Comprobar recursos y aislamiento, desplegar SOC-WAZUH y SOC-WIN11, registrar el agente Windows y configurar Security, System, PowerShell, Sysmon y Defender. Después, verificar la llegada de eventos inocuos y guardar configuraciones, consultas y fragmentos sin datos sensibles.

El detalle y los criterios de cierre están en el [plan del entregable 1](../implementation-checklist.md#entregable-1--wazuh-windows-y-sysmon). Ubuntu, el simulador, Active Directory, Suricata, las investigaciones, AWS y Splunk se incorporarán en las etapas posteriores.
