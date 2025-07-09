from logic.calcular_roi import calcularROI, calcularPayback, calcularResumenROIyPayback

# Funcion para probar ROI
def prueba_ROI(nombre_prueba, costo_total, consumo_diario, energia_generada_diaria, costo_kwh_red, esperado=None):
    print(f"\n--- {nombre_prueba} ---")
    print(f"Datos de entrada:\nCosto total del sistema: {costo_total}, Consumo diario: {consumo_diario}, Energía generada diaria: {energia_generada_diaria}, Costo kWh red: {costo_kwh_red}")
    try:
        resultado = calcularROI(costo_total, consumo_diario, energia_generada_diaria, costo_kwh_red)
        print(f"Resultado obtenido: {resultado}")
        if esperado is not None:
            print(f"Esperado: {esperado}")
            print("✅ PASA" if resultado == esperado else "❌ NO PASA")
        else:
            print("✅ Cálculo exitoso (sin valor esperado definido)")
    except Exception as e:
        print(f"❌ Error capturado: {e}")

# Funcion para payback        
def prueba_payback (nombre_prueba, costo_total,  costo_kwh_red, consumo_diario, esperado=None):
    print(f"\n--- {nombre_prueba} ---")
    print(f"Datos de entrada:\nCosto total del sistema: {costo_total}, Consumo diario: {consumo_diario}, Costo kWh red: {costo_kwh_red}")
    try:
        resultado = calcularPayback(costo_total, costo_kwh_red, consumo_diario)
        print(f"Resultado obtenido: {resultado}")
        if esperado is not None:
            print(f"Esperado: {esperado}")
            print("✅ PASA" if resultado == esperado else "❌ NO PASA")
        else:
            print("✅ Cálculo exitoso (sin valor esperado definido)")
    except Exception as e:
        print(f"❌ Error capturado: {e}")
        
# Funcion para resumen
def prueba_Resumen(nombre_prueba, costo_total, consumo_diario, energia_generada_diaria, costo_kwh_red, esperado=None):
    print(f"\n--- {nombre_prueba} ---")
    print(f"Datos de entrada:\nCosto total del sistema: {costo_total}, Consumo diario: {consumo_diario}, Energía generada diaria: {energia_generada_diaria}, Costo kWh red: {costo_kwh_red}")
    try:
        resultado = calcularResumenROIyPayback(costo_total, consumo_diario, energia_generada_diaria, costo_kwh_red)
        print(f"Resultado obtenido: {resultado}")
        if esperado is not None:
            print(f"Esperado: {esperado}")
            print("✅ PASA" if resultado == esperado else "❌ NO PASA")
        else:
            print("✅ Cálculo exitoso (sin valor esperado definido)")
    except Exception as e:
        print(f"❌ Error capturado: {e}")
        
        
# === PRUEBAS ===

## Pruebas de ROI
# Prueba 1: Generación igual al consumo
prueba_ROI(
    "Test 1: Generación igual al consumo",
    costo_total=10000,
    consumo_diario=30,
    energia_generada_diaria=30,
    costo_kwh_red=0.25,
    esperado={
        "ahorro_diario_soles": 7.5,
        "retorno_inversion_dias": 1333.33,
        "retorno_inversion_anios": 3.65,
        "notas": ["La energía generada es igual al consumo diario."]
    }
)
# Prueba 2: Generación menor que el consumo
prueba_ROI(
    "Test 2: Generación menor que el consumo",
    costo_total=8000,
    consumo_diario=30,
    energia_generada_diaria=20,
    costo_kwh_red=0.3,
    esperado={
        "ahorro_diario_soles": 6.0,
        "retorno_inversion_dias": 1333.33,
        "retorno_inversion_anios": 3.65,
        "notas": ["La energía generada excede el consumo diario. El ahorro se calcula solo sobre el consumo del usuario, sin considerar venta de excedentes."]
    }
)
# Prueba 3: Generación mayor que el consumo
prueba_ROI(
    "Test 3: Generación mayor que el consumo",
    costo_total=15000,
    consumo_diario=30,
    energia_generada_diaria=50,
    costo_kwh_red=0.2,
    esperado={
        "ahorro_diario_soles": 6.0,
        "retorno_inversion_dias": 2500.0,
        "retorno_inversion_anios": 6.85,
        "notas": ["La energía generada es menor que el consumo diario. El ahorro se calcula solo por la energía generada."]
    }
)
# Prueba 4: Valores inválidos
prueba_ROI(
    "Test 4: Valores inválidos",
    costo_total=0,
    consumo_diario=20,
    energia_generada_diaria=30,
    costo_kwh_red=0.25
)

## pruebas de Payback
# Prueba 5: Valores correctos
prueba_payback(
    "Test 5: Valores correctos",
    costo_total=10000,
    costo_kwh_red=0.25,
    consumo_diario=30,
    esperado={
        "tiempo_recuperacion_dias": 1333.33,
        "tiempo_recuperacion_anios": 3.65
    }
)
# Prueba 6: Valores inválidos
prueba_payback(
    "Test 6: Valores inválidos",
    costo_total=-10000,
    costo_kwh_red=0.25,
    consumo_diario=30,
)

## pruebas de Resumen
# Prueba 7: Resumen completo
prueba_Resumen(
    "Test 7: Resumen completo",
    costo_total=12000,
    consumo_diario=25,
    energia_generada_diaria=30,
    costo_kwh_red=0.22,
    esperado={
        "datos_entrada": {
            "costo_total_sistema_soles": 12000,
            "consumo_diario_kwh": 25,
            "energia_generada_diaria_kwh": 30,
            "tarifa_red_soles_kwh": 0.22
        },
        "analisis": {
            "retorno_inversion": {
                "ahorro_diario_soles": 5.5,
                "dias": 2181.82,
                "anios": 5.98
            },
            "tiempo_recuperacion": {
                "dias": 2181.82,
                "anios": 5.98
            }
        },
        'notas':['La energía generada excede el consumo diario. El ahorro se calcula solo sobre el consumo del usuario, sin considerar venta de excedentes.', 'No se incluyen incentivos gubernamentales ni venta de excedentes.', 'La recuperación de inversión considera solo el reemplazo del consumo de red eléctrica.']
    }
)