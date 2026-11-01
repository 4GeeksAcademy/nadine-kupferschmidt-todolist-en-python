# Módulo estándar para trabajar con archivos CSV.
import csv

# Lista global donde se guardarán las tareas.
todos = []


# Devuelve la lista actual de tareas.
def get_todos():
    return todos


# Agrega una tarea si el título no está vacío.
def add_one_task(title):
    title = title.strip()
    if title == "":
        print("La tarea no puede estar vacía.")
        return
    todos.append(title)
    print("Tarea agregada exitosamente.")


# Muestra las tareas numeradas o avisa si la lista está vacía.
def print_list():
    if len(todos) == 0:
        print("No hay tareas pendientes.")
    else:
        # Recorre las tareas y las numera desde 1.
        for numero, tarea in enumerate(todos, start=1):
            print(f"{numero}. {tarea}")


# Elimina una tarea usando el número que ve la persona.
def delete_task(number_to_delete):
    try:
        numero = int(number_to_delete)
    except (ValueError, TypeError):
        print("Por favor, escribí un número válido.")
        return

    if numero < 1 or numero > len(todos):
        print("No existe una tarea con ese número.")
        return

    # Ajusta el número al índice de Python y elimina la tarea.
    tarea_eliminada = todos.pop(numero - 1)
    print("Tarea eliminada: " + tarea_eliminada)


# Guarda cada tarea en una fila de todos.csv.
def save_todos():
    with open("todos.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        for tarea in todos:
            escritor.writerow([tarea])
    print("Tareas guardadas en todos.csv.")


# Carga las tareas guardadas en todos.csv.
def load_todos():
    try:
        with open("todos.csv", "r", newline="", encoding="utf-8") as archivo:
            todos.clear()
            lector = csv.reader(archivo)
            for fila in lector:
                # Ignora las filas que no tienen contenido.
                if fila and fila[0]:
                    todos.append(fila[0])
    except FileNotFoundError:
        print("Todavía no hay un archivo todos.csv para cargar.")
        return

    if len(todos) == 1:
        print("Se cargó 1 tarea.")
    else:
        print(f"Se cargaron {len(todos)} tareas.")


# Ejecuta el menú solo cuando este archivo se inicia directamente.
if __name__ == "__main__":
    salir = False
    load_todos()
    ultima_version_guardada = list(get_todos())
    while not salir:
        print("""
══════════════════════════════════
         GESTOR DE TAREAS
══════════════════════════════════
  1. Agregar una tarea
  2. Eliminar una tarea
  3. Ver la lista de tareas
  4. Guardar tareas en todos.csv
  5. Cargar tareas desde todos.csv
  6. Salir (o escribí 'salir')
──────────────────────────────────
""")
        respuesta = input("Elegí una opción (1-6): ").strip()

        if respuesta == "6" or respuesta.lower() == "salir":
            if get_todos() != ultima_version_guardada:
                guardar_antes_de_salir = input(
                    "Tenés cambios sin guardar. ¿Querés guardar antes de salir? (s/n): "
                ).strip().lower()
                if guardar_antes_de_salir == "s":
                    save_todos()
            print("¡Hasta luego!")
            salir = True
        elif respuesta == "1":
            print("--- Agregar tarea ---")
            print("(escribí 'v' para volver al menú)")
            titulo = input("¿Cuál es el título de la tarea? ")
            if titulo.strip().lower() != "v":
                add_one_task(titulo)
            print("---------------------")
            input("Presioná Enter para volver al menú...")
        elif respuesta == "2":
            print("--- Eliminar tarea ---")
            print_list()
            if len(get_todos()) > 0:
                print("(escribí 'v' para volver al menú)")
                numero = input("¿Qué número de tarea querés eliminar? ")
                if numero.strip().lower() != "v":
                    delete_task(numero)
            print("---------------------")
            input("Presioná Enter para volver al menú...")
        elif respuesta == "3":
            print("--- Tus tareas ---")
            print_list()
            print("---------------------")
            input("Presioná Enter para volver al menú...")
        elif respuesta == "4":
            print("--- Guardar tareas ---")
            save_todos()
            ultima_version_guardada = list(get_todos())
            print("---------------------")
            input("Presioná Enter para volver al menú...")
        elif respuesta == "5":
            print("--- Cargar tareas ---")
            if get_todos() != ultima_version_guardada:
                cargar_igual = input(
                    "Tenés cambios sin guardar que se van a perder. ¿Querés cargar igual? (s/n): "
                ).strip().lower()
                if cargar_igual == "s":
                    load_todos()
                    ultima_version_guardada = list(get_todos())
                else:
                    print("Carga cancelada.")
            else:
                load_todos()
                ultima_version_guardada = list(get_todos())
            print("---------------------")
            input("Presioná Enter para volver al menú...")
        else:
            print("Opción inválida, probá de nuevo.")
            input("Presioná Enter para volver al menú...")
