from logica import agregar_perfume
from logica import mostrar_inventario
from logica import buscar_id
from logica import eliminar_perfume
from logica import actualizar_stock

def menu(lista):
    while True:
        print("1. Agregar perfume")
        print("2. Mostrar inventario")
        print("3. Busacar por ID")
        print("4. Eliminar perfume")
        print("5. actualizar stock")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("Ingrese el ID del perfume: "))
            nombre = input("Ingrese el nombre del perfume: ")
            marca = input("Ingrese la marca del perfume: ")
            familia = input("Ingrese la familia del perfume: ")
            precio = float(input("Ingrese el precio del perfume: "))
            stock = int(input("Ingrese el stock del perfume: "))
            proveedor = input("Ingrese el proveedor del perfume: ")


            if agregar_perfume(lista, id, nombre, marca, familia, precio, stock, proveedor) == False:
                print("El ID ya existe en el inventario. No se pudo agregar el perfume.")
            else:
                print("Perfume agregado exitosamente.")


        elif opcion == "2":
            lista_inventario = mostrar_inventario(lista)
            
            if lista_inventario is not None:
                for perfume in lista_inventario:
                    print(f"ID: {perfume['id']}\n NOMBRE: {perfume['nombre']}\n MARCA: {perfume['marca']}\n FAMILIA: {perfume['familia']}\n PRECIO: {perfume['precio']}\n STOCK: {perfume['stock']}\n PROVEEDOR: {perfume['proveedor']}\n")
            else:
                print("El inventario está vacío.")

        elif opcion == "3":
            id_buscada = int(input("Ingrese la id del perfume que desea buscar: "))
            buscar = buscar_id(id_buscada, lista)

            if buscar is not None:
                print(f"ID: {buscar['id']}\n NOMBRE: {buscar['nombre']}\n MARCA: {buscar['marca']}\n FAMILIA: {buscar['familia']}\n PRECIO: {buscar['precio']}\n STOCK: {buscar['stock']}\n PROVEEDOR: {buscar['proveedor']}\n")
            else:
                print("No se encontró un perfume con esa ID.")

        elif opcion == "4":
            id_eliminar = int(input("Ingrese la id del perfume que desea eliminar: "))
            eliminar = eliminar_perfume(id_eliminar, lista)

            if eliminar == True:
                print("Perfume eliminado exitosamente.")
            else:
                print("No se encontró un perfume con esa ID. No se pudo eliminar.")

        elif opcion == "5":
            id_actualizar = int(input("Ingrese la id del perfume que desea actualizar el stock: "))
            nuevo_stock = int(input("Ingrese la cantidad de perfumes que ingresaron al iventario: "))
            actualizar = actualizar_stock(id_actualizar, nuevo_stock, lista)

            if actualizar == True:
                print("Stock actualizado exitosamente.")
            else:
                print("No se encontró un perfume con esa ID. No se pudo actualizar el stock.")
        
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
