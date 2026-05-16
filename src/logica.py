from database import get_connection

def agregar_perfume(nombre, nombre_marca, nombre_familia, precio, stock, nit_proveedor, nombre_proveedor, direccion_proveedor, nombre_ciudad):
    conexion = get_connection()
    if not conexion:
        print("No se pudo establecer conexión con la base de datos.")
        return False
    
    try:
        cursor = conexion.cursor()
        
        # 1. Marca
        cursor.execute("SELECT id_marca FROM marca WHERE nombre = %s", (nombre_marca,))
        resultado = cursor.fetchone()
        if resultado:
            id_marca = resultado[0]
        else:
            cursor.execute("INSERT INTO marca (nombre) VALUES (%s)", (nombre_marca,))
            id_marca = cursor.lastrowid
            
        # 2. Familia
        cursor.execute("SELECT codigo FROM familia WHERE nombre = %s", (nombre_familia,))
        resultado = cursor.fetchone()
        if resultado:
            codigo_familia = resultado[0]
        else:
            cursor.execute("INSERT INTO familia (nombre) VALUES (%s)", (nombre_familia,))
            codigo_familia = cursor.lastrowid
            
        # 3. Ciudad (para el proveedor)
        cursor.execute("SELECT id_ciudad FROM ciudad WHERE nombre = %s", (nombre_ciudad,))
        resultado = cursor.fetchone()
        if resultado:
            id_ciudad = resultado[0]
        else:
            cursor.execute("INSERT INTO ciudad (nombre) VALUES (%s)", (nombre_ciudad,))
            id_ciudad = cursor.lastrowid
            
        # 4. Proveedor
        cursor.execute("SELECT NIT FROM proveedor WHERE NIT = %s", (nit_proveedor,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO proveedor (NIT, nombre, direccion, id_ciudad) VALUES (%s, %s, %s, %s)", 
                           (nit_proveedor, nombre_proveedor, direccion_proveedor, id_ciudad))
            
        # 5. Perfume (código es AUTO_INCREMENT, no necesitamos proveerlo)
        cursor.execute("INSERT INTO perfume (nombre, stock, id_marca, codigo_familia) VALUES (%s, %s, %s, %s)",
                       (nombre, stock, id_marca, codigo_familia))
        codigo_perfume = cursor.lastrowid
        
        # 6. Relación proveedor_perfume
        cursor.execute("INSERT INTO proveedor_perfume (NIT, codigo_perfume, precio) VALUES (%s, %s, %s)",
                       (nit_proveedor, codigo_perfume, precio))
        
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al agregar perfume a la base de datos: {e}")
        conexion.rollback()
        return False
    finally:
        cursor.close()
        conexion.close()


def mostrar_inventario():
    conexion = get_connection()
    if not conexion:
        return None
    try:
        cursor = conexion.cursor(dictionary=True)
        query = """
            SELECT p.codigo as id, p.nombre, m.nombre as marca, f.nombre as familia,
                   pp.precio, p.stock, prov.nombre as proveedor
            FROM perfume p
            JOIN marca m ON p.id_marca = m.id_marca
            JOIN familia f ON p.codigo_familia = f.codigo
            JOIN proveedor_perfume pp ON p.codigo = pp.codigo_perfume
            JOIN proveedor prov ON pp.NIT = prov.NIT
        """
        cursor.execute(query)
        resultados = cursor.fetchall()
        
        if not resultados:
            print("El inventario está vacío.")
            return

        for perfume in resultados:
            print(
                f"ID: {perfume['id']}\n"
                f"NOMBRE: {perfume['nombre']}\n"
                f"MARCA: {perfume['marca']}\n"
                f"FAMILIA: {perfume['familia']}\n"
                f"PRECIO: {perfume['precio']}\n"
                f"STOCK: {perfume['stock']}\n"
                f"PROVEEDOR: {perfume['proveedor']}\n"
            )
            print("-" * 30)
    except Exception as e:
        print(f"Error al obtener el inventario: {e}")
    finally:
        cursor.close()
        conexion.close()


def buscar_id(id):
    conexion = get_connection()
    if not conexion:
        return None
    try:
        cursor = conexion.cursor(dictionary=True)
        query = """
            SELECT p.codigo as id, p.nombre, m.nombre as marca, f.nombre as familia,
                   pp.precio, p.stock, prov.nombre as proveedor
            FROM perfume p
            JOIN marca m ON p.id_marca = m.id_marca
            JOIN familia f ON p.codigo_familia = f.codigo
            JOIN proveedor_perfume pp ON p.codigo = pp.codigo_perfume
            JOIN proveedor prov ON pp.NIT = prov.NIT
            WHERE p.codigo = %s
        """
        cursor.execute(query, (id,))
        return cursor.fetchone()
    except Exception as e:
        print(f"Error al buscar el perfume: {e}")
        return None
    finally:
        cursor.close()
        conexion.close()


def eliminar_perfume(id):
    conexion = get_connection()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        
        # Verificar si existe
        cursor.execute("SELECT codigo FROM perfume WHERE codigo = %s", (id,))
        if not cursor.fetchone():
            return False
            
        cursor.execute("DELETE FROM proveedor_perfume WHERE codigo_perfume = %s", (id,))
        cursor.execute("DELETE FROM perfume WHERE codigo = %s", (id,))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar perfume: {e}")
        conexion.rollback()
        return False
    finally:
        cursor.close()
        conexion.close()


def actualizar_stock(id, nuevo_stock):
    conexion = get_connection()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        
        cursor.execute("SELECT codigo FROM perfume WHERE codigo = %s", (id,))
        if not cursor.fetchone():
            return False
            
        cursor.execute("UPDATE perfume SET stock = stock + %s WHERE codigo = %s", (nuevo_stock, id))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al actualizar stock: {e}")
        conexion.rollback()
        return False
    finally:
        cursor.close()
        conexion.close()