import json
import os
import time     #Importamos time para hacer pausas

#CONFIGURACION
NOMBRE_ARCHIVO = "tareas.json"

#FUNCIONES DE MANEJO DE DATOS
def cargar_tareas():
    """
    Intenta cargar las tareas desde el archivo Json.
    Si el archivo no existe, devuelve una lista vacia
    """
    try:
        with open(NOMBRE_ARCHIVO, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        #Si el archivo no existe, es la pñrimera vez que se usa el programa
        return []

def guardar_tareas(tareas):
    """Guarda la lista de tareas en el archivo Json"""
    with open(NOMBRE_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)
        
#FUNCIONES DE INTERACCION CON EL USUARIO
def mostrar_tareas(tareas):
    """Muestra la lista de las tareas formateada"""
    print("\n---    Lista de Tareas     ---")
    if not tareas:
        print("No hay tareas pendientes")
    else:
        #Enumerate nos da el indice empezando en 1 y la tarea
        for i, tarea in enumerate(tareas, 1):
            estado = "[X]" if tarea["completada"] else "[ ]"
            print(f"{estado} {i}. {tarea['descripcion']}")
    print("-------------------")

def anadir_tarea(tareas):
    """Pide una descripcion y añade la tarea a la lista"""
    descripcion = input("\nEscribe la descripcion de la nueva tarea:")
    nueva_tarea = {
        "descripcion" : descripcion,
        "completada" : False
    }
    tareas.append(nueva_tarea)
    print(f"¡Tarea '{descripcion}' añadida con éxito!")
    
def marcar_completada(tareas):
    """Muestra las tareas y pide al usuario que elija una para marcarla"""
    mostrar_tareas(tareas)
    if not tareas:
        return  #Si  no hay tareas no hacemos nada
    try:
        num_tarea = int(input("Ingresa el  numero de tarea para marcar como completada: "))
        #Restamos 1 porque las listas empiezan de 0 y mostramos desde 1
        indice = num_tarea - 1
            
        if 0 <= indice < len(tareas):
            tareas[indice]["completada"] = True
            print(f"\n!Tarea {num_tarea} marcada como completada¡")
        else:
            print("\nError: Número de tarea fuera de rango")
    except ValueError:
            print("\nError: Porfavor ingresa solo un número")
            
def eliminar_tarea(tareas):
    """Muestra las tareas y pide al usuario que elija una para eliminarla"""
    mostrar_tareas(tareas)
    if not tareas:
        return  #Si  no hay tareas no hacemos nada
    try:
        num_tarea = int(input("Ingresa el  numero de tarea para marcar como completada: "))
        #Restamos 1 porque las listas empiezan de 0 y mostramos desde 1
        indice = num_tarea - 1
            
        if 0 <= indice < len(tareas):
            #Usamos .pop() para eliminarla por completo
            tarea_eliminada = tareas.pop(indice)
            print(f"\n!Tarea '{tarea_eliminada['descripcion']}' eliminada¡")
        else:
            print("\nError: Número de tarea fuera de rango")
    except ValueError:
            print("\nError: Porfavor ingresa solo un número")
            
#FUNCION PRINCIPAL
def main():
    """Esta es la funcion principal que ejecuta el programa"""
    tareas = cargar_tareas()
    
    while True:
        #Mostramos menú de opciones
        print("\n---    Gestor de Tareas    ---")
        print("1. Ver todas las tareas")
        print("2. Añadir una tarea")
        print("3. Marcar una tarea como completada")
        print("4. Eliminar una tarea")
        print("5. Guardar y Salir")
        
        opcion = input("\nElige una opcion: ")
        
        if opcion == '1':
            mostrar_tareas(tareas)
        elif opcion == '2':
            anadir_tarea(tareas)
        elif opcion == '3':
            marcar_completada(tareas)
        elif opcion == '4':
            eliminar_tarea(tareas)
        elif opcion == '5':
            guardar_tareas(tareas)
            print("\n!Tareas guardadadas. Adios¡")
            break #Rompemos el bucle while para salir
        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 5.")
        
        # Pausa para que el usuario pueda ver el resultado antes de volver al menú
        time.sleep(2) 
    
#PUNTO DE ENTRADA DEL PROGRAMA
if __name__ == "__main__":
    main()

