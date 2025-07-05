"""
Método basado en la Irradiancia Solar:
Similar al anterior, pero usando directamente la irradiancia solar promedio en kWh/m²/día.

Fórmula:
Energia_generada(kWh)= Areadelpanel(m2)*Irradianciasolar(kWh/m2/dıa)*Eficienciadelpanel*FactordePerdidas

Área del panel (m²): El área física del panel.

Irradiancia solar (kWh/m²/día): Datos promedio de la radiación solar incidente en la superficie del panel para la ubicación.

Eficiencia del panel: Porcentaje de la energía solar que el panel puede convertir en electricidad (dado por el fabricante, ej. 18%, 21%).

Factor de Pérdidas: Considera diversas pérdidas en el sistema (temperatura, suciedad, sombreado, eficiencia del inversor, cableado, etc.). Un valor común es 0.8 (es decir, un 20% de pérdidas), pero puede variar entre 0.7 y 0.9.

"""

def calcularEnergiaPaneles(area_panel, irradiancia_solar, eficiencia_panel, factor_perdidas):
    """
    Calcula la energía generada por un panel solar basado en su área, la irradiancia solar, la eficiencia del panel y el factor de pérdidas.

    Parámetros:
    area_panel (float): Área del panel en metros cuadrados (m²).
    irradiancia_solar (float): Irradiancia solar promedio en kWh/m²/día.
    eficiencia_panel (float): Eficiencia del panel como porcentaje (ej. 0.18 para 18%).
    factor_perdidas (float): Factor de pérdidas del sistema (ej. 0.8).

    Retorna:
    float: Energía generada por el panel en kWh.
    """
    
    if area_panel <= 0 or irradiancia_solar <= 0 or eficiencia_panel < 0 or factor_perdidas <= 0:
        raise ValueError("Todos los parámetros deben ser mayores que cero.")
    
    energia_generada = area_panel * irradiancia_solar * eficiencia_panel * factor_perdidas
    return energia_generada