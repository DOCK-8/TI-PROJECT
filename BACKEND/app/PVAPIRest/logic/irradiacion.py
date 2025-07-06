import numpy as np
# ra Radiacion Anual
# va Varianza
def simulacion_irradiacion(va, ra, vmax, vmin):
    rango = 366 #rango para la dataset
    dias = np.arange(rango) #rango de dias 0-366
    pico = 0.5 #aleatoria para ver la irradiacion mas alta
    data = ra + va*np.sin(2*np.pi*dias/rango+pico)
    # agregamos ruido con tecnica de distribucion gauciana
    # data = centro, intervalo, data
    data += np.random.normal(0, 0.15, rango)
    # limpiamos datos fuera de rango
    data = np.clip(data, vmin, vmax)
    return data
