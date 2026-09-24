# Ingeniería de detecciones

El objetivo es convertir los hallazgos de las investigaciones en reglas que aporten contexto útil al analista. **Avance:** estructura y criterios definidos; reglas pendientes de implementación y validación.

Las primeras reglas podrán surgir durante cada investigación. La etapa 8 consolidará su cobertura y las pruebas. La recepción de un evento y la activación de una alerta se comprobarán por separado.

| Directorio | Contenido previsto |
| --- | --- |
| [Wazuh](wazuh/README.md) | Reglas y decodificadores necesarios, entradas sin datos sensibles y resultados observados |
| [Sigma](sigma/README.md) | Lógica portable con fuentes, campos y motores de destino identificados |
| [Suricata](suricata/README.md) | Reglas IDS comprobadas sobre la ruta real del tráfico del laboratorio |

## Documentación de cada regla

- Objetivo, fuente y campos necesarios.
- Lógica, umbral, intervalo y agrupación.
- Correspondencia con ATT&CK y evidencia que la justifica.
- Verdaderos positivos esperados y posibles falsos positivos.
- Versiones de regla y motor, entrada de prueba y pasos de validación.
- Resultado esperado y observado, control negativo y pruebas de umbral cuando correspondan.
- Limitaciones y enlace al caso que motivó la regla.

Si falta una alerta esperada, se conservará el resultado como **brecha de detección (Detection Gap)** y se investigará antes de dar por validada la regla.
