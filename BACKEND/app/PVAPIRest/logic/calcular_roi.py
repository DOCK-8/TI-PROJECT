"""
Cálculo del ROI respecto al costo del sistema fotovoltaico y el ahorro anual en costos de energía,
considerando el tiempo necesario para recuperar lo invertido.

- El sistema fotovoltaico tiene un costo total.
- Por cada kWh generado, se ahorra un costo equivalente al precio del kWh de la red eléctrica.
- El sistema debe generar al menos lo necesario para cubrir el consumo del usuario.
"""

# Datos de entrada
costo_total_sistema = 10000  # USD
consumo_energia_diario = 30  # kWh/día
energia_generada_diaria = 40  # kWh/día por el sistema FV
costo_kwh_red = 0.25  # USD/kWh (tarifa de red eléctrica)

def calcularROI(costo_total_sistema, energia_generada_diaria, consumo_diario, costo_kwh_red):
    """
    Calcula el ROI (retorno de inversión) considerando solo el consumo del usuario.
    
    - Si se genera más de lo que se consume, se asume que el excedente no se vende.
    - Si se genera menos, el ahorro es proporcional a lo generado.

    Retorna:
    - ROI en días y años
    - Ahorro diario
    """
    if costo_total_sistema <= 0 or energia_generada_diaria <= 0 or consumo_diario <= 0 or costo_kwh_red <= 0:
        raise ValueError("Todos los valores deben ser mayores que cero.")
    
    if energia_generada_diaria < consumo_diario:
        print("Advertencia: La energía generada es menor que el consumo diario. El ahorro se calculará solo por la energía generada.")
    energia_utilizada = min(energia_generada_diaria, consumo_diario) # Elegir la menor entre lo generado y lo consumido
    ahorro_diario = energia_utilizada * costo_kwh_red
    roi_dias = costo_total_sistema / ahorro_diario
    roi_anios = roi_dias / 365

    return roi_dias, roi_anios, ahorro_diario

############# calculo de recuperación de la inversión (payback) solar
# periodo de amortización:  tiempo que se tarda en recuperar el coste inicial de instalación del sistema.  
# retorno de la inversión en paneles solares
"""
coste real de la instalación de energía solar una vez solicitados los incentivos. 
coste de la electricidad de la compañía eléctrica, indica cuánto tiempo se tarda en amortizar el sistema.

"""

def calcularSolarPayback(costo_total_sistema, costo_electricidad, electricidad_diaria_usada):
    """
    Calcula el tiempo de recuperación de la inversión (payback) en días y años.
    No toma en cuenta los incentivos o créditos fiscales, solo el costo total del sistema y el ahorro diario.
    
    (Total System Cost - Value of Incentives) ÷ Cost of Electricity ÷ Annual Electricity Usage = Payback Period
    
    [LINK: https://unboundsolar.com/solar-information/return-on-solar-investment#roi-calculator]
    Retorna:
    - Tiempo de recuperación en días y años
    """
    if costo_total_sistema <= 0 or costo_electricidad <= 0 or electricidad_diaria_usada <= 0:
        raise ValueError("El costo total del sistema, el costo de electricidad o la electricidad anual usada deben ser mayores que cero.")
    
    electricidad_anual_usada = electricidad_diaria_usada *365  # Consumo anual de electricidad en kWh
    payback_anios = costo_total_sistema / costo_electricidad / electricidad_anual_usada  
    payback_dias = payback_anios * 365  # Convertir a días    

    return payback_dias, payback_anios

# Ejecución
roi_dias, roi_anios, ahorro_diario = calcularROI(
    costo_total_sistema,
    energia_generada_diaria,
    consumo_energia_diario,
    costo_kwh_red
)


print("===== CÁLCULO DEL ROI =====")
print(f"Consumo diario: {consumo_energia_diario} kWh")
print(f"Energía generada por el sistema: {energia_generada_diaria} kWh")
print(f"Ahorro diario real: ${ahorro_diario:.2f}")
print(f"ROI estimado: {roi_dias:.1f} días ({roi_anios:.2f} años)")


print("===== CÁLCULO DEL PAYBACK =====")
payback_dias, payback_anios = calcularSolarPayback(
    costo_total_sistema,
    costo_kwh_red,
    consumo_energia_diario
)
print(f"Tiempo de recuperación de la inversión: {payback_dias:.1f} días ({payback_anios:.2f} años)")