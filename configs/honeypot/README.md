# Configuraciones del honeypot

**Estado: requisitos de diseño; sin archivos operativos, claves ni servicios desplegados.**

| Directorio | Alcance futuro |
| --- | --- |
| [cowrie](cowrie/README.md) | Emulación, JSON, seguridad del proceso y límites de almacenamiento |
| [wazuh](wazuh/README.md) | Ingestión local, contrato de campos, parsing, normalización y reglas verificadas |

El transporte, firewall y Suricata público se documentarán aquí con versión, propósito, ubicación, entradas permitidas y pruebas al implementar HP-1–HP-3. No sustituirán las configuraciones del laboratorio controlado. Las reglas de Cowrie tendrán una única fuente versionada en `configs/honeypot/wazuh/`; [detections/wazuh](../../detections/wazuh/README.md) enlazará su documentación de validación, sin copias divergentes.

Endpoints reales, claves, contraseñas y certificados privados permanecerán fuera de Git. Una configuración de ejemplo no se considerará aplicada hasta guardar evidencia de su comprobación. Seguir [seguridad](../../honeypot/security-model.md) y [transporte](../../honeypot/telemetry-pipeline.md).
