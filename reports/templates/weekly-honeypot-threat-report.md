# Weekly Honeypot Threat Report

**Evidence Origin: Observed Honeypot Telemetry**

**Estado: plantilla sin datos. NO DATA — DEPLOYMENT PENDING.** La procedencia indica la fuente requerida para completar este informe; no certifica observaciones existentes. Observed Internet activity does not imply compromise of a production environment.

| Control | Registro |
| --- | --- |
| Observation window | Inicio incluido / fin excluido UTC: pendiente |
| Sensor / época / versiones | Pendiente |
| Analista / destinatario | Alias / responsable SOC: pendiente |
| Fecha del informe y corte de ingestión | Pendiente |
| Revisión / informe sustituido / motivo | Pendiente; registrar lotes tardíos o correcciones sin sobrescribir resultados publicados |
| Sensor uptime | NO DATA — DEPLOYMENT PENDING |
| Cobertura y lagunas | NO DATA — DEPLOYMENT PENDING |
| Retraso de importación / última recepción | NO DATA — DEPLOYMENT PENDING |
| Consulta, filtros, deduplicación y revisión | Pendiente |

## Resumen para el responsable SOC

Pendiente de observaciones. Resumir comportamientos que requieren atención, impacto demostrado, confianza, cambios frente a una ventana comparable y decisiones solicitadas. Distinguir hechos de hipótesis y actividad del señuelo de compromiso del host o de producción.

## Calidad y alcance de la observación

Documentar servicios expuestos, interfaz y cobertura de red, periodos operativos, mantenimiento, desfase, pérdida, errores de parsing y datos atrasados. Calcular uptime desde salud del sensor; no desde el tiempo entre primer y último evento. Indicar fuente y denominador del porcentaje. Las pruebas del operador y replays se excluyen y se registran aparte.

## Métricas de la semana

| Métrica | Valor observado | Consulta / evidencia / comparación válida |
| --- | --- | --- |
| Total events | NO DATA — DEPLOYMENT PENDING | Pendiente |
| Unique sources | NO DATA — DEPLOYMENT PENDING | Pendiente |
| Authentication attempts y resultados | NO DATA — DEPLOYMENT PENDING | Pendiente |
| Successful emulated sessions | NO DATA — DEPLOYMENT PENDING | Pendiente |
| Interactive sessions / commands | NO DATA — DEPLOYMENT PENDING | Pendiente |
| Top services / destination ports | NO DATA — DEPLOYMENT PENDING | Pendiente |
| Top ASNs / source networks | NO DATA — DEPLOYMENT PENDING | Pendiente |
| Geographic observations / unknowns | NO DATA — DEPLOYMENT PENDING | Pendiente |
| Most common usernames revisados o alias | NO DATA — DEPLOYMENT PENDING | Pendiente |

Conservar definiciones y unidades de [SOC Overview](../../dashboards/soc-overview/README.md). Si la semana está incompleta o cambió la cobertura, explicar la comparación; no extrapolar un total sin indicarlo. Después del despliegue, usar cero solo si una consulta con cobertura comprobada devuelve cero.

Calcular por tiempo de evento y corte de ingestión registrado. Si llegan lotes de esta semana después del corte, emitir una revisión identificable de sus métricas y decisiones; no contarlos como actividad nueva de la semana siguiente. Conservar consulta y versión anterior para explicar la diferencia.

## Sesiones y comportamientos relevantes

| Sesión / caso | Intervalo UTC | Comportamiento y secuencia | Evidencia revisada | Limitación / decisión |
| --- | --- | --- | --- | --- |
| Pendiente | Pendiente | NO DATA — DEPLOYMENT PENDING | Pendiente | Sin decisión |

Incluir autenticación, comandos, intentos de descarga y duración únicamente cuando existan. No ejecutar payloads, abrir URL maliciosas ni adjuntar binarios/transcripciones completas. La aceptación por Cowrie es emulada.

## Detecciones y MITRE ATT&CK

| Regla / revisión | Alertas observadas y nivel | Comportamiento validado | Técnica y referencia oficial | Evidencia / brecha |
| --- | --- | --- | --- | --- |
| Pendiente | NO DATA — DEPLOYMENT PENDING | Pendiente | Pendiente | Pendiente |

Solo incluir técnicas sostenidas por detecciones validadas; no asignar técnicas por país, ASN, reputación o volumen. Separar nivel Wazuh de severidad del incidente y no contar alertas como intentos.

## Incidentes abiertos y decisiones

| Caso | Motivo de apertura | Clasificación / severidad | Estado y decisión | Responsable / siguiente acción |
| --- | --- | --- | --- | --- |
| Pendiente | NO DATA — DEPLOYMENT PENDING | Sin evaluar | Pendiente | Pendiente |

Relacionar alerta → triage → evidencia → enriquecimiento → timeline → ATT&CK → clasificación → decisión. Registrar cero casos solo tras una revisión real de la ventana; los placeholders SOC-011–SOC-015 no son incidentes abiertos.

## Falsos positivos y ruido benigno

Pendiente. Registrar reglas afectadas, explicación alternativa y evidencia, distinguiendo False Positive, Benign Positive, Internet Noise y actividad sospechosa no concluyente. Un volumen alto no obliga a abrir un incidente ni confirma DDoS.

## Anomalías de red

Pendiente. Comparar tasas con baseline, distribución de protocolos/puertos, estados TCP, pérdida y salud. Registrar evidencia del proveedor y resultado de mitigación si existe. Aplicar los [criterios de clasificación](../../dashboards/network-anomalies/README.md); no forzar una conclusión de DoS/DDoS sin soporte.

## Observaciones geográficas y enriquecimiento

> Geographic information represents the estimated location of the observed source IP address and does not establish the physical location or identity of an attacker.

Registrar GeoIP/ASN, fuente, fecha de consulta, versión, resultado, confianza y limitación. Las IP pueden ser intermediarios, nodos comprometidos o NAT; no atribuir identidad o coordinación. Aplicar [enriquecimiento seguro](../../enrichment/README.md); servicios externos opcionales y sin envíos automáticos de datos privados.

## Brechas y recomendaciones

| Gap / hallazgo | Evidencia e impacto sobre la conclusión | Recomendación priorizada | Responsable / plazo | Comprobación de cierre |
| --- | --- | --- | --- | --- |
| Pendiente | NO DATA — DEPLOYMENT PENDING | Pendiente | Pendiente | Pendiente |

## Anexo reproducible y revisión de publicación

Enlazar consultas, filtros, ventanas, versión del contrato, registros e incidentes revisados; incluir inventario de evidencia con hash posterior a la sanitización. Conservar raw privado. Revisar credenciales, usuarios, IP de infraestructura, comandos, URL, filenames, tokens y datos personales según [manejo de evidencias](../../docs/evidence-handling.md).

La aprobación del contenido del informe no implica autorización para realizar contención en sistemas ajenos ni enviar mensajes a terceros. Registrar acciones recomendadas y ejecutadas por separado.
