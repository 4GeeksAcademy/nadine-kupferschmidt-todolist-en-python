# Gestor de Tareas (CLI en Python)

## Descripción

Herramienta de terminal para que un equipo de operaciones de logística gestione tareas pendientes.

## Funcionalidades

- Agrega tareas con un título no vacío.
- Muestra las tareas pendientes numeradas.
- Elimina una tarea mediante el número que aparece en la lista.
- Guarda las tareas en `todos.csv` y las carga desde ese archivo.
- Al iniciar, intenta cargar las tareas guardadas. Al salir, ofrece guardar si hay cambios sin guardar.

## Cómo usarlo

Iniciá el programa desde la terminal con:

```bash
python3 app.py
```

Usá las opciones del menú para agregar, eliminar, ver, guardar o cargar tareas. Elegí la opción 6 o escribí `salir` para terminar. Al agregar o eliminar, podés escribir `v` para volver al menú.

## Cómo correr las pruebas

Ejecutá las pruebas desde la terminal con:

```bash
python3 test.py
```

## Estructura del proyecto

- `app.py`: aplicación de gestión de tareas y menú de terminal.
- `test.py`: pruebas automatizadas.
- `.gitignore`: excluye archivos generados, incluido `todos.csv`.
- `todos.csv`: archivo de tareas que se crea al guardar; no se sube al repositorio.

## Tecnologías

Python y solo módulos de la biblioteca estándar. La aplicación usa el módulo `csv` para guardar y cargar tareas.
