import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

import unittest
from PVAPIRest.logic.calcular_energia_panel import calcularEnergiaPanelesPorDia


class TestCalculoEnergiaPanel(unittest.TestCase):

    def test_calculo_valores_normales(self):
        area = 1.6  # m²
        irradiancia = 4.9  # kWh/m²/día
        eficiencia = 0.15  # 15%
        perdidas = 0.8  # 80% rendimiento
        energia = calcularEnergiaPanelesPorDia(area, irradiancia, eficiencia, perdidas)
        esperado = area * irradiancia * eficiencia * perdidas # Funcion de calculo E = A * r * H * PR
        self.assertAlmostEqual(energia, esperado, places=4)

    def test_calculo_valores_altos(self):
        energia = calcularEnergiaPanelesPorDia(1000.0, 12.0, 0.30, 0.9)
        esperado = 1000.0 * 12.0 * 0.30 * 0.9
        self.assertAlmostEqual(energia, esperado, places=4)

    def test_valores_cero_espera_error(self):
        with self.assertRaises(ValueError):
            calcularEnergiaPanelesPorDia(0, 4.5, 0.18, 0.8)

    def test_valor_eficiencia_negativa(self):
        with self.assertRaises(ValueError):
            calcularEnergiaPanelesPorDia(1.6, 4.9, -0.1, 0.8)

    def test_factor_perdidas_cero(self):
        with self.assertRaises(ValueError):
            calcularEnergiaPanelesPorDia(1.6, 4.9, 0.18, 0.0)

    def test_calculo_redondeo_precision(self):
        energia = calcularEnergiaPanelesPorDia(2.0, 5.0, 0.20, 0.75)
        self.assertAlmostEqual(energia, 1.5, places=2)  # 2*5*0.20*0.75 = 1.5

if __name__ == '__main__':
    unittest.main()
