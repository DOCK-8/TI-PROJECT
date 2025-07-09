from logic.calcular_energia_panel import calcularEnergiaPanelesPorDia

def prueba_t(nombre_prueba, area, irradiancia, eficiencia, perdidas, esperado=None):
    print(f"\n--- {nombre_prueba} ---")
    print(f"Datos de entrada:\nÁrea: {area} m², Irradiancia: {irradiancia} kWh/m²/día, Eficiencia: {eficiencia}, Pérdidas: {perdidas}")
    try:
        resultado = calcularEnergiaPanelesPorDia(area, irradiancia, eficiencia, perdidas)
        print(f"Resultado obtenido: {resultado:.6f} kWh/día")
        if esperado is not None:
            print(f"Esperado aprox.: {esperado:.6f} kWh/día")
            print("✅ PASA" if abs(resultado - esperado) < 0.0001 else "❌ NO PASA")
        else:
            print("✅ Cálculo exitoso (sin valor esperado definido)")
    except Exception as e:
        print(f"❌ Error capturado: {e}")

# === PRUEBAS ===

# Prueba 1: Valores normales
prueba_t(
    "\nTest 1: Valores normales",
    area=1.6,
    irradiancia=4.9,
    eficiencia=0.15,
    perdidas=0.8,
    esperado=1.6 * 4.9 * 0.15 * 0.8
)

# Prueba 2: Alta irradiancia y eficiencia
prueba_t(
    "\nTest 2: Valores altos",
    area=10.0,
    irradiancia=7.0,
    eficiencia=0.22,
    perdidas=0.9,
    esperado=10.0 * 7.0 * 0.22 * 0.9
)

# Prueba 3: Área cero (debe fallar)
prueba_t(
    "\nTest 3: Área cero",
    area=0,
    irradiancia=4.9,
    eficiencia=0.18,
    perdidas=0.8
)

# Prueba 4: Factor de pérdidas cero (debe fallar)
prueba_t(
    "\nTest 4: Factor de pérdidas cero",
    area=1.6,
    irradiancia=4.9,
    eficiencia=0.18,
    perdidas=0
)

# Prueba 5: Irradiancia negativa (debe fallar)
prueba_t(
    "\nTest 5: Irradiancia negativa",
    area=1.6,
    irradiancia=-1.0,
    eficiencia=0.18,
    perdidas=0.8
)

# Prueba 6: Eficiencia negativa (debe fallar)
prueba_t(
    "\nTest 6: Eficiencia negativa",
    area=1.6,
    irradiancia=4.9,
    eficiencia=-0.1,
    perdidas=0.8,
)

# Prueba 7: Precisión de dos decimales
prueba_t(
    "\nTest 7: Precisión de dos decimales",
    area=2.0,
    irradiancia=5.0,
    eficiencia=0.2,
    perdidas=0.75,
    esperado=1.5
)

# Prueba 8: Precisión alta
prueba_t(
    "\nTest 8: Precisión alta",
    area=1.234,
    irradiancia=5.678,
    eficiencia=0.19,
    perdidas=0.85,
    esperado=1.234 * 5.678 * 0.19 * 0.85
)