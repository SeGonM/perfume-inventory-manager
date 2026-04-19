import unittest
import sys
sys.path.insert(0, '.')  # Agrega la raíz del proyecto al path para imports
from Codigo.logica import agregar_perfume, mostrar_inventario, buscar_id, eliminar_perfume, actualizar_stock

class TestLogica(unittest.TestCase):
    def setUp(self):
        """Configura un inventario de prueba antes de cada test."""
        self.inventario = {
            1: {
                "id": 1,
                "nombre": "Sauvage",
                "marca": "Dior",
                "familia": "Fougère",
                "precio": 450000.0,
                "stock": 10,
                "proveedor": "Importadora Fragancias"
            }
        }

    def test_agregar_perfume_exitoso(self):
        """Prueba agregar un perfume nuevo."""
        resultado = agregar_perfume(self.inventario, 2, "Bleu", "Chanel", "Amaderada", 520000.0, 5, "Lujo Global")
        self.assertTrue(resultado)
        self.assertIn(2, self.inventario)
        self.assertEqual(self.inventario[2]["nombre"], "Bleu")

    def test_agregar_perfume_id_duplicado(self):
        """Prueba agregar un perfume con ID existente."""
        resultado = agregar_perfume(self.inventario, 1, "Duplicado", "Marca", "Familia", 100000.0, 1, "Proveedor")
        self.assertFalse(resultado)
        self.assertEqual(len(self.inventario), 1)  # No se agregó

    def test_buscar_id_existente(self):
        """Prueba buscar un ID que existe."""
        perfume = buscar_id(1, self.inventario)
        self.assertIsNotNone(perfume)
        self.assertEqual(perfume["nombre"], "Sauvage")

    def test_buscar_id_inexistente(self):
        """Prueba buscar un ID que no existe."""
        perfume = buscar_id(999, self.inventario)
        self.assertIsNone(perfume)

    def test_buscar_id_inventario_none(self):
        """Prueba buscar en inventario None."""
        perfume = buscar_id(1, None)
        self.assertIsNone(perfume)

    def test_eliminar_perfume_existente(self):
        """Prueba eliminar un perfume existente."""
        resultado = eliminar_perfume(1, self.inventario)
        self.assertTrue(resultado)
        self.assertNotIn(1, self.inventario)

    def test_eliminar_perfume_inexistente(self):
        """Prueba eliminar un perfume que no existe."""
        resultado = eliminar_perfume(999, self.inventario)
        self.assertFalse(resultado)
        self.assertIn(1, self.inventario)  # Sigue ahí

    def test_eliminar_perfume_inventario_none(self):
        """Prueba eliminar en inventario None."""
        resultado = eliminar_perfume(1, None)
        self.assertIsNone(resultado)

    def test_actualizar_stock_existente(self):
        """Prueba actualizar stock de un perfume existente."""
        resultado = actualizar_stock(1, 5, self.inventario)
        self.assertTrue(resultado)
        self.assertEqual(self.inventario[1]["stock"], 15)  # 10 + 5

    def test_actualizar_stock_inexistente(self):
        """Prueba actualizar stock de un perfume que no existe."""
        resultado = actualizar_stock(999, 5, self.inventario)
        self.assertFalse(resultado)

    def test_actualizar_stock_inventario_none(self):
        """Prueba actualizar stock en inventario None."""
        resultado = actualizar_stock(1, 5, None)
        self.assertIsNone(resultado)

    # Nota: mostrar_inventario imprime, así que no se prueba directamente (sería un test de integración).
    # Para probarlo, podrías capturar stdout, pero por simplicidad, lo omitimos aquí.

if __name__ == '__main__':
    unittest.main()