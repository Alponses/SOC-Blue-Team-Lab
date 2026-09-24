# Procedimientos de investigación SOC

Los procedimientos servirán para decidir qué comprobar primero, qué registros consultar y cuándo cerrar o escalar un caso. **Avance:** plantilla preparada; procedimientos específicos pendientes.

Se desarrollarán en la etapa 8 a partir de los casos investigados, utilizando la [plantilla SOC](../templates/soc-playbook.md). Los apartados de phishing y AWS se validarán después de ejecutar sus respectivas investigaciones.

| Procedimiento previsto | Pregunta principal |
| --- | --- |
| Fuerza bruta | ¿Los fallos eran esperados y hubo un acceso exitoso posterior? |
| PowerShell sospechoso | ¿Qué se ejecutó, quién lo hizo, con qué autorización y qué efecto tuvo? |
| Inicio de sesión sospechoso | ¿El origen, el método, la cuenta y el horario corresponden a un acceso autorizado? |
| Cambios de cuentas o privilegios | ¿Quién modificó la identidad o sus permisos y estaba aprobado? |
| Phishing | ¿Qué demuestran los encabezados confiables y el contenido, y hubo interacción? |
| Escaneo de red | ¿El patrón corresponde a un inventario aprobado o a una exploración sospechosa? |
| Conexión saliente sospechosa | ¿Qué proceso contactó con qué destino y qué justifica escalar? |
| Actividad IAM en AWS | ¿Qué principal o sesión realizó qué cambio de API y sobre qué recurso? |

Cada procedimiento incluirá comprobaciones iniciales, fuentes y campos concretos, consultas, enriquecimiento, explicaciones benignas frecuentes, criterios de escalamiento y requisitos de cierre. Los enlaces a casos y comandos se incorporarán cuando estén disponibles y revisados.
