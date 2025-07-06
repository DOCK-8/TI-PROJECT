from logic.ModelAgent import ModelAgent
from logic.TrainerModel import TrainerModel
from logic.buscar_sistema_optimo import buscar_panel_optimo, buscar_inversor_optimo, buscar_bateria_optima

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
    panel = buscar_panel_optimo(potencia, Area_U)
    inversor = buscar_inversor_optimo(potencia)
    bateria = buscar_bateria_optima(capacidad)
    return [panel, inversor, bateria]


def generateOPC(Agente, LLC_U):
    oPP, oCB = Agente.generateOptimoConfig(LLC_U)
    generateSO(oPP, oCB, Agente.areaUS)
