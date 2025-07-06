from logic.ModelAgent import ModelAgent
from logic.TrainerModel import TrainerModel

def generateModel(Consumo_U, Area_U):
    irradiacion = #traer de model
    paneles = 0
    bateria = 0
    inversor = 0
    cableado =  0
    mTrainer = TrainerModel(Area_U, Consumo_U, irradiacion, paneles, bateria, inversor, cableado) 
    mTrainer.entrenar_modelo_completo()
    modelo = ModelAgente(mTrainer)
    return modelo

def generateSO(potencia, capacidad, Area_U):


def generateOPC(Agente, LLC_U):
    oPP, oCB = Agente.generateOptimoConfig(LLC_U)
    generateSO(oPP, oCB, Agente.areaUS)
