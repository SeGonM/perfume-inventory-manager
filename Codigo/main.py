from menu import menu

if __name__ == "__main__":
    ##Nueva estructura de datos más eficiente: diccionario con ID como clave
    inventario = {
        1: {
            "id": 1,
            "nombre": "Sauvage",
            "marca": "Dior",
            "familia": "Fougère",
            "precio": 450000.0,
            "stock": 10,
            "proveedor": "Importadora Fragancias"
        },
        2: {
            "id": 2,
            "nombre": "Bleu de Chanel",
            "marca": "Chanel",
            "familia": "Amaderada",
            "precio": 520000.0,
            "stock": 5,
            "proveedor": "Lujo Global"
        }
    }

    menu(inventario)