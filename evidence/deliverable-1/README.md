# Evidencia del entregable 1

**CONTROLLED TELEMETRY: validación benigna, sin incidentes ni ataques.** Únicamente se ha observado el [preflight del host](preflight.md). No existen capturas ni logs de Windows/Wazuh recopilados. Las fichas siguientes son registros pendientes, no muestras de eventos.

| Fuente | Ficha | Evidencia operativa |
| --- | --- | --- |
| Security | [security.md](security.md) | No recopilada |
| System | [system.md](system.md) | No recopilada |
| Sysmon | [sysmon.md](sysmon.md) | No recopilada |
| PowerShell | [powershell.md](powershell.md) | No recopilada |
| Defender | [defender.md](defender.md) | No recopilada |

Aplicar [manejo de evidencias](../../docs/evidence-handling.md). Los originales van fuera de Git. Publicar solo extractos mínimos revisados; incluir nombre de archivo, consulta/método, versión, fecha de recopilación UTC, zona original, transformaciones, localizador y SHA-256 de cada archivo publicado. Calcular hash con `Get-FileHash -Algorithm SHA256` o `shasum -a 256` después de sanitizar. No convertir un ejemplo documental en evidencia observada.

Para pruebas del operador, la taxonomía existente usa **Evidence Origin: Controlled Simulation**; en esta etapa significa validación normal autorizada, no una simulación de ataque. El preflight es evidencia de ingeniería del host, sin incidente asociado. No abrir/cerrar SOC-001–SOC-015.

## Cadena exigida por fuente

Cada ficha debe enlazar a: evento local → configuración efectiva/estado del agente → evento correlacionado en manager → documento en indexer/Discover. Un screenshot es opcional y debe explicar fuente, consulta/ventana, qué prueba y qué no prueba. No publicar capturas decorativas ni pestañas/credenciales ajenas al lab. Usar `screenshots/deliverable-1/` solo cuando haya capturas reales revisadas.

Los nombres de archivos se elegirán al recopilar (por ejemplo, fuente, UTC y RecordID reales); no se han creado JSON, timestamps ni IDs de eventos ficticios. Un `No verificado` expresa falta de ejecución, no la demostración de que un canal esté vacío.

## Snapshots

Conservar la convención existente `SOC-<equipo>-<checkpoint>`. **Ninguno creado en esta sesión.** Cuando se ejecute, anotar nombre real, UUID, UTC, estado de VM, motivo y salida de `VBoxManage snapshot <VM> list --machinereadable`, sanitizada. Snapshots/VM fuera de Git.

| VM | Nombre previsto | Momento | Nombre/UUID/UTC observado |
| --- | --- | --- | --- |
| SOC-WAZUH | SOC-WAZUH-base-install | Ubuntu/red actualizados, antes de Wazuh | Pendiente |
| SOC-WIN11 | SOC-WIN11-clean-install | Windows/Defender actualizados, antes del agente | Pendiente |
| SOC-WAZUH | SOC-WAZUH-wazuh-operational | Servicios comprobados, antes de archives | Pendiente |
| SOC-WIN11 | SOC-WIN11-wazuh-agent | Enrollment comprobado, antes de Sysmon/logging | Pendiente |
| SOC-WIN11 | SOC-WIN11-sysmon-configured | XML aceptado y canal local disponible, antes de validar toda la cadena | Pendiente |
| Ambas, por separado | SOC-WAZUH-deliverable-1-validated / SOC-WIN11-deliverable-1-validated | Solo tras aceptación completa y cierre de ventana | Pendiente |

Si una configuración importante adicional no tiene checkpoint previo, crear otro nombre descriptivo y registrarlo. Restaurar puede alterar relojes y enrollment; revalidar ambos y no usar snapshots como sustituto de backups privados.
