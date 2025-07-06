from TrainerModel import TrainerModel
from ModelAgent import ModelAgent
import numpy as np

# Simulación o carga real de irradiación diaria
irradiacion_data = np.random.uniform(4.5, 5.2, 366)  # ejemplo temporal

# Entrenar el modelo con datos de usuario
modelo = TrainerModel(
    areaU=5,
    consumoU=2.2,
    data=irradiacion_data,
    paneles=0.18,
    bateria=0.9,
    inversor=0.95,
    cableado=0.98
)
modelo.entrenar_modelo_completo()

# Crear el agente con el modelo entrenado
agente = ModelAgent(modelo)

# Generar configuración óptima para un LLP deseado
oPP, oCB = agente.generateOptimoConfig(LLP_U=0.05)

print(f"Potencia óptima de paneles: {oPP:.2f} kWh")
print(f"Capacidad óptima de batería: {oCB:.2f} kWh")
