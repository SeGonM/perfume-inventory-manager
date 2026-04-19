from logica import agregar_perfume
from logica import mostrar_inventario
from logica import buscar_id
from logica import eliminar_perfume
from logica import actualizar_stock
from solicitudes import solicitar_entero
from solicitudes import solicitar_flotante
from solicitudes import solicitar_texto

def menu(inventario):
    while True:
        print("1. Agregar perfume")
        print("2. Mostrar inventario")
        print("3. Buscar por ID")
        print("4. Eliminar perfume")
        print("5. Actualizar stock")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_perfume = solicitar_entero("Ingrese el ID del perfume: ", min_val=0)
            nombre = solicitar_texto("Ingrese el nombre del perfume: ")
            marca = solicitar_texto("Ingrese la marca del perfume: ")
            familia = solicitar_texto("Ingrese la familia del perfume: ")
            precio = solicitar_flotante("Ingrese el precio del perfume: ", min_val=0.0)
            stock = solicitar_entero("Ingrese el stock del perfume: ", min_val=0)
            proveedor = solicitar_texto("Ingrese el proveedor del perfume: ")

            if agregar_perfume(inventario, id_perfume, nombre, marca, familia, precio, stock, proveedor) is False:
                print("El ID ya existe en el inventario. No se pudo agregar el perfume.")
            else:
                print("Perfume agregado exitosamente.")

        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            id_buscada = solicitar_entero("Ingrese la ID del perfume que desea buscar: ", min_val=0)
            buscar = buscar_id(id_buscada, inventario)
            if buscar is not None:
                print(
                    f"ID: {buscar['id']}\n"
                    f"NOMBRE: {buscar['nombre']}\n"
                    f"MARCA: {buscar['marca']}\n"
                    f"FAMILIA: {buscar['familia']}\n"
                    f"PRECIO: {buscar['precio']}\n"
                    f"STOCK: {buscar['stock']}\n"
                    f"PROVEEDOR: {buscar['proveedor']}\n"
                )
            else:
                print("No se encontró un perfume con esa ID.")

        elif opcion == "4":
            id_eliminar = solicitar_entero("Ingrese la ID del perfume que desea eliminar: ", min_val=0)
            eliminar = eliminar_perfume(id_eliminar, inventario)
            if eliminar:
                print("Perfume eliminado exitosamente.")
            else:
                print("No se encontró un perfume con esa ID. No se pudo eliminar.")

        elif opcion == "5":
            id_actualizar = solicitar_entero("Ingrese la ID del perfume que desea actualizar el stock: ", min_val=0)
            nuevo_stock = solicitar_entero("Ingrese la cantidad de perfumes que ingresaron al inventario: ", min_val=0)
            actualizar = actualizar_stock(id_actualizar, nuevo_stock, inventario)
            if actualizar:
                print("Stock actualizado exitosamente.")
            else:
                print("No se encontró un perfume con esa ID. No se pudo actualizar el stock.")

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
