def agregar_perfume(lista, id, nombre, marca, familia, precio, stock, proveedor):
    existe = False
    for perfume in lista:
        if id == perfume[0]:
            existe = True
            return False



    if existe == False:
        perfume = [id, nombre, marca, familia, precio, stock, proveedor]
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
            if perfume[0] == id:
                return perfume
        else:
            return None

def eliminar_perfume(id, lista):
    if lista is None:
        return None
    else:
        for perfume in lista:
            if perfume[0] == id:
                lista.remove(perfume)
                return True
        else:
            return False
        

def actualizar_stock(id, nuevo_stock, lista):
    if lista is None:
        return None
    else:
        for perfume in lista:
            if perfume[0] == id:
                perfume[5] += nuevo_stock
                return True
        else:
            return False