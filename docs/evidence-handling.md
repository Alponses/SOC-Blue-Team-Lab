# Manejo de evidencias

El objetivo es conservar suficiente información para reproducir una investigación y explicar sus conclusiones, sin publicar secretos ni datos personales. Hasta ahora está definido el procedimiento; la recopilación de evidencias operativas comenzará con el despliegue del laboratorio.

## Evidence Origin

Cada ficha e informe de incidente debe declarar **Evidence Origin:** cerca del inicio con exactamente uno de estos valores. Una ficha pendiente indica la fuente requerida; no acredita que ya exista evidencia.

| Valor permitido | Uso |
| --- | --- |
| Controlled Simulation | Actividad autorizada generada en el laboratorio o pruebas del operador, incluidas pruebas Cowrie |
| Observed Honeypot Telemetry | Actividad no solicitada de Internet realmente observada en el sensor dedicado |
| Synthetic Training Sample | Correo o datos construidos para entrenamiento y declarados sintéticos |
| Sanitized Cloud Activity | Extractos revisados de actividad de nube; documentar si fue generada de forma controlada |

SOC-001–SOC-010 conservan su condición de investigaciones CONTROLLED LAB. SOC-001–SOC-008 usarán `Controlled Simulation`, SOC-009 `Synthetic Training Sample` y SOC-010 `Sanitized Cloud Activity` en cuenta propia con actividad controlada. SOC-011 y posteriores requerirán `Observed Honeypot Telemetry` salvo excepción explícita documentada. No renumerar ni reclasificar las simulaciones como ataques de Internet.

`CONTROLLED TELEMETRY` y `OBSERVED INTERNET TELEMETRY` son las etiquetas de entorno/actividad. El origen se mantiene al sanitizar o reproducir un extracto; su reproducción para probar detecciones debe registrarse aparte y excluirse de métricas operativas. En casos con fuentes mixtas, declarar origen principal y procedencia individual en el inventario sin mezclar conclusiones.

Observed Internet activity does not imply compromise of a production environment. Una autenticación aceptada o comando dentro de Cowrie demuestra interacción emulada, no compromiso del host ni de producción.

## Procedencia y almacenamiento

Los registros originales, correos completos, capturas de paquetes, credenciales, exportaciones y tablas de correspondencia entre identidades reales y ficticias se guardarán fuera del repositorio, en almacenamiento privado. Las exclusiones de `private/`, `raw/` y `exports/` son una protección adicional. `.gitignore` no protege archivos ya versionados ni incorporados a la fuerza.

Cada investigación publicará únicamente los fragmentos necesarios para respaldar sus hallazgos, dentro de su subdirectorio `evidence/`. El inventario de evidencias incluirá fuente, fecha de recopilación, zona horaria original, consulta o método de exportación, versión de la fuente, datos eliminados, localizadores de registros y SHA-256 del archivo publicado. Todavía no hay muestras recopiladas.

Los alias y direcciones sustituidos deberán ser coherentes en todo el caso para conservar la correlación. Si se desplazan las fechas, se explicará el ajuste y se preservarán el orden y los intervalos. Se mantendrán las diferencias entre actor y cuenta afectada, y entre origen y destino. Los campos ausentes quedarán identificados como tales.

