# Calculo de Energía Solar: Generada por Paneles Solares (Estimacion de producción energética diaria)
"""
Método basado en la Irradiancia Solar:
Usando directamente la irradiancia solar promedio en kWh/m²/día.

Fórmula:
E = A * r * H * PR

Energia_generada(kWh)= Areadelpanel(m2)*Irradianciasolar(kWh/m2/dia)*Eficienciadelpanel*FactordePerdidas

- A = Área del panel (m²): El área física del panel.
- r = Irradiancia solar (kWh/m²/día): Datos promedio de la radiación solar incidente en la superficie del panel para la ubicación (r = irradiacion ANUAL del area en kWh/m2/dia).
- H = Eficiencia del panel: Porcentaje de la energía solar que el panel puede convertir en electricidad (dado por el fabricante, ej. 18%, 21%). (H = eficiencia en terminos de radiacion solar).
-- Factor de Pérdidas: Considera diversas pérdidas en el sistema (temperatura, suciedad, sombreado, eficiencia del inversor, cableado, etc.). Un valor común es 0.8 (es decir, un 20% de pérdidas), pero puede variar entre 0.7 y 0.9.
- PR = Indice de rendimiento del panel solar:

"""
# [LINK: https://www.bluettipower.com/blogs/articles/solar-power-calculation-formula]
# Ejemplo de uso: modulo fotovoltaico
## Potencia nominal:
p_nominal = 250  # Wp (vatios pico)
## Superficie del panel (area del panel):
area_panel = 1.6  # m² (metros cuadrados)

## Irradiancia solar promedio (anual): La irradiancia horizontal global (GHI)
### Del Dataset de la NASA es ALLSKY_SFC_SW_DWN     CERES SYN1deg All Sky Surface Shortwave Downward Irradiance (kW-hr/m^2/day) [LINK: https://firstgreenconsulting.wordpress.com/2012/04/26/differentiate-between-the-dni-dhi-and-ghi/], se debe de sacar el promedio anual de la irradiancia solar en kWh/m²/día.
irradiancia_solar_anual = 4.9  # kWh/m²/día (valor promedio para una ubicación específica)

## Eficiencia del panel:
eficiencia_panel = 0.15  # 18% (valor típico para panel

## Indice de rendimiento del panel solar:
indice_rendimiento = 0.8  # 80% (considerando pérdidas)


def calcularEnergiaPanelesPorDia(area_panel, irradiancia_solar, eficiencia_panel, factor_perdidas):
    """
    Calcula la energía generada por un panel solar basado en su área, la irradiancia solar, la eficiencia del panel y el factor de pérdidas.

    Parámetros:
    area_panel (float): Área del panel en metros cuadrados (m²).
    irradiancia_solar (float): Irradiancia solar promedio en kWh/m²/día.
    eficiencia_panel (float): Eficiencia del panel como porcentaje (ej. 0.18 para 18%).
    factor_perdidas (float): Factor de pérdidas del sistema (ej. 0.8).

    Retorna:
    float: Energía generada por el panel en kWh/dia.
    """
    
    if area_panel <= 0 or irradiancia_solar <= 0 or eficiencia_panel < 0 or factor_perdidas <= 0:
        raise ValueError("Todos los parámetros deben ser mayores que cero.")
    
    energia_generada = area_panel * irradiancia_solar * eficiencia_panel * factor_perdidas
    return energia_generada # Produccion energetica diaria en kWh/día

"""
print("Producción energética diaria del panel solar:")
print(f"Área del panel: {area_panel} m²")
print(f"Irradiancia solar anual: {irradiancia_solar_anual} kWh/m²/día")
print(f"Eficiencia del panel: {eficiencia_panel * 100}%")
print(f"Índice de rendimiento del panel: {indice_rendimiento * 100}%")
print("Energía generada por el panel solar (kWh/día):")
print(calcularEnergiaPanelesPorDia(area_panel, irradiancia_solar_anual, eficiencia_panel, indice_rendimiento)*365)
"""