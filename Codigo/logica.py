def agregar_perfume(lista, id, nombre, marca, familia, precio, stock, proveedor):
    existe = False
    for perfume in lista:
        if id == perfume["id"]:
            existe = True
            return False

    if existe == False:
        perfume = {"id":id,
                    "nombre":nombre,
                    "marca":marca,
                    "familia":familia, 
                    "precio":precio, 
                    "stock":stock, 
                    "proveedor": proveedor
                    }
        lista.append(perfume)
        return True

def mostrar_inventario(lista):
    if lista is None:
        return None
    else:
        return lista
            


def buscar_id(id, lista):
    encontrado = False
    if lista is None:
        return None
    else:
        for perfume in lista:
            if perfume['id'] == id:
                return perfume
        else:
            return None

def eliminar_perfume(id, lista):
    if lista is None:
        return None
    else:
        for i in range(len(lista)):
            if lista[i]['id'] == id:
                lista.pop(i)
                return True
        return False
        

def actualizar_stock(id, nuevo_stock, lista):
    if lista is None:
        return None
    else:
        for perfume in lista:
            if perfume['id'] == id:
                perfume['stock'] += nuevo_stock
                return True
        else:
            return False