"""
Cálculo del ROI respecto al costo del sistema fotovoltaico y el ahorro anual en costos de energía,
considerando el tiempo necesario para recuperar lo invertido.

- El sistema fotovoltaico tiene un costo total.
- Por cada kWh generado, se ahorra un costo equivalente al precio del kWh de la red eléctrica.
- El sistema debe generar al menos lo necesario para cubrir el consumo del usuario.
"""

# Datos de entrada
costo_total_sistema = 10000  # USD
consumo_energia_diario = 50  # kWh/día
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