La procedencia se registrará con los valores exactos de [Evidence Origin](#evidence-origin), y la sanitización se documentará por separado sin cambiar el origen. Un correo sintético permite practicar análisis, pero no demuestra que una regla desplegada haya detectado un evento real.

## Revisión de datos sensibles

La revisión cubrirá JSON anidado, líneas de comandos, bloques de scripts, URL y parámetros, encabezados de correo, capturas y metadatos. Se eliminarán contraseñas, credenciales, tokens, claves de acceso, cookies, claves privadas, identificadores reales de cuentas y ARN, correos y usuarios personales, direcciones de infraestructura pública y rutas ajenas al caso. Los originales y las correspondencias permanecerán privados.

Se utilizarán identidades ficticias y dominios reservados como `soc.test` o `example.invalid`. Las URL de phishing se escribirán de forma no navegable. Las consultas de reputación indicarán servicio, fecha, resultado y alcance de lo compartido; si no se realizan, se dejará constancia. Un dominio reservado no permite obtener una conclusión útil sobre reputación de infraestructura real.

VirusTotal, URLScan y servicios similares no recibirán material confidencial. Una consulta pública puede revelar el indicador o el archivo. Se priorizará el análisis local y el uso de muestras de entrenamiento, sin visitar enlaces sospechosos.

Los registros completos, imágenes de máquinas virtuales, ISO, binarios y capturas de paquetes quedan fuera de Git. Se prefieren fragmentos JSON/CSV/TXT revisados. Como criterio de selección, cada fragmento de texto debería ocupar como máximo 1 MiB y cada imagen 2 MiB. Estos límites se revisan al preparar la publicación; `.gitignore` no controla tamaños.

## Telemetría pública y payloads

Los JSON originales Cowrie/EVE, recordings de sesión, credenciales, archivos recibidos, logs de transporte y PCAP permanecerán privados, fuera del repositorio. Definir responsable, acceso, cifrado, retención y eliminación antes de desplegar. Las carpetas ignoradas son una protección adicional, no un destino recomendado para raw dentro del repositorio.

La copia pública contendrá extractos mínimos con manifiesto en [datasets/sanitized-honeypot](../datasets/sanitized-honeypot/README.md) o evidencia enlazada del incidente, sin duplicar archivos divergentes. Registrar consulta, ventana, criterios de selección, cobertura, transformaciones y hash del archivo publicado. Un extracto no representa necesariamente todo el tráfico; calcular métricas en el corpus privado y declarar el alcance verificable.

Revisar origen/destino e infraestructura propia, usernames/passwords, comandos, URL y parámetros, nombres de archivos descargados, indicadores de payload, tokens y PII, incluidos mensajes, JSON anidado y copias del registro completo. Usar alias estables y conservar correspondencias privadas. No publicar contraseñas en bulk ni hashes simples que permitan recuperar secretos por diccionario. Comparaciones de credenciales necesarias para SOC-013 se realizarán de forma privada; publicar solo agregados o alias revisados.

No publicar enlaces maliciosos funcionales: retirar tokens y neutralizar esquemas/dominios como texto sin hipervínculos. No descargar un archivo para enriquecerlo, ejecutar binarios recibidos ni abrir automáticamente transcripciones o adjuntos hostiles. Los binarios maliciosos siempre quedan fuera de Git. Un PCAP completo requiere revisión explícita antes de considerarse para publicación; por defecto solo se usan fragmentos de texto seleccionados.

Enriquecer indicadores reales en privado antes de sustituir IP. Conservar fuente, query date, resultado, confianza y limitación. Nunca enviar automáticamente información privada, credenciales, sesiones completas ni archivos confidenciales a terceros. Seguir [enriquecimiento](../enrichment/README.md) y [seguridad del sensor](../honeypot/security-model.md).

> Geographic information represents the estimated location of the observed source IP address and does not establish the physical location or identity of an attacker.

## Revisión antes de publicar

- [ ] Evidence Origin aparece al inicio y corresponde a la fuente; las pruebas y replays están excluidos de métricas de observación.
- [ ] Las conclusiones tienen evidencias; los planes, las muestras sintéticas y los puntos sin validar están identificados.
- [ ] No hay credenciales, claves, cookies, datos personales, infraestructura propia expuesta, URL maliciosas funcionales, binarios maliciosos, imágenes de máquinas virtuales ni capturas sensibles.
- [ ] Los fragmentos son pequeños, relevantes y coherentes; incluyen procedencia y localizadores.
- [ ] Las capturas tienen descripción y se han revisado interfaz, pestañas, metadatos e información personal.
- [ ] Se han ejecutado `python3 scripts/validate_repository.py` y `git diff --check`.
- [ ] Se han revisado `git status --short`, `git diff --cached --stat` y `git diff --cached` antes del commit.
- [ ] Se han revisado el historial y los metadatos de autor antes de publicar. Eliminar un secreto en un commit posterior no lo borra del historial.
- [ ] Se ha utilizado un analizador de secretos antes de publicar evidencias reales, además de la revisión manual.

El repositorio sigue siendo local. El commit inicial utiliza una identidad genérica del proyecto y una dirección de correo reservada para no incluir datos personales.
