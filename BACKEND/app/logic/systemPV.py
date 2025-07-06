from irradiacion import simulacion_irradiacion
from TrainerModel import TrainerModel
from ModelAgent import ModelAgent

# Fijamos valores del paper
consumoU = 2.215     # kWh/día
LLP_U = 0.01         # 1 %
areaU = 8            # parámetro genérico, puede ajustarse
# Irradiación según paper, usa tu generador con valores típicos
irradiacion_data = simulacion_irradiacion(va=0.7, ra=4.9, vmax=5.7, vmin=3.8)

modelo = TrainerModel(areaU, consumoU, irradiacion_data,
                      paneles=0.18, bateria=0.90,
                      inversor=0.95, cableado=0.98)

modelo.entrenar_modelo_completo()
agente = ModelAgent(modelo)

oPP, oCB = agente.generateOptimoConfig(LLP_U)
print(f"Modelo → CA: {oPP:.3f}, Cs: {oCB:.3f}")
print("Paper → CA: 2.02, Cs: 0.793")
