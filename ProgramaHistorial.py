
# Creamos una lista vacia de tareas pendientes
tareasPendientes = []

# programa principal
while True:
    print('\n******************************')
    print('\nHISTORIAL DE TAREAS PENDIENTES')
    print('\n1. Agregar una tarea al inicio de la lista'  
          '\n2. Eliminar la última tarea de la lista'
          '\n3. Mostrar las tareas de lista de manera inversa'
          '\n4. Salir')
    
    opcion = input("Ingresa la opcion deseada: ")
    
    if opcion == '1':
        tarea = input('Tarea que desea agregar: ')
        tareasPendientes.insert(0, tarea)
        print("\nLa tarea se agrego.")
    elif opcion == "2":
        if len(tareasPendientes) == 0:
            print("\nNo hay tareas pendientes para eliminar.")
        else:
            tareaEliminada = tareasPendientes.pop()
            print(f'\nLa tarea {tareaEliminada} ha sido eliminada del historial')
    elif opcion == "3":
        if len(tareasPendientes) == 0:
            print('\nNo hay tareas para mostrar')
        else:
            print('\nLista de tareas de manera invertida')
            for i in reversed(tareasPendientes):
                print(i)
    elif opcion == "4":
        break
    else:
        print('\Dato inválida')
        
    print(f"Tareas pendientes: {len(tareasPendientes)}")
