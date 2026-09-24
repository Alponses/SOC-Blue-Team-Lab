# Detecciones de Suricata

**Objetivo:** Detectar comportamientos de red relevantes para los casos del laboratorio.

**Avance:** reglas pendientes de creación, carga y validación.

La cobertura del laboratorio se conserva. Para el entorno público, revisar [Suricata y punto de observación](../../honeypot/suricata-visibility.md); las reglas necesitarán tráfico realmente visible y origen diferenciado. SOC-LINUX no observa automáticamente el VPS y una alerta no confirma DDoS.

## Comprobaciones previstas

Registrar SID y revisión, protocolo y dirección del flujo, variables, umbrales, versión, comprobación de sintaxis, cobertura de captura y resultados de tráfico positivo y negativo. La activación ante un escaneo deberá comprobarse con las reglas realmente instaladas.

Cada regla seguirá los [criterios de documentación](../README.md), con objetivo, fuente, lógica, ATT&CK, verdaderos positivos esperados, falsos positivos, procedimiento de prueba y resultados. Los fallos de detección quedarán registrados junto al caso que motivó la regla.
