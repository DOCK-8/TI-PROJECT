import unittest
from irradiacion import simulacion_irradiacion
from TrainerModel import TrainerModel
from ModelAgent import ModelAgent

class TestModelPV(unittest.TestCase):
    def test_valores_vs_paper(self):
        consumoU = 2.215
        LLP_U = 0.01
        areaU = 8
        irradiacion_data = simulacion_irradiacion(va=0.7, ra=4.9, vmax=5.7, vmin=3.8)

        modelo = TrainerModel(areaU, consumoU, irradiacion_data,
                              paneles=0.18, bateria=0.90,
                              inversor=0.95, cableado=0.98)
        modelo.entrenar_modelo_completo()

        agente = ModelAgent(modelo)
        oPP, oCB = agente.generateOptimoConfig(LLP_U)

        CA_paper = 2.02
        Cs_paper = 0.793

        # Comparaciones con tolerancia
        self.assertAlmostEqual(oPP, CA_paper, delta=0.15, msg="Potencia óptima fuera del rango esperado")
        self.assertAlmostEqual(oCB, Cs_paper, delta=0.05, msg="Capacidad de batería fuera del rango esperado")

if __name__ == '__main__':
    unittest.main()
