import unittest
from unittest.mock import MagicMock
from restaurante import Restaurante, Pedido
from menu import Plato

class TestRestaurante(unittest.TestCase):
    def setUp(self):
        self.mock_menu = MagicMock()
        self.restaurante = Restaurante(self.mock_menu)

    def test_crear_pedido_agrega_a_lista(self):
        pedido = self.restaurante.crear_pedido()
        self.assertIn(pedido, self.restaurante.pedidos)

    def test_agregar_plato_existente_a_pedido(self):
        plato_mock = Plato("Pizza", 25.0)
        self.mock_menu.obtener_plato.return_value = plato_mock
        pedido = Pedido()

        resultado = self.restaurante.agregar_plato_a_pedido(pedido, "Pizza")
        
        self.assertTrue(resultado)
        self.assertIn(plato_mock, pedido.platos)

    def test_agregar_plato_inexistente_a_pedido(self):
        self.mock_menu.obtener_plato.return_value = None
        pedido = Pedido()

        resultado = self.restaurante.agregar_plato_a_pedido(pedido, "Ceviche")
        
        self.assertFalse(resultado)
        self.assertEqual(len(pedido.platos), 0)

if __name__ == "__main__":
    unittest.main()
