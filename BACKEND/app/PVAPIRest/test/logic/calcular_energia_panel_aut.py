import unittest
from logic.calcular_energia_panel import calcularEnergiaPanelesPorDia


class TestCalcularEnergiaPanel(unittest.TestCase):
    
    
    # 1
    def test_valores_normales(self):
        area = 1.6
        irradiancia = 4.9
        eficiencia = 0.15
        perdidas = 0.8
        #print("\nTest 1: Valores normales")
        #print(f"Datos de entrada:\nÁrea: {area} m², Irradiancia: {irradiancia} kWh/m²/día, Eficiencia: {eficiencia}, Pérdidas: {perdidas}")
        resultado = calcularEnergiaPanelesPorDia(area, irradiancia, eficiencia, perdidas)
        esperado = area * irradiancia * eficiencia * perdidas
        self.assertAlmostEqual(resultado, esperado, places=4)
    # 2
    def test_valores_altos(self):
        #print("\nTest 2: Valores altos")
        #print("Datos de entrada:\nÁrea: 10.0 m², Irradiancia: 7.0 kWh/m²/día, Eficiencia: 0.22, Pérdidas: 0.9")
        resultado = calcularEnergiaPanelesPorDia(10.0, 7.0, 0.22, 0.9)
        esperado = 10.0 * 7.0 * 0.22 * 0.9
        self.assertAlmostEqual(resultado, esperado, places=4)
    # 3
    def test_area_cero(self):
        #print("\nTest 3: Área cero")
        #print("Datos de entrada:\nÁrea: 0 m², Irradiancia: 4.9 kWh/m²/día, Eficiencia: 0.18, Pérdidas: 0.8")
        with self.assertRaises(ValueError):
            calcularEnergiaPanelesPorDia(0, 4.9, 0.18, 0.8)
    # 4
    def test_factor_perdidas_cero(self):
        #print("\nTest 4: Factor de pérdidas cero")
        #print("Datos de entrada:\nÁrea: 1.6 m², Irradiancia: 4.9 kWh/m²/día, Eficiencia: 0.18, Pérdidas: 0")
        with self.assertRaises(ValueError):
            calcularEnergiaPanelesPorDia(1.6, 4.9, 0.18, 0)
    # 5
    def test_irradiancia_negativa(self):
        #print("\nTest 5: Irradiancia negativa")
        #print("Datos de entrada:\nÁrea: 1.6 m², Irradiancia: -1 kWh/m²/día, Eficiencia: 0.18, Pérdidas: 0.8")
        with self.assertRaises(ValueError):
            calcularEnergiaPanelesPorDia(1.6, -1, 0.18, 0.8)
    # 6
    def test_eficiencia_negativa(self):
        #print("\nTest 6: Eficiencia negativa")
        #print("Datos de entrada:\nÁrea: 1.6 m², Irradiancia: 4.9 kWh/m²/día, Eficiencia: -0.1, Pérdidas: 0.8")
        with self.assertRaises(ValueError):
            calcularEnergiaPanelesPorDia(1.6, 4.9, -0.1, 0.8)
    # 7
    def test_precision_dos_decimales(self):
        #print("\nTest 7: Precisión de dos decimales")
        #print("Datos de entrada:\nÁrea: 2.0 m², Irradiancia: 5.0 kWh/m²/día, Eficiencia: 0.2, Pérdidas: 0.75")
        resultado = calcularEnergiaPanelesPorDia(2.0, 5.0, 0.2, 0.75)
        self.assertAlmostEqual(resultado, 1.5, places=2)
    # 8
    def test_precision_alta(self):
        #print("\nTest 8: Precisión alta")
        #print("Datos de entrada:\nÁrea: 1.234 m², Irradiancia: 5.678 kWh/m²/día, Eficiencia: 0.19, Pérdidas: 0.85")
        resultado = calcularEnergiaPanelesPorDia(1.234, 5.678, 0.19, 0.85)
        esperado = 1.234 * 5.678 * 0.19 * 0.85
        self.assertAlmostEqual(resultado, esperado, places=6)


if __name__ == '__main__':
    unittest.main()
