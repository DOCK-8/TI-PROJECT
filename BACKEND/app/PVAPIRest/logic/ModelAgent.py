import numpy as np
# from TrainerModel import TrainerModel

class ModelAgent:
    @staticmethod
    def optimoPotenciaPaneles(c1, c2, c3, c4, LLP):
        return c1 * np.exp(c2 * LLP) + c3 * np.exp(c4 * LLP)

    @staticmethod
    def optimoCapacidadBateria(c5, c6, CA):
        return c5 + c6 * CA

    @staticmethod
    def generateOptimoConfig(c1, c2, c3, c4, c5, c6, LLP_U):
        oPP = ModelAgent.optimoPotenciaPaneles(c1, c2, c3, c4, LLP_U)
        oCB = ModelAgent.optimoCapacidadBateria(c5, c6, oPP)
        return [oPP, oCB]
