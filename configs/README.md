# Configuraciones del laboratorio

Este directorio reunirá las configuraciones necesarias para reproducir la recopilación y las pruebas. **Avance:** carpetas preparadas; todavía no hay configuraciones desplegadas.

| Directorio | Contenido previsto | Etapa |
| --- | --- | --- |
| [wazuh](wazuh/) | Recopilación del servidor y los agentes, retención y comprobaciones | Desde la 1 |
| [windows](windows/) | Auditoría, registro PowerShell, filtros Sysmon y canales del agente | 1 |
| [linux](linux/) | Autenticación, diario del sistema, auditoría, SSH y ruta de prueba FIM | 2 |
| [suricata](suricata/) | Interfaz de captura y selección de salida EVE | 6 |
| [active-directory](active-directory/) | Identidades, DNS, auditoría y procedimientos de cambio | 7 |
| [honeypot](honeypot/README.md) | Cowrie y Wazuh del pipeline público, con frontera independiente; solo requisitos por ahora | HP-1–HP-3, después de 0.5 y 1 |
| [aws](aws/) | Registro e IAM del laboratorio sin credenciales ni identificadores reales | 10 |

Cada archivo indicará versión, propósito y comprobaciones realizadas. Los secretos se sustituirán por marcadores y sus valores se introducirán de forma privada. Las claves de registro de agentes, contraseñas, claves de nube y certificados privados permanecerán fuera de Git. El informe de la etapa dejará constancia de qué configuración se aplicó y con qué resultado.
