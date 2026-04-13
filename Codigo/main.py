from menu import menu

if __name__ == "__main__":
    ##Nueva estructura de datos
    inventario = [
        {
            "id": 1,
            "nombre": "Sauvage",
            "marca": "Dior",
            "familia": "Fougère",
            "precio": 450000.0,
            "stock": 10,
            "proveedor": "Importadora Fragancias"
        },
        {
            "id": 2,
            "nombre": "Bleu de Chanel",
            "marca": "Chanel",
            "familia": "Amaderada",
            "precio": 520000.0,
            "stock": 5,
            "proveedor": "Lujo Global"
        }
    ]

    menu(inventario)