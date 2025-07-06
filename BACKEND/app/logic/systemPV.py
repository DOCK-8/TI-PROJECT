demands = 0 #demanda del usuario
efficienciaPV = 0 #efficciencia del sistema PV
efficienciaI = 0 #efficciencia del inversor
efficienciaC = 0 #efficciencia del cableado
efficienciaB = 0 #efficciencia del bateria
areaPV = 0 #area de uso para el sistema PV
irradiacionS = 0 #irradiacion solar

#Produccion del sistema PV
producePV = areaPV*irradiacionS*efficienciaPV*efficienciaI*efficienciaC
#energy difference
energyD = 0
for produce in producePV:
    energyD += produce-demands

if()
