# SOC-011 — Internet SSH Brute Force

**Evidence Origin: Observed Honeypot Telemetry**

**Entorno: Internet Honeypot — OBSERVED INTERNET TELEMETRY.**

**Estado: placeholder; NO DATA — DEPLOYMENT PENDING.** La procedencia indica la fuente requerida; no hay alerta, investigación abierta, evidencia, métricas, clasificación ni decisión existentes. Depende de HP-2/HP-3 y de observar actividad pertinente en HP-4.

## Objetivo

Investigar intentos SSH no solicitados y determinar si el patrón sostiene fuerza bruta, ruido u otra explicación.

## Evidencias necesarias

IP de origen, ASN, GeoIP estimada, usuarios intentados revisados, frecuencia, timestamps, resultados de sesión, fuentes relacionadas y actividad previa dentro de la retención.

Originales privados; publicar solo extractos revisados con manifiesto y localizadores según [manejo de evidencias](../../docs/evidence-handling.md). No sustituirlos por muestras inventadas ni simulaciones presentadas como Internet.

## Recorrido de investigación pendiente

Alerta → triage → evidencia → enriquecimiento → timeline → ATT&CK → clasificación → decisión.

1. Partir de una alerta real o búsqueda documentada; registrar regla, versión, intervalo y salud de ingestión. Si la detección esperada no existe, documentar Detection Gap.
2. Contar intentos únicos por fuente, usuario y ventana, separando conexiones, fallos, aceptación emulada y sesiones posteriores; contrastar timestamps y duplicados.
3. Enriquecer IP en privado con ASN/GeoIP y reputación opcional; buscar actividad previa y fuentes relacionadas sin atribuir identidad por red compartida.
4. Construir timeline y comparar fuerza bruta con reintentos aislados, comprobaciones autorizadas o automatización sin evidencia suficiente de coordinación.

## Entrega y decisión

Completar la [plantilla de incidente](../../templates/incident-report.md) con evidencia vinculada, timeline UTC, [enriquecimiento](../../enrichment/README.md) con fuente/fecha/confianza/limitación, comportamiento que respalde ATT&CK, severidad y clasificación justificadas, decisión de cierre o escalamiento, responsable y mejora de detección. No asignar técnicas ni resultado antes del análisis.

**Límites específicos:** Una autenticación aceptada por Cowrie representa acceso a la emulación. No prueba compromiso del VPS ni de producción. No publicar contraseñas ni inferir fuerza bruta solo por volumen de logs.

Observed Internet activity does not imply compromise of a production environment. La reputación y GeoIP no determinan identidad, ubicación física ni responsabilidad.

## Dependencias y siguiente paso

Cumplir [seguridad y despliegue](../../honeypot/deployment-checklist.md), [contrato Wazuh](../../configs/honeypot/wazuh/README.md) y [criterios de red](../../dashboards/network-anomalies/README.md). Esperar telemetría real suficiente y registrar carencias; ninguna actividad pública se ejecuta para completar esta ficha.

[Volver al índice de investigaciones](../README.md)
