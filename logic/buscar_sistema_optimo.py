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
import math

BDpanel = [
    [1, 350, 1.6, 0.16, 0.8, 500],  # [id, potencia (Wp), area (m²), eficiencia, factor de perdidas, costo (USD)]
    [2, 250, 1.5, 0.18, 0.4, 300],
    [3, 100, 21.0, 0.20, 0.8, 600],
    [4, 150, 1.8, 0.19, 0.3, 900]
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
consumo_hogar = 20  # kWh/día
area_disponible = 10  # m²
capacidad_bateria_requerida = 10000  # Wh (10 kWh)

## se requiere cantidad de paneles y bateria
cantidad_paneles = 0
cantidad_baterias = 0

"""Se usara la funcion de calcularEnergiaPanelesPorDia para calcular la energia generada por los paneles"""


def buscar_panel_optimo(consumo_hogar, area_disponible): ## solo considera el area y consumo para buscar el panel optimo
    mejor_opcion = BDpanel[0]  # Iniciar con el primer panel como mejor opcion
    cantidad_paneles = 0  # Inicializar cantidad de paneles
    energia_requerida = consumo_hogar  # kWh/día
    
    energia_generada_pv = calcularEnergiaPanelesPorDia(mejor_opcion[2], 4.9, mejor_opcion[3], mejor_opcion[4])
    cantidad_paneles_pv = energia_requerida / energia_generada_pv  # Cantidad de paneles necesarios para cumplir con la energia requerida
    energia_generada_pv_total = energia_generada_pv * cantidad_paneles_pv  # Energia total generada por los paneles necesarios
    
    cantidad_paneles = int(cantidad_paneles_pv)  # Convertir a entero para la cantidad de paneles
    
    cumple_area = False
    cumple_consumo = False
    
    
    
    for panel in BDpanel:
        id_panel, potencia, area, eficiencia, factor_perdidas = panel
        print(panel)
        
        # Calcular la energía generada por el panel en un día
        energia_generada = calcularEnergiaPanelesPorDia(area, 4.6, eficiencia, factor_perdidas) # kWh/día (usando un valor promedio de irradiancia solar de 4.9 kWh/m²/día), cambiar por el dato real
        print (f"-------------\nEnergía generada por el panel {id_panel}: {energia_generada} kWh/día")
        
        
        paneles_necesarios = math.ceil(energia_requerida / energia_generada) # redondeo hacia arriba
        energia_generada_total = float(energia_generada * paneles_necesarios)
        
        print(f"paneles necesarios para cumplir con el consumo: {paneles_necesarios}  Energía generada total: {energia_generada_total} kWh/día")
        if paneles_necesarios * area <= area_disponible:
            print(f"Panel {id_panel} cumple con el área disponible: {paneles_necesarios * area} m² <= {area_disponible} m²")
            if (energia_generada_total >= energia_requerida and energia_generada_total >= energia_generada_pv_total) or panel == mejor_opcion:
                print(f"Panel {id_panel} cumple con el consumo requerido: {energia_generada_total} kWh/día >= {energia_requerida} kWh/día")
                mejor_opcion = panel
                energia_generada_pv = energia_generada_total
                
                cantidad_paneles = int(paneles_necesarios)
                cumple_area = True
                cumple_consumo = energia_generada_total >= energia_requerida

    return mejor_opcion, cantidad_paneles, cumple_area, cumple_consumo
print("Mejor Opcion: ", buscar_panel_optimo(consumo_hogar, area_disponible))

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
