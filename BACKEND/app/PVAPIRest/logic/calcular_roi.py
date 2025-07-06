

def calcularROI(costo_total, ahorros_ani):
    if costo_total <= 0:
        raise ValueError("El costo total debe ser mayor que cero.")
    
    roi = (costo_total / ahorros_ani)
    return roi