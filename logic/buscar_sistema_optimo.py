'''
esa es si puedes crear una funcion en python que busque entre todos los paneles y segun una potencia y area que te envie me devuelva el id del panel de la base de datos y cantidad, lo mismo para bateria solo que en este caso te enviare la capacidad de bateria requerida, y que sea la optima o minima el costo de todos estos

ahora yo le pasare la energia que se necesita

y necesitamos que se busque en la base de datos que panel cumple con ese criterio

asi como la cantidad

osea que panel genera esa cantidad de energia que se necesita

y lo que entrega son 3 datos

el area que tenemos disponible para poner los paneles, consumo hogar, capacidad de bateria requerida
'''
from calcular_energia_panel import calcularEnergiaPanelesPorDia

BDpanel = [
    [1, 300, 1.6, 0.18, 0.8],  # [id, potencia (Wp), area (m²), eficiencia, factor de perdidas]
    [2, 250, 1.5, 0.18, 0.8],
    [3, 400, 2.0, 0.20, 0.8],
    [4, 350, 1.8, 0.19, 0.8]
]
BDbateria = [
    [1, 5000, 12, 100],  # [id, capacidad (Wh), voltaje (V), costo (USD)]
    [2, 10000, 12, 150],
    [3, 7500, 24, 130],
    [4, 15000, 48, 200]
]
BDinversor = [
    [1, 3000, 12],  # [id, potencia (W), voltaje (V)
    [2, 5000, 24],
]


### Data input
consumo_hogar = 10  # kWh/día
area_disponible = 10  # m²
capacidad_bateria_requerida = 10000  # Wh (10 kWh)

## se requiere cantidad de paneles y bateria
cantidad_paneles = 0
cantidad_baterias = 0

"""Se usara la funcion de calcularEnergiaPanelesPorDia para calcular la energia generada por los paneles"""

def buscar_panel_optimo(consumo_hogar, area_disponible):
    mejor_opcion = None
    energia_requerida = consumo_hogar  # kWh/día
    area_utilizada = 0
    
    for panel in BDpanel:
        id_panel, potencia, area, eficiencia, factor_perdidas = panel
        
        # Calcular la energía generada por el panel en un día
        energia_generada = calcularEnergiaPanelesPorDia(area, 4.9, eficiencia, factor_perdidas) # kWh/día (usando un valor promedio de irradiancia solar de 4.9 kWh/m²/día), cambiar por el dato real
        print (f"Energía generada por el panel {id_panel}: {energia_generada} kWh/día")
    

    return 0 #panel_optimo, cantidad_paneles
buscar_panel_optimo(consumo_hogar, area_disponible)

"""
def buscar_bateria_optima(capacidad_bateria_requerida):
    global BDbateria
    bateria_optima = None
    cantidad_baterias = 0

    for bateria in BDbateria:
        id_bateria, capacidad, voltaje = bateria

        if capacidad >= capacidad_bateria_requerida:
            if not bateria_optima or capacidad < bateria_optima[1]:  # Elegir la batería con menor capacidad que cumpla el requisito
                bateria_optima = bateria
                cantidad_baterias = 1  # Solo se necesita una batería que cumpla el requisito

    return bateria_optima, cantidad_baterias

"""
"""
### Probar funciones
print("Buscando panel óptimo...")
panel_optimo, cantidad_paneles = buscar_panel_optimo(consumo_hogar, area_disponible)

if panel_optimo:
    print(f"Panel óptimo encontrado: ID {panel_optimo[0]}, Potencia {panel_optimo[1]} Wp, Área {panel_optimo[2]} m²")
    print(f"Cantidad de paneles necesarios: {cantidad_paneles}")   
else:
    print("No se encontró un panel que cumpla con los requisitos.")

print("Buscando batería óptima...")
if capacidad_bateria_requerida > 0:
    bateria_optima, cantidad_baterias = buscar_bateria_optima(capacidad_bateria_requerida)

    if bateria_optima:
        print(f"Batería óptima encontrada: ID {bateria_optima[0]}, Capacidad {bateria_optima[1]} Wh, Voltaje {bateria_optima[2]} V")
        print(f"Cantidad de baterías necesarias: {cantidad_baterias}")
    else:
        print("No se encontró una batería que cumpla con los requisitos.")
        
"""
