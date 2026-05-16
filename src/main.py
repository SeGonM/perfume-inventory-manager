from menu import menu
from database import get_connection

if __name__ == "__main__":
    print("Iniciando Perfume Inventory Manager...")
    
    # Verificar conexión a la base de datos antes de arrancar
    conexion = get_connection()
    if conexion:
        print("Conectado exitosamente a la base de datos MySQL.")
        conexion.close()
        menu()
    else:
        print("Error crítico: No se pudo conectar a la base de datos.")
        print("Por favor, asegúrate de que:")
        print("  1. Tu servidor MySQL (XAMPP, WAMP, etc.) esté en ejecución.")
        print("  2. Hayas ejecutado el script 'data/scheme.sql' para crear la base de datos.")
        print("  3. Las credenciales en 'src/database.py' sean correctas.")