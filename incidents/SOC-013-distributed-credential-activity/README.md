# SOC-013 — Distributed Credential Activity

**Evidence Origin: Observed Honeypot Telemetry**

**Entorno: Internet Honeypot — OBSERVED INTERNET TELEMETRY.**

**Estado: placeholder; NO DATA — DEPLOYMENT PENDING.** La procedencia indica la fuente requerida; no hay alerta, investigación abierta, evidencia, métricas, clasificación ni decisión existentes. Depende de HP-2/HP-3 y de observar actividad pertinente en HP-4.

## Objetivo

Evaluar similitudes de autenticación entre múltiples orígenes y distinguir distributed brute force, password spraying, automatización y ruido no relacionado.

## Evidencias necesarias

IP y ASN de fuentes, ventanas sincronizadas, cuentas intentadas, secuencia/frecuencia, resultados, sesiones y similitud de credenciales solo bajo análisis privado cuando esté autorizada.

Originales privados; publicar solo extractos revisados con manifiesto y localizadores según [manejo de evidencias](../../docs/evidence-handling.md). No sustituirlos por muestras inventadas ni simulaciones presentadas como Internet.

## Recorrido de investigación pendiente

Alerta → triage → evidencia → enriquecimiento → timeline → ATT&CK → clasificación → decisión.

1. Definir cohortes y ventana antes de comparar; deduplicar sin colapsar intentos distintos y excluir pruebas del operador.
2. Comparar usuarios, orden, tiempos, cadencia y otros atributos efectivamente registrados; documentar similitudes y diferencias con evidencia.
3. Evaluar password spraying solo si existe evidencia de pocos secretos repetidos contra varias cuentas; si las credenciales no están disponibles, declarar que esa distinción no puede validarse.
4. Contrastar distributed brute force, bot automation y fuentes independientes; considerar NAT, proxies, herramientas comunes y sesgo de un único sensor. Un ASN o país compartido no acredita coordinación.

## Entrega y decisión

Completar la [plantilla de incidente](../../templates/incident-report.md) con evidencia vinculada, timeline UTC, [enriquecimiento](../../enrichment/README.md) con fuente/fecha/confianza/limitación, comportamiento que respalde ATT&CK, severidad y clasificación justificadas, decisión de cierre o escalamiento, responsable y mejora de detección. No asignar técnicas ni resultado antes del análisis.

**Límites específicos:** No inferir coordinación por múltiples IP o diccionarios genéricos compartidos. Comparaciones sensibles permanecen privadas; no publicar passwords, hashes simples ni diccionarios masivos.

Observed Internet activity does not imply compromise of a production environment. La reputación y GeoIP no determinan identidad, ubicación física ni responsabilidad.

## Dependencias y siguiente paso

Cumplir [seguridad y despliegue](../../honeypot/deployment-checklist.md), [contrato Wazuh](../../configs/honeypot/wazuh/README.md) y [criterios de red](../../dashboards/network-anomalies/README.md). Esperar telemetría real suficiente y registrar carencias; ninguna actividad pública se ejecuta para completar esta ficha.

[Volver al índice de investigaciones](../README.md)
