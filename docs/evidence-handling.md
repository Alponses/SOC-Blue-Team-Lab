# Manejo de evidencias

El objetivo es conservar suficiente información para reproducir una investigación y explicar sus conclusiones, sin publicar secretos ni datos personales. Hasta ahora está definido el procedimiento; la recopilación de evidencias operativas comenzará con el despliegue del laboratorio.

## Procedencia y almacenamiento

Los registros originales, correos completos, capturas de paquetes, credenciales, exportaciones y tablas de correspondencia entre identidades reales y ficticias se guardarán fuera del repositorio, en almacenamiento privado. Las exclusiones de `private/`, `raw/` y `exports/` son una protección adicional. `.gitignore` no protege archivos ya versionados ni incorporados a la fuerza.

Cada investigación publicará únicamente los fragmentos necesarios para respaldar sus hallazgos, dentro de su subdirectorio `evidence/`. El inventario de evidencias incluirá fuente, fecha de recopilación, zona horaria original, consulta o método de exportación, versión de la fuente, datos eliminados, localizadores de registros y SHA-256 del archivo publicado. Todavía no hay muestras recopiladas.

Los alias y direcciones sustituidos deberán ser coherentes en todo el caso para conservar la correlación. Si se desplazan las fechas, se explicará el ajuste y se preservarán el orden y los intervalos. Se mantendrán las diferencias entre actor y cuenta afectada, y entre origen y destino. Los campos ausentes quedarán identificados como tales.

La procedencia se registrará como simulación observada en el laboratorio, exportación de evidencia observada con datos sensibles retirados, o muestra sintética de entrenamiento. Un correo sintético permite practicar análisis, pero no demuestra que una regla desplegada haya detectado un evento real.

## Revisión de datos sensibles

La revisión cubrirá JSON anidado, líneas de comandos, bloques de scripts, URL y parámetros, encabezados de correo, capturas y metadatos. Se eliminarán contraseñas, credenciales, tokens, claves de acceso, cookies, claves privadas, identificadores reales de cuentas y ARN, correos y usuarios personales, direcciones de infraestructura pública y rutas ajenas al caso. Los originales y las correspondencias permanecerán privados.

Se utilizarán identidades ficticias y dominios reservados como `soc.test` o `example.invalid`. Las URL de phishing se escribirán de forma no navegable. Las consultas de reputación indicarán servicio, fecha, resultado y alcance de lo compartido; si no se realizan, se dejará constancia. Un dominio reservado no permite obtener una conclusión útil sobre reputación de infraestructura real.

VirusTotal, URLScan y servicios similares no recibirán material confidencial. Una consulta pública puede revelar el indicador o el archivo. Se priorizará el análisis local y el uso de muestras de entrenamiento, sin visitar enlaces sospechosos.

Los registros completos, imágenes de máquinas virtuales, ISO, binarios y capturas de paquetes quedan fuera de Git. Se prefieren fragmentos JSON/CSV/TXT revisados. Como criterio de selección, cada fragmento de texto debería ocupar como máximo 1 MiB y cada imagen 2 MiB. Estos límites se revisan al preparar la publicación; `.gitignore` no controla tamaños.

## Revisión antes de publicar

- [ ] Las conclusiones tienen evidencias; los planes, las muestras sintéticas y los puntos sin validar están identificados.
- [ ] No hay credenciales, claves, cookies, datos personales, objetivos públicos, binarios maliciosos, imágenes de máquinas virtuales ni capturas sensibles.
- [ ] Los fragmentos son pequeños, relevantes y coherentes; incluyen procedencia y localizadores.
- [ ] Las capturas tienen descripción y se han revisado interfaz, pestañas, metadatos e información personal.
- [ ] Se han ejecutado `python3 scripts/validate_repository.py` y `git diff --check`.
- [ ] Se han revisado `git status --short`, `git diff --cached --stat` y `git diff --cached` antes del commit.
- [ ] Se han revisado el historial y los metadatos de autor antes de publicar. Eliminar un secreto en un commit posterior no lo borra del historial.
- [ ] Se ha utilizado un analizador de secretos antes de publicar evidencias reales, además de la revisión manual.

El repositorio sigue siendo local. El commit inicial utiliza una identidad genérica del proyecto y una dirección de correo reservada para no incluir datos personales.
