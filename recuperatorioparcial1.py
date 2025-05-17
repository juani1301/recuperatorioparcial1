def mostrar_menu():
    print("\n Menú de opciones:")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Actualizar stock")
    print("4. Ver todos los productos")
    print("5. Salir")

def agregar_producto(nombres, cantidades):
    nuevo_producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    nombres.append(nuevo_producto)
    cantidades.append(cantidad)

def ver_productos_agotados(nombres, cantidades):
    print("\nProductos agotados:")
    hay_agotados = False
    for i in range(len(cantidades)):
        if cantidades[i] == 0:
            print(f"- {nombres[i]}")
            hay_agotados = True
    if not hay_agotados:
        print("No hay productos agotados.")

def actualizar_stock(nombres, cantidades):
    producto = input("Ingrese el nombre del producto a actualizar: ")
    if producto in nombres:
        indice = nombres.index(producto)
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        cantidades[indice] = nueva_cantidad
        print(f"Stock actualizado para {producto}: {nueva_cantidad}")
    else:
        print("El producto no se encuentra en la lista.")

def ver_todos_los_productos(nombres, cantidades):
    print("\nListado de productos:")
    for i in range(len(nombres)):
        print(f"{nombres[i]}: {cantidades[i]} unidades")

def main():
    nombres = []
    cantidades = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            agregar_producto(nombres, cantidades)
        elif opcion == '2':
            ver_productos_agotados(nombres, cantidades)
        elif opcion == '3':
            actualizar_stock(nombres, cantidades)
        elif opcion == '4':
            ver_todos_los_productos(nombres, cantidades)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()


### Descripción del programa:
#1. **Funciones**:

#2.Principal**: El programa se ejecuta en un bucle `while` que permite seguir utilizando el menú hasta que el usuario decida salir.

#3. **Listas paralelas**: Usa dos listas, `nombres` y `cantidades`, para almacenar los productos y sus respectivas cantidades.

