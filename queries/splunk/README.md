# Investigaciones con Splunk y SPL

El objetivo de esta etapa es analizar los datos obtenidos en el laboratorio mediante SPL y comparar las búsquedas con las investigaciones realizadas en Wazuh.

**Avance:** alcance definido para el entregable 11; instalación, importaciones y consultas pendientes. Wazuh seguirá siendo el SIEM principal. La práctica prevista corresponde a Splunk Enterprise y SPL; Splunk Enterprise Security no se ha utilizado.

| Consulta prevista | Propósito |
| --- | --- |
| Fallos de autenticación | Contar fallos por cuenta, origen y equipo en un intervalo definido, considerando duplicados |
| Acceso exitoso después de varios fallos | Reconstruir la secuencia ordenada para la misma cuenta y origen relevante; una suma sin orden temporal no basta |
| PowerShell sospechoso | Revisar comandos y bloques de script con contexto de proceso, padre y usuario |
| Creación de cuentas | Identificar actor, identidad creada, equipo y acciones posteriores relacionadas |
| Cambios de privilegios | Identificar grupo o privilegio anterior y posterior, actor, cuenta afectada y autorización |
| Escaneo de red | Evaluar puertos y equipos de destino distintos y sus tiempos, considerando tareas de inventario conocidas |
| Análisis DNS | Relacionar consultas, respuestas, equipo solicitante, proceso disponible y resultado |

Cada consulta incluirá objetivo, tipo de fuente, correspondencia de campos, procedencia de los datos, interpretación de tiempos y zona horaria, intervalo, SPL, utilidad, resultado esperado, resultado observado y limitaciones. Los campos CIM y los modelos de Enterprise Security solo podrán utilizarse si se han configurado y verificado.

Los datos importados serán fragmentos del laboratorio revisados y sin información sensible. Se conservarán los campos necesarios para reproducir la correlación y se documentarán las transformaciones y los recuentos de importación.
