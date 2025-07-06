import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import linregress
from irradiacion import simulacion_irradiacion

def ca_fit(llp, c1, c2, c3, c4):
    return c1 * np.exp(c2 * llp) + c3 * np.exp(c4 * llp)

class TrainerModel:
    def __init__(self, areaU, consumoU, data, paneles, bateria, inversor, cableado):
        self.rango_dato = 366
        self.area = np.linspace(1, areaU, 30)
        self.consumo = [consumoU] * self.rango_dato
        self.data = data
        self.paneles = paneles
        self.bateria = bateria
        self.inversor = inversor
        self.cableado = cableado

        self.LLP_G = []
        self.CA_G = []
        self.Cs_G = []

        # Atributos para almacenar los coeficientes
        self.c1 = None
        self.c2 = None
        self.c3 = None
        self.c4 = None
        self.c5 = None
        self.c6 = None

    def train(self):
        for areaV in self.area:
            potenciaSPV = areaV * self.data * self.paneles * self.inversor * self.cableado
            residuo = potenciaSPV - self.consumo
            exceso = np.where(residuo > 0, residuo, 0)
            faltante = np.where(residuo < 0, -residuo, 0)

            total_exceso = np.sum(exceso)
            total_faltante = np.sum(faltante)
            EB = (total_exceso - total_faltante) * self.bateria
            EBA = EB / self.rango_dato

            LLP = total_faltante / np.sum(self.consumo)
            CA = np.sum(potenciaSPV) / np.sum(self.consumo)
            Cs = EBA / np.mean(self.consumo)

            self.LLP_G.append(LLP)
            self.CA_G.append(CA)
            self.Cs_G.append(Cs)

    def generar_p0_automatica(self):
        LLP_arr = np.array(self.LLP_G)
        CA_arr = np.array(self.CA_G)

        CA_max = np.max(CA_arr)
        CA_min = np.min(CA_arr)
        LLP_max = np.max(LLP_arr[LLP_arr > 0])

        c1 = (CA_max - CA_min) * 0.6
        c3 = (CA_max - CA_min) * 0.4
        c2 = -5 / LLP_max
        c4 = -1 / LLP_max
        return [c1, c2, c3, c4]

    def generateII(self):
        p0 = self.generar_p0_automatica()
        popt, _ = curve_fit(ca_fit, self.LLP_G, self.CA_G, p0=p0)
        self.c1, self.c2, self.c3, self.c4 = popt
        return popt

    def generateC5C6(self):
        slope, intercept, _, _, _ = linregress(self.CA_G, self.Cs_G)
        self.c6 = slope
        self.c5 = intercept
        return slope, intercept

    def entrenar_modelo_completo(self):
        self.train()
        self.generateII()
        self.generateC5C6()
