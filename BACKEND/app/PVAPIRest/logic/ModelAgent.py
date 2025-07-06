import numpy as np
from TrainerModel import TrainerModel

class ModelAgent:
    def __init__(self, trainer_model):
        self.trainer = trainer_model

    def optimoPotenciaPaneles(self, LLP):
        return self.trainer.c1 * np.exp(self.trainer.c2 * LLP) + \
               self.trainer.c3 * np.exp(self.trainer.c4 * LLP)

    def optimoCapacidadBateria(self, CA):
        return self.trainer.c5 + self.trainer.c6 * CA

    def generateOptimoConfig(self, LLP_U):
        oPP = self.optimoPotenciaPaneles(LLP_U)
        oCB = self.optimoCapacidadBateria(oPP)
        return [oPP, oCB]
