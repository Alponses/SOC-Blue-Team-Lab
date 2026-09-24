# Detecciones de Wazuh

**Objetivo:** Crear reglas y decodificadores a partir de eventos reales de las fuentes verificadas, separando simulaciones de actividad no solicitada.

La integración del honeypot se reservará en [configs/honeypot/wazuh](../../configs/honeypot/wazuh/README.md), como fuente única de sus configuraciones; aquí se enlazarán las pruebas. No se escribirá lógica Cowrie hasta inspeccionar eventos de la versión elegida y validar campos, unidades y origen. Ninguna regla honeypot está implementada en 0.5.

**Avance:** reglas pendientes de creación, carga y validación.

## Comprobaciones previstas

Registrar versión de Wazuh, ID de reglas personalizadas, campos y decodificadores necesarios, pruebas de reglas y resultados de ingestión de extremo a extremo. La prueba de una regla y la llegada del evento al panel se verificarán por separado.

Cada regla seguirá los [criterios de documentación](../README.md), con objetivo, fuente, lógica, ATT&CK, verdaderos positivos esperados, falsos positivos, procedimiento de prueba y resultados. Los fallos de detección quedarán registrados junto al caso que motivó la regla.
