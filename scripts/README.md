# Validación del repositorio

El script comprueba los enlaces internos de la documentación. Se ejecuta desde la raíz del repositorio con Python 3.9 o posterior y Git:

```sh
python3 scripts/validate_repository.py
git diff --check
```

Revisa archivos Markdown versionados y archivos nuevos no excluidos por Git. Comprueba destinos de archivo o directorio, rutas dentro del repositorio y anclas de encabezados con el formato de GitHub, incluidas repeticiones. Omite los bloques de código. Devuelve un código distinto de cero si encuentra enlaces rotos o falta el contexto Git.

La documentación utiliza enlaces Markdown en línea. Los enlaces por referencia, las anclas HTML y las construcciones menos habituales necesitarían ampliar el analizador. El script no comprueba URL externas, representación visual de Mermaid, secretos ni funcionamiento del laboratorio.

**Avance:** validador disponible y utilizado en la revisión documental. Los scripts de instalación y simulación se prepararán en las etapas correspondientes; su ejecución operativa sigue pendiente.
