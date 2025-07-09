import unittest
from logic.calcular_roi import (
    calcularROI,
    calcularPayback,
    calcularResumenROIyPayback
)

class TestCalculoROIyPayback(unittest.TestCase):
    # Test para calcularROI
    # Test 1
    def test_roi_generacion_igual_consumo(self):
        resultado = calcularROI(10000, 30, 30, 0.25)
        self.assertEqual(resultado["ahorro_diario_soles"], 7.5)
        self.assertIn("igual al consumo diario", resultado["notas"][0])
    
    # Test 2
    def test_roi_generacion_menor_que_consumo(self):
        resultado = calcularROI(8000, 20, 30, 0.3)
        self.assertEqual(resultado["ahorro_diario_soles"], 6.0)
        self.assertIn("menor que el consumo diario", resultado["notas"][0])
    
    # Test 3
    def test_roi_generacion_mayor_que_consumo(self):
        resultado = calcularROI(15000, 50, 30, 0.2)
        self.assertEqual(resultado["ahorro_diario_soles"], 6.0)
        self.assertIn("excede el consumo diario", resultado["notas"][0])

    # Test 4
    def test_roi_valores_invalidos(self):
        with self.assertRaises(ValueError):
            print("Test 4", calcularROI(0, 20, 30, 0.25))
        with self.assertRaises(ValueError):
            calcularROI(10000, -5, 30, 0.25)

    # Test para calcularPayback
    # Test 5
    def test_payback_valores_correctos(self):
        resultado = calcularPayback(10000, 0.25, 30)
        esperado_anios = 10000 / (0.25 * 30 * 365)
        self.assertAlmostEqual(resultado["tiempo_recuperacion_anios"], round(esperado_anios, 2))

    # Test 6
    def test_payback_valores_invalidos(self):
        with self.assertRaises(ValueError):
            calcularPayback(-10000, 0.25, 30)
        with self.assertRaises(ValueError):
            calcularPayback(10000, 0, 30)

    # Test para calcularResumenROIyPayback
    # Test 7
    def test_resumen_completo(self):
        resultado = calcularResumenROIyPayback(
            costo_total_sistema=12000,
            consumo_diario_kwh=25,
            energia_generada_diaria_kwh=30,
            costo_kwh_red=0.22
        )
        self.assertIn("datos_entrada", resultado)
        self.assertIn("analisis", resultado)
        self.assertIn("retorno_inversion", resultado["analisis"])
        self.assertIn("tiempo_recuperacion", resultado["analisis"])
        self.assertGreater(len(resultado["notas"]), 1)

if __name__ == "__main__":
    unittest.main()
