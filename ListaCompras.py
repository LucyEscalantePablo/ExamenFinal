listaProductos = []

# funcion para agregar un producto a la lista
def agregarProducto():
    producto = input('Ingrese el nombre del produccto: ')
    listaProductos.append(producto)

# Eliminamos productos del inicio
def EliminarProducto():
    if len(listaProductos)>0:
        productoEliminado = listaProductos.pop(0)
    else:
        print('La lista está vacia')

# Mostramos la lista

def MostramosLista():
    print('Lista actual es: ')
    print(listaProductos)

# programa principal
while True:
    print('**************************************')
    print('Que desea hacer con la lista de compra')
    print('\n1. Aregar producto'
          '\n2. Eliminar el producto'
          '\n3. Mostrar la lista'
          '\n4. salir')
    opcion = int(input('Ingrese la opcion: '))

    if opcion == 1:
        agregarProducto()
    elif opcion == 2:
        EliminarProducto()
    elif opcion == 3:
        MostramosLista()
    elif opcion == 4:
        break
    else:
        print('Dato invalida')
