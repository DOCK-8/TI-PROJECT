import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))


import unittest
from PVAPIRest.logic.buscar_sistema_optimo import (
    buscar_panel_optimo, 
    buscar_bateria_optima, 
    buscar_inversor_optimo
)
"""
# Suponemos que la función de cálculo ya ha sido importada correctamente
def fake_calcularEnergiaPanelesPorDia(area, irradiancia, eficiencia, perdidas):
    return area * irradiancia * eficiencia * (1 - perdidas)

# Parcheamos la función usada en buscar_panel_optimo (mock)
import sistema_optimizacion
sistema_optimizacion.calcularEnergiaPanelesPorDia = fake_calcularEnergiaPanelesPorDia
"""

class TestSistemaOptimizacion(unittest.TestCase):

    def test_buscar_panel_optimo_valido(self):
        consumo = 10  # kWh/día
        area = 20     # m²
        resultado = buscar_panel_optimo(consumo, area)
        panel, cantidad, costo = resultado

        self.assertIsNotNone(panel)
        self.assertGreaterEqual(cantidad, 1)
        self.assertGreater(costo, 0)
        self.assertLessEqual(cantidad * panel[2], area)  # Área total no debe exceder

    def test_buscar_panel_optimo_sin_area(self):
        consumo = 10
        area = 1  # Demasiado poco para cualquier panel
        resultado = buscar_panel_optimo(consumo, area)
        self.assertIsNone(resultado[0])  # No debe encontrar panel
        self.assertEqual(resultado[1], 0)
        self.assertIsNone(resultado[2])

    def test_buscar_bateria_optima(self):
        capacidad = 10000  # Wh
        resultado = buscar_bateria_optima(capacidad)
        self.assertIsNotNone(resultado)
        id_bat, cantidad, costo = resultado
        self.assertGreaterEqual(cantidad, 1)
        self.assertGreater(costo, 0)

    def test_buscar_inversor_optimo(self):
        potencia = 5000  # W
        resultado = buscar_inversor_optimo(potencia)
        inversor, cantidad, costo = resultado
        self.assertIsNotNone(inversor)
        self.assertGreaterEqual(cantidad, 1)
        self.assertGreater(costo, 0)
        self.assertGreaterEqual(inversor[1] * cantidad, potencia)

    def test_buscar_inversor_demasiada_potencia(self):
        potencia = 99999  # Mucho más que cualquier combinación
        resultado = buscar_inversor_optimo(potencia)
        self.assertIsNotNone(resultado[0])  # Debería encontrar algo
        self.assertGreaterEqual(resultado[0][1] * resultado[1], potencia)


if __name__ == '__main__':
    unittest.main()