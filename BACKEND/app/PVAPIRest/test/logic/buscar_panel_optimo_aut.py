### Aun no funcionable

import unittest
import math
import sys
import os
from unittest.mock import patch, MagicMock
# Agregar ruta raíz del proyecto para importar correctamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from logic.buscar_sistema_optimo import buscar_panel_optimo

class PruebasSimuladasBuscarPanelOptimo(unittest.TestCase):

    @patch('logic.buscar_sistema_optimo.Paneles')
    def test_panel_optimo_satisfactorio(self, MockPaneles):
        print("\n---- [PRUEBA] Panel óptimo con parámetros válidos ----")
        mock_panel = MagicMock()
        mock_panel.id = 101
        mock_panel.modelo = "S-FV350"
        mock_panel.potencia = 350
        mock_panel.ancho = 1000
        mock_panel.alto = 1600
        mock_panel.eficiencia = 18
        mock_panel.precio = 200

        MockPaneles.objects.all.return_value = [mock_panel]

        consumo_hogar = 10  # kWh/día
        area_disponible = 20  # m²

        resultado = buscar_panel_optimo(consumo_hogar, area_disponible)

        print("Resultado:", resultado)

        self.assertIsNotNone(resultado)
        self.assertIn("panel", resultado)
        self.assertGreater(resultado["cantidad"], 0)
        self.assertGreater(resultado["costo_total_usd"], 0)

    @patch('logic.buscar_sistema_optimo.Paneles')
    def test_panel_optimo_area_insuficiente(self, MockPaneles):
        print("\n---- [PRUEBA] Área insuficiente para instalación ----")
        mock_panel = MagicMock()
        mock_panel.id = 102
        mock_panel.modelo = "S-FV400"
        mock_panel.potencia = 400
        mock_panel.ancho = 1200
        mock_panel.alto = 2000
        mock_panel.eficiencia = 20
        mock_panel.precio = 220

        MockPaneles.objects.all.return_value = [mock_panel]

        consumo_hogar = 30  # kWh/día
        area_disponible = 1  # m² (muy poco)

        resultado = buscar_panel_optimo(consumo_hogar, area_disponible)

        print("Resultado esperado: None")
        print("Resultado real:", resultado)

        self.assertIsNone(resultado)

    @patch('logic.buscar_sistema_optimo.Paneles')
    def test_panel_optimo_datos_invalidos(self, MockPaneles):
        print("\n---- [PRUEBA] Datos del panel inválidos ----")
        mock_panel = MagicMock()
        mock_panel.id = 103
        mock_panel.modelo = "INV-XXX"
        mock_panel.potencia = 300
        mock_panel.ancho = 0  # ancho inválido
        mock_panel.alto = 1600
        mock_panel.eficiencia = -5  # eficiencia inválida
        mock_panel.precio = 0  # precio inválido

        MockPaneles.objects.all.return_value = [mock_panel]

        resultado = buscar_panel_optimo(10, 10)

        print("Resultado esperado: None")
        print("Resultado real:", resultado)

        self.assertIsNone(resultado)


if __name__ == '__main__':
    unittest.main()
