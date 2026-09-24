# Procedimiento SOC — Nombre del escenario

Plantilla para convertir un tipo de alerta en una secuencia de comprobaciones y decisiones. Su validación operativa queda pendiente hasta ejecutar el escenario y revisar los resultados.

| Campo | Contenido |
| --- | --- |
| Objetivo y activación | Alerta u observación concreta y resultado que debe obtener el analista |
| Alcance y responsable | Equipos permitidos y rol encargado |
| Acceso necesario | Permisos de lectura, índices, herramientas y limitaciones |
| Requisitos de registros | Fuentes, comprobación de recopilación, campos e intervalo |
| Documentos relacionados | Enlaces a casos, consultas y detecciones existentes |
| Validación | Versiones, fecha, resultados observados y alias del revisor |

## Primeras comprobaciones

- [ ] Conservar alerta original, regla y versión, hora del evento y referencia de evidencia.
- [ ] Confirmar equipo, usuario, privilegio, criticidad e impacto observado.
- [ ] Revisar actualización de registros, zonas horarias, desfases, duplicados y fuentes ausentes.
- [ ] Consultar cambios autorizados, registro de simulaciones y casos relacionados.
- [ ] Aplicar los criterios de escalamiento inmediato sin retrasarlos por enriquecimiento opcional.

## Registros y campos

| Pregunta por resolver | Fuente, canal o índice exacto | Campos necesarios | Consulta o búsqueda relacionada | Limitaciones |
| --- | --- | --- | --- | --- |
| Por completar | Por completar | Por completar | Por completar | Por completar |

## Investigación

- [ ] Definir el intervalo inicial y justificar cualquier ampliación.
- [ ] Relacionar origen y destino, actor y cuenta afectada, proceso y padre, éxitos y fallos según el caso.
- [ ] Revisar otros equipos o usuarios y actividad exitosa anterior o posterior.
- [ ] Eliminar duplicados y distinguir eventos de alertas agregadas.
- [ ] Crear una línea de tiempo UTC con ID de evidencia e incertidumbres.
- [ ] Comparar la explicación principal con una alternativa basada en hechos.

## Enriquecimiento

- [ ] Identificar indicadores internos, sintéticos, reservados o públicos.
- [ ] Consultar primero inventario, rol del usuario, ventana de cambio, servicio conocido, hash y firma.
- [ ] Registrar servicio, fecha, resultado y confianza cuando corresponda una consulta externa.
- [ ] Mantener archivos confidenciales, URL privadas completas, encabezados, tokens y hashes sensibles fuera de servicios externos. Utilizar muestras sintéticas o dejar constancia de la consulta no realizada.

## Falsos positivos y actividad benigna

| Explicación alternativa | Evidencia para confirmarla | Cuándo no basta para cerrar |
| --- | --- | --- |
| Por completar | Por completar | Por completar |

La inclusión de un usuario o una IP en una lista permitida debe acompañarse de una comprobación del contexto.

## Criterios de escalamiento

Definir umbrales y evidencias propios del escenario. Considerar acceso exitoso tras fallos sospechosos, cambios inesperados de privilegios, impacto confirmado, ampliación del alcance y vacíos relevantes de evidencia.

| Condición | Prioridad y rol receptor | Evidencia mínima y preguntas pendientes | Acción permitida a L1 |
| --- | --- | --- | --- |
| Por completar | Por completar | Por completar | Por completar |

La contención requiere la autoridad operativa correspondiente. En el laboratorio, los cambios se limitarán a los equipos definidos en el procedimiento de simulación.

## Clasificación y cierre

- [ ] Elegir verdadero positivo, falso positivo, positivo benigno o no concluyente con respaldo en evidencias.
- [ ] Separar el resultado de la prueba de detección de la clasificación del caso.
- [ ] Justificar severidad, cierre o escalamiento y seguimiento recomendado.
- [ ] Registrar responsable, contenido de la entrega y próxima revisión si quedan asuntos abiertos.
- [ ] Confirmar limpieza, remediación y ausencia de actividad pendiente de explicación.
- [ ] Adjuntar evidencias revisadas y línea de tiempo con la estructura del informe de incidente.

## Validación y mejora

- [ ] Ejecutar control positivo, control benigno o negativo y prueba de umbral cuando corresponda.
- [ ] Registrar resultados y limitaciones; una alerta esperada ausente queda como **brecha de detección (Detection Gap)**.
- [ ] Actualizar consultas, requisitos de recopilación y criterios de escalamiento según lo observado.
