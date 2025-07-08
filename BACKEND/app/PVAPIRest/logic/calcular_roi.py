import json

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
    
    notas = []
    if energia_generada_diaria < consumo_diario:
        notas.append("La energía generada es menor que el consumo diario. El ahorro se calcula solo por la energía generada.")
    elif energia_generada_diaria > consumo_diario:
        notas.append("La energía generada excede el consumo diario. El ahorro se calcula solo sobre el consumo del usuario, sin considerar venta de excedentes.")
    else:
        notas.append("La energía generada es igual al consumo diario.")

    energia_utilizada = min(energia_generada_diaria, consumo_diario)  # Solo lo que se puede usar
    ahorro_diario = energia_utilizada * costo_kwh_red
    retorno_inversion_dias = costo_total_sistema / ahorro_diario
    retorno_inversion_anios = retorno_inversion_dias / 365

    return {
        "ahorro_diario_soles": round(ahorro_diario, 2),
        "retorno_inversion_dias": round(retorno_inversion_dias, 2),
        "retorno_inversion_anios": round(retorno_inversion_anios, 2),
        "notas": notas
    }

def calcularPayback(costo_total_sistema, costo_kwh_red, consumo_diario):
    """
    Calcula el tiempo de recuperación de la inversión (payback) en días y años.
    No considera incentivos ni venta de excedentes.
    
    (Costo total del sistema) / (costo de electricidad * consumo anual) = tiempo de recuperación
    """
    if costo_total_sistema <= 0 or costo_kwh_red <= 0 or consumo_diario <= 0:
        raise ValueError("Todos los valores deben ser mayores que cero.")

    consumo_anual_kwh = consumo_diario * 365
    tiempo_recuperacion_anios = costo_total_sistema / (costo_kwh_red * consumo_anual_kwh)
    tiempo_recuperacion_dias = tiempo_recuperacion_anios * 365

    return {
        "tiempo_recuperacion_dias": round(tiempo_recuperacion_dias, 2),
        "tiempo_recuperacion_anios": round(tiempo_recuperacion_anios, 2)
    }

def calcularResumenROIyPayback(costo_total_sistema, consumo_diario_kwh, energia_generada_diaria_kwh, costo_kwh_red):
    """
    Calcula el resumen general del ROI y del período de recuperación.
    Devuelve un objeto estructurado con nombres claros y notas interpretativas.
    """
    roi = calcularROI(costo_total_sistema, energia_generada_diaria_kwh, consumo_diario_kwh, costo_kwh_red)
    payback = calcularPayback(costo_total_sistema, costo_kwh_red, consumo_diario_kwh)

    return {
        "datos_entrada": {
            "costo_total_sistema_soles": costo_total_sistema,
            "consumo_diario_kwh": consumo_diario_kwh,
            "energia_generada_diaria_kwh": energia_generada_diaria_kwh,
            "tarifa_red_soles_kwh": costo_kwh_red
        },
        "analisis": {
            "retorno_inversion": {
                "ahorro_diario_soles": roi["ahorro_diario_soles"],
                "dias": roi["retorno_inversion_dias"],
                "anios": roi["retorno_inversion_anios"]
            },
            "tiempo_recuperacion": {
                "dias": payback["tiempo_recuperacion_dias"],
                "anios": payback["tiempo_recuperacion_anios"]
            }
        },
        "notas": roi["notas"] + [
            "No se incluyen incentivos gubernamentales ni venta de excedentes.",
            "La recuperación de inversión considera solo el reemplazo del consumo de red eléctrica."
        ]
    }
