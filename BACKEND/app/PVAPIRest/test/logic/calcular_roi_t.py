import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

import unittest
from PVAPIRest.logic.calcular_roi import calcularROI, calcularSolarPayback


class TestCalculoROIandPayback(unittest.TestCase):

    # === Pruebas para calcularROI ===
    def test_roi_caso_normal(self):
        costo = 10000
        generado = 40
        consumo = 30
        tarifa = 0.25
        roi_dias, roi_anios, ahorro_diario = calcularROI(costo, generado, consumo, tarifa)

        esperado_ahorro = consumo * tarifa
        esperado_roi_dias = costo / esperado_ahorro
        esperado_roi_anios = esperado_roi_dias / 365

        self.assertAlmostEqual(ahorro_diario, esperado_ahorro, places=2)
        self.assertAlmostEqual(roi_dias, esperado_roi_dias, places=2)
        self.assertAlmostEqual(roi_anios, esperado_roi_anios, places=4)

    def test_roi_generacion_menor_que_consumo(self):
        costo = 8000
        generado = 10
        consumo = 30
        tarifa = 0.20
        roi_dias, roi_anios, ahorro_diario = calcularROI(costo, generado, consumo, tarifa)

        esperado_ahorro = generado * tarifa
        self.assertAlmostEqual(ahorro_diario, esperado_ahorro, places=2)
        self.assertGreater(roi_dias, 0)
        self.assertGreater(roi_anios, 0)

    def test_roi_valores_invalidos(self):
        with self.assertRaises(ValueError):
            calcularROI(0, 10, 30, 0.25)
        with self.assertRaises(ValueError):
            calcularROI(10000, -5, 30, 0.25)
        with self.assertRaises(ValueError):
            calcularROI(10000, 10, 0, 0.25)
        with self.assertRaises(ValueError):
            calcularROI(10000, 10, 30, 0)

    # === Pruebas para calcularSolarPayback ===
    def test_payback_normal(self):
        costo = 12000
        tarifa = 0.30
        consumo_diario = 25
        dias, anios = calcularSolarPayback(costo, tarifa, consumo_diario)

        consumo_anual = consumo_diario * 365
        esperado_anios = costo / tarifa / consumo_anual
        esperado_dias = esperado_anios * 365

        self.assertAlmostEqual(dias, esperado_dias, places=2)
        self.assertAlmostEqual(anios, esperado_anios, places=4)

    def test_payback_valores_invalidos(self):
        with self.assertRaises(ValueError):
            calcularSolarPayback(0, 0.25, 20)
        with self.assertRaises(ValueError):
            calcularSolarPayback(10000, 0, 20)
        with self.assertRaises(ValueError):
            calcularSolarPayback(10000, 0.25, 0)

    def test_payback_consumo_alto(self):
        costo = 10000
        tarifa = 0.25
        consumo_diario = 100  # Consumo alto, recuperación más rápida
        dias, anios = calcularSolarPayback(costo, tarifa, consumo_diario)

        self.assertLess(anios, 5)
        self.assertLess(dias, 2000)


if __name__ == '__main__':
    unittest.main()