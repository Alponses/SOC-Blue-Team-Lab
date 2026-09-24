# SOC-NNN — Título del incidente

**Evidence Origin: [seleccionar un valor permitido]**

Elegir exactamente uno antes de utilizar el informe: `Controlled Simulation`, `Observed Honeypot Telemetry`, `Synthetic Training Sample` o `Sanitized Cloud Activity`. En una ficha pendiente indicar que es la fuente requerida, aún sin recopilar. Registrar también `CONTROLLED TELEMETRY` u `OBSERVED INTERNET TELEMETRY` según el contexto; sanitizar no cambia el origen. Ver [definiciones](../docs/evidence-handling.md#evidence-origin).

Plantilla para documentar una investigación desde la alerta inicial hasta su cierre o escalamiento. Los campos se completan durante el análisis; la clasificación y la decisión quedan pendientes hasta disponer de evidencias suficientes.

| Dato | Registro |
| --- | --- |
| Estado | Pendiente / Requiere ejecución manual / En investigación / Validado |
| Analista | Alias del laboratorio |
| Procedencia de la evidencia | Valor exacto de Evidence Origin; sensor/época y procedencia de fuentes adicionales si existen |
| Intervalo | Inicio y fin en UTC; zona original y desfase del reloj |
| Entorno y versiones | Sistema, agente, revisión de reglas/configuración y herramientas |
| Autorización | Equipos propios, propósito, actor autorizado y ventana de prueba |
| Ejecución y recuperación | Pasos acotados, instantánea previa, señal esperada, condiciones de parada, limpieza y resultado comprobado |

## Resumen ejecutivo

Describir el comportamiento observado, los equipos afectados, el impacto demostrado, la conclusión y la acción. En phishing, incluir el pretexto del correo y si se conoce alguna interacción o ejecución por parte del usuario. Diferenciar hechos, hipótesis e información pendiente.

Para casos de honeypot: **Observed Internet activity does not imply compromise of a production environment.** Distinguir sesión aceptada por emulación, comando solicitado, respuesta emulada e impacto demostrado en el host. No asumir una persona interactuando ni coordinación entre fuentes.

## Alerta

Registrar hora, ID/nombre/versión de regla, nivel, fuente, campos que activaron la detección y referencia de la alerta. Explicar por qué se investigó. Si faltó una alerta esperada, registrar **brecha de detección (Detection Gap)**, la prueba realizada y el evento o búsqueda manual que inició el caso.

## Evaluación inicial

Revisar criticidad del activo, duplicados, salud de la recopilación, tiempos y desfases, actividad autorizada e impacto inmediato. Anotar la hipótesis inicial y la evidencia que permitiría descartarla.

## Alcance

Identificar equipos, usuarios, direcciones de origen y destino, servicios, intervalo, actividad relacionada y puntos sin visibilidad. Explicar cualquier ampliación del alcance.

## Evidencias

Asignar identificadores estables y enlazar fragmentos revisados mediante rutas relativas. Conservar los originales en almacenamiento privado. Cada evidencia publicada debe indicar procedencia y cambios realizados para retirar información sensible.

| ID de evidencia | Fuente e ID de evento | Archivo y localizador del registro | Qué demuestra | Limitaciones o datos retirados |
| --- | --- | --- | --- | --- |
| Por completar | Por completar | Por completar | Por completar | Por completar |

Registrar consulta, intervalo de búsqueda, zona horaria, método de recuento y eliminación de duplicados. Diferenciar eventos, alertas e intentos únicos; conservar los ID necesarios para relacionar fuentes. Calcular el hash después de retirar datos sensibles e indicar el algoritmo: ese valor identifica el archivo publicado, no el original privado.

## Línea de tiempo

| Fecha y hora UTC | Equipo o actor | Evento observado | ID de evidencia | Interpretación e incertidumbre |
| --- | --- | --- | --- | --- |
| Por completar | Por completar | Por completar | Por completar | Por completar |

Ordenar por hora del evento y conservar la hora de ingestión si aporta contexto. Explicar vacíos, desfases, efectos de instantáneas y contradicciones entre fuentes.

## Indicadores

| Tipo | Valor sin datos sensibles | Contexto o función | Fuente y fecha de enriquecimiento | Resultado y confianza |
| --- | --- | --- | --- | --- |
| Por completar | Por completar | Por completar | Por completar | Por completar |

Una IP interna, una cuenta o un proceso pueden orientar la investigación sin ser un indicador malicioso. Identificar dominios ficticios o reservados y consultas de reputación no realizadas. La falta de información de reputación no demuestra que algo sea benigno.

En phishing, revisar From, Reply-To, Return-Path, cadena Received, resultados confiables de SPF/DKIM/DMARC, URL y dominios no navegables, hashes y metadatos de adjuntos. Diferenciar encabezados sintéticos, datos insertados por el remitente y resultados verificados por infraestructura de confianza. Mantener el contenido confidencial fuera de servicios externos de enriquecimiento.

En honeypot registrar GeoIP/ASN, reverse DNS, RDAP/reputación opcionales, first/last seen internos y frecuencia con fuente, fecha, resultado, confianza y limitación. No ejecutar payloads, visitar URL maliciosas ni enviar datos privados a terceros. Enriquecimiento [seguro y opcional](../enrichment/README.md).

> Geographic information represents the estimated location of the observed source IP address and does not establish the physical location or identity of an attacker.

## MITRE ATT&CK

Registrar táctica, ID de técnica o subtécnica, referencia oficial y comportamiento concreto que respalda la correspondencia. Usar «no aplica» con una explicación cuando la evidencia no permita asociar una técnica. ATT&CK describe comportamiento; no determina por sí solo si hubo una intrusión. La atribución de robo de credenciales, persistencia o mando y control requiere evidencia suficiente.

## Análisis

Relacionar las evidencias y explicar la secuencia, las alternativas y la información que falta. Incluir los campos relevantes de los registros. En autenticación, separar fallos, bloqueos y éxitos posteriores. En AWS responder **quién → qué → cuándo → desde dónde → contra qué recurso → qué cambió**, con resultado de la API, errores y estado anterior y posterior cuando esté disponible.

## Clasificación

Elegir una categoría después del análisis y justificarla con evidencia y contexto de autorización:

- **Verdadero positivo (True Positive):** se sostiene el comportamiento malicioso o no autorizado que busca la detección. Si es una simulación, dejar explícitos el escenario y su resultado esperado de referencia.
- **Falso positivo (False Positive):** la condición señalada por la detección no está respaldada por los hechos; explicar la discrepancia.
- **Positivo benigno (Benign Positive):** el comportamiento se detectó correctamente y estaba autorizado o era esperado.
- **No concluyente (Inconclusive):** faltan datos o existen contradicciones; indicar qué información hace falta.

Registrar por separado el resultado de la regla: **sin probar / activada según lo esperado / brecha de detección**. Una regla puede funcionar correctamente durante una prueba autorizada y el caso clasificarse como positivo benigno.

Para telemetría de Internet registrar además la categoría de actividad (Internet Noise, Reconnaissance, Port Scan, Credential Brute Force, Distributed Brute Force, Traffic Spike, Suspected DoS o Confirmed DDoS) cuando haya base, separada de la clasificación de la regla/caso. Aplicar los [criterios de red y evidencia](../dashboards/network-anomalies/README.md): múltiples IP o muchos eventos no confirman DDoS. No clasificar por obligación si la evidencia es insuficiente.

## Severidad

Justificar la severidad según impacto observado, privilegios y criticidad del objetivo, alcance, acciones exitosas o fallidas e incertidumbre. Conservar por separado el nivel original del SIEM y explicar cualquier ajuste. Un recuento elevado de fallos no demuestra acceso exitoso.

## Decisión

Elegir **cerrar** o **escalar** cuando haya base suficiente. Explicar motivo, responsable o rol receptor, urgencia, evidencias que se entregan y preguntas pendientes. Distinguir una solicitud de contención de una acción realmente ejecutada.

## Acciones recomendadas

Separar contención inmediata, investigación adicional, remediación y prevención. Indicar responsable y estado de ejecución. Una recomendación L1 no equivale a autorización para deshabilitar cuentas o aislar equipos. En las simulaciones, documentar la retirada de artefactos de prueba, la restauración de cambios y su comprobación.

## Lecciones aprendidas y mejora de detecciones

Registrar carencias de recopilación, hipótesis descartadas, ajustes propuestos y falsos positivos previsibles. Enlazar las reglas y los procedimientos modificados. Anotar resultados reales de controles positivos y negativos, y brechas que continúan abiertas. Una mejora se considera validada después de probarla.
