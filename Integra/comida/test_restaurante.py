import unittest
from unittest.mock import MagicMock
from restaurante import Restaurante, Pedido
from menu import Plato

class TestAgregarPlatoAPedido(unittest.TestCase):
    
    def setUp(self):
        self.menu_mock = MagicMock()
        self.restaurante = Restaurante(self.menu_mock)

    def test_agregar_plato_existente(self):
        """Debe retornar True y agregar el plato al pedido si el plato existe en el menú."""

        plato = Plato("Hamburguesa", 18.5)
        self.menu_mock.obtener_plato.return_value = plato #Simula que el playo existe

        pedido = Pedido()
        resultado = self.restaurante.agregar_plato_a_pedido(pedido, "Hamburguesa")

        self.assertTrue(resultado)
        self.assertIn(plato, pedido.platos)
if __name__ == "__main__":
    unittest.main()