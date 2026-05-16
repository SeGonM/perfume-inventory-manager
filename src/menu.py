from logica import agregar_perfume
from logica import mostrar_inventario
from logica import buscar_id
from logica import eliminar_perfume
from logica import actualizar_stock
from solicitudes import solicitar_entero
from solicitudes import solicitar_flotante
from solicitudes import solicitar_texto

def menu():
    while True:
        print("\n--- MENU DE INVENTARIO ---")
        print("1. Agregar perfume")
        print("2. Mostrar inventario")
        print("3. Buscar por ID")
        print("4. Eliminar perfume")
        print("5. Actualizar stock")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            print("\n-- Datos del Perfume --")
            nombre = solicitar_texto("Ingrese el nombre del perfume: ")
            marca = solicitar_texto("Ingrese la marca del perfume: ")
            familia = solicitar_texto("Ingrese la familia del perfume: ")
            precio = solicitar_flotante("Ingrese el precio del perfume: ", min_val=0.0)
            stock = solicitar_entero("Ingrese el stock del perfume: ", min_val=0)
            
            print("\n-- Datos del Proveedor --")
            nit_proveedor = solicitar_entero("Ingrese el NIT del proveedor: ", min_val=1)
            nombre_proveedor = solicitar_texto("Ingrese el nombre del proveedor: ")
            direccion_proveedor = solicitar_texto("Ingrese la dirección del proveedor: ")
            nombre_ciudad = solicitar_texto("Ingrese la ciudad del proveedor: ")

            if agregar_perfume(nombre, marca, familia, precio, stock, nit_proveedor, nombre_proveedor, direccion_proveedor, nombre_ciudad) is False:
                print("Hubo un error al agregar el perfume. Verifique la conexión a la base de datos o si los datos son correctos.")
            else:
                print("Perfume agregado exitosamente.")

        elif opcion == "2":
            print("\n--- INVENTARIO ACTUAL ---")
            mostrar_inventario()

        elif opcion == "3":
            id_buscada = solicitar_entero("Ingrese la ID del perfume que desea buscar: ", min_val=0)
            buscar = buscar_id(id_buscada)
            if buscar is not None:
                print("\n-- Perfume Encontrado --")
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
            eliminar = eliminar_perfume(id_eliminar)
            if eliminar:
                print("Perfume eliminado exitosamente.")
            else:
                print("No se encontró un perfume con esa ID. No se pudo eliminar.")

        elif opcion == "5":
            id_actualizar = solicitar_entero("Ingrese la ID del perfume que desea actualizar el stock: ", min_val=0)
            nuevo_stock = solicitar_entero("Ingrese la cantidad de perfumes que ingresaron al inventario: ", min_val=0)
            actualizar = actualizar_stock(id_actualizar, nuevo_stock)
            if actualizar:
                print("Stock actualizado exitosamente.")
            else:
                print("No se encontró un perfume con esa ID. No se pudo actualizar el stock.")

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
