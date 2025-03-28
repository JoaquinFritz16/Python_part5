tareas=[]

def agregar_tarea():
    tarea= input("Ingresar la tarea: ")
    descripcion= input("Ingresar una descripcion: ")
    fecha_vencimiento=input("Ingresar una fecha de vencimiento(DD-MM-YYYY): ")
    estado=input("Ingresar el estado (pendiente/en proceso/completada): ")
    importancia=input("Ingresar la importancia (alta/media/baja): ")

    new_task={
        "tarea": tarea,
        "descripcion": descripcion,
        "fecha_vencimiento": fecha_vencimiento,
        "estado": estado,
        "importancia": importancia
    }
    tareas.append(new_task)
    print("Tarea agregada con exito")
def mostrar_tareas():
    if not tareas:
        print("No hay tareas")
    else:
        print("\nLista de tareas")
        for i, t in enumerate(tareas, 1):
            print(f"Tarea {i}: {t['tarea']} - Descripcion: {t['descripcion']} - Vence: {t['fecha_vencimiento']} - Estado: {t['estado']} - Importancia: {t['importancia']}")
        print()
def completar_tarea():
    mostrar_tareas()
    if not tareas:
        print("No hay tareas")
    else:
        tarea_completar=int(input("Ingrese el numero de la tarea a completar: "))
        if tarea_completar>len(tareas):
            print("☣ Tarea no encontrada")
        else:
            tareas[tarea_completar-1]["estado"]="completada"
            print("✔ Tarea completada con exito")
def eliminar_tarea():
    mostrar_tareas()
    if not tareas:
        print("No hay tareas")
    else:
        tarea_eliminar=int(input("Ingrese el numero de la tarea a eliminar: "))
        if tarea_eliminar>len(tareas):
            print("☣ Tarea no encontrada")
        else:
            del tareas[tarea_eliminar-1]
            print("✔ Tarea eliminada con exito")
if __name__=="__main__":
    while True:
        print("1. Agregar tareas")
        print("2. Mostrar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Seleccione alguna opcion: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion =="5":
            print("🛫Hasta luego")
            break
        else:
            print("Opcion invalida, por favor seleccione una opcion valida")
