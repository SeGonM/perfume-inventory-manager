from menu import menu

if __name__ == "__main__":
    #[ID, NOMBRE, MARCA, FAMILIA, PRECIO, STOCK, PROVEEDOR]
    inventario = [
        [101, "Sauvage", "Dior", "Fougère", 125000.0, 15, "Distribuidora Internacional"],
        [102, "Light Blue", "Dolce & Gabbana", "Cítrica", 95000.0, 8, "Fragancias del Sur"],
        [103, "Club de Nuit", "Armaf", "Amaderada", 45000.0, 20, "Importaciones Directas"]
    ]

    menu(inventario)