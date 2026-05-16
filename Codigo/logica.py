def agregar_perfume(inventario, id, nombre, marca, familia, precio, stock, proveedor):
    if id in inventario:
        return False
    inventario[id] ={"id": id,
                      "nombre": nombre,
                      "marca": marca,
                      "familia": familia, 
                      "precio": precio, 
                      "stock": stock, 
                      "proveedor": proveedor
                    }
    return True

def mostrar_inventario(inventario):
    if inventario is None:
        return None
    
    for perfume in inventario.values():
        print(
            f"ID: {perfume['id']}\n"
            f"NOMBRE: {perfume['nombre']}\n"
            f"MARCA: {perfume['marca']}\n"
            f"FAMILIA: {perfume['familia']}\n"
            f"PRECIO: {perfume['precio']}\n"
            f"STOCK: {perfume['stock']}\n"
            f"PROVEEDOR: {perfume['proveedor']}\n"
        )


def buscar_id(id, inventario):
    if inventario is None:
        return None
    return inventario.get(id, None)


def eliminar_perfume(id, inventario):
    if inventario is None:
        return None
    if id in inventario:
        del inventario[id]
        return True
    return False

def actualizar_stock(id, nuevo_stock, inventario):
    if inventario is None:
        return None
    if id in inventario:
        inventario[id]['stock'] += nuevo_stock
        return True
    return False