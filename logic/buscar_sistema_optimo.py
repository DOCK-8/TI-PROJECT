'''
esa es si puedes crear una funcion en python que busque entre todos los paneles y segun una potencia 
y area que te envie me devuelva el id del panel de la base de datos y cantidad, lo mismo para bateria 
solo que en este caso te enviare la capacidad de bateria requerida, y que sea la optima o minima el 
costo de todos estos

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
    [1, 350, 1.6, 0.15, 0.8, 2500],  # [id, potencia (Wp), area (m²), eficiencia, factor de perdidas, costo (USD)]
    [2, 250, 1.5, 0.18, 0.4, 3000],
    [3, 100, 2.5, 0.20, 0.8, 2800],
    [4, 150, 1.8, 0.19, 0.3, 2200]
]
BDbateria = [
    [1, 5000, 12, 100],  # [id, capacidad (Wh), voltaje (V), costo (USD)]
    [2, 10000, 12, 150],
    [3, 7500, 24, 130],
    [4, 15000, 48, 200]
]
BDinversor = [
    [1, 3000, 12, 600],  # [id, potencia (W), voltaje (V), Costo (USD)]
    [2, 5000, 24, 550],
    [3, 10000, 48, 800],
    [4, 5000, 48, 600]
]


### Data input
consumo_hogar = 10  # kWh/día
area_disponible = 20  # m²
capacidad_bateria_requerida = 10000  # Wh (10 kWh)
capacidad_inversor_requerida = 50000  # W (5 kW)

## se requiere cantidad de paneles y bateria
cantidad_paneles = 0
cantidad_baterias = 0

"""Se usara la funcion de calcularEnergiaPanelesPorDia para calcular la energia generada por los paneles"""


def buscar_panel_optimo(consumo_hogar, area_disponible):
    mejor_opcion = None
    cantidad_paneles = 0  # Inicializar cantidad de paneles
    energia_requerida = consumo_hogar  # kWh/día
    
    mejor_energia_generada = 0  # Inicializar mejor energía generada
    mejor_costo = float('inf')  # Inicializar mejor costo a infinito
    
    for panel in BDpanel:
        id_panel, potencia, area, eficiencia, factor_perdidas, costo = panel
        print(panel)
        
        # Calcular la energía generada por el panel en un día
        energia_generada = calcularEnergiaPanelesPorDia(area, 4.6, eficiencia, factor_perdidas) # kWh/día (usando un valor promedio de irradiancia solar de 4.9 kWh/m²/día), cambiar por el dato real
        print (f"-------------\nEnergía generada por el panel {id_panel}: {energia_generada} kWh/día")
        
        
        paneles_necesarios = math.ceil(energia_requerida / energia_generada) # redondeo hacia arriba
        energia_generada_total = float(energia_generada * paneles_necesarios)
        costos_totales = costo * paneles_necesarios
        
        print(f"paneles necesarios para cumplir con el consumo: {paneles_necesarios}  Energía generada total: {energia_generada_total} kWh/día")
        
        # Verificar Area disponible
        if paneles_necesarios * area <= area_disponible:
            print(f"Panel {id_panel} cumple con el área disponible: {paneles_necesarios * area} m² <= {area_disponible} m²")
            
            # Verificar si la energía generada es suficiente
            if (energia_generada_total >= energia_requerida and energia_generada_total >= mejor_energia_generada and costos_totales < mejor_costo):
                print(f"Panel {id_panel} cumple con el consumo requerido: {energia_generada_total} kWh/día >= {energia_requerida} kWh/día")
                print(f"Costo total: {costos_totales} USD")
                mejor_opcion = panel
                mejor_energia_generada = energia_generada_total
                mejor_costo = costos_totales
                cantidad_paneles = int(paneles_necesarios)

    return mejor_opcion, cantidad_paneles, mejor_costo if mejor_opcion else None
print("Mejor Opcion: ", buscar_panel_optimo(consumo_hogar, area_disponible))

### buscar inversor optimo
def buscar_inversor_optimo(potencia_requerida): # potencia_requerida y costo minimo
    inversor_optimo = None
    cantidad_inversores = 0

    costo_minimo = 99999999999
    potencia_total_op = 0   
    for inversor in BDinversor:
        id_inversor, potencia, voltaje, costo = inversor

        cantidad_inv = math.ceil(potencia_requerida / potencia)  # Cantidad de inversores necesarios para cumplir con la potencia requerida
        potencia_total = potencia * cantidad_inv  # Potencia total que puede entregar el inversor
        costo_total = costo * cantidad_inv  # Costo total de los inversores necesarios
        
        if potencia_total >= potencia_requerida:
            if not inversor_optimo or potencia_total <= potencia_total_op:  # Elegir el inversor con menor potencia que cumpla el requisito
                if costo_minimo > costo_total:  # Comparar costo del inversor
                    print(f"Inversor {id_inversor} cumple con la potencia requerida: {potencia_total} W >= {potencia_requerida} W")
                    print(f"Cantidad de inversores necesarios: {cantidad_inv}")
                    print(f"Costo total: {costo_total} USD")
                    inversor_optimo = inversor
                    costo_minimo = costo_total  # Actualizar costo mínimo
                    potencia_total_op = potencia_total
                    cantidad_inversores = cantidad_inv  # Actualizar cantidad de inversores necesarios

    return inversor_optimo, cantidad_inversores, costo_minimo if inversor_optimo else None

print("Buscando inversor óptimo...")
print(buscar_inversor_optimo(capacidad_inversor_requerida))


def buscar_bateria_optima(capacidad_requerida):
    """
    Busca la bateria mas optima de una lista (mock de base de datos), cumpliendo con la capacidad 
    requerida al menor costo posible.

    Parametro:
        capacidad_requerida (int): Capacidad total necesaria en Wh (por ejemplo, 10000 para 10 kWh).

    Retorna:
        tuple: (id_bateria, cantidad_baterias, costo_total)
    """
    mejor_opcion = None
    menor_costo = float('inf')

    for bateria in BDbateria:
        id_bat, capacidad, voltaje, costo = bateria

        cantidad = int((capacidad_requerida / capacidad) + 0.9999)  # Redondeo hacia arriba
        costo_total = cantidad * costo

        if costo_total < menor_costo:
            menor_costo = costo_total
            mejor_opcion = (id_bat, cantidad, costo_total)

    return mejor_opcion


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
