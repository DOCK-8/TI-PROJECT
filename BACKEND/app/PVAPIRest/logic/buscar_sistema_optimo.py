from logic.calcular_energia_panel import calcularEnergiaPanelesPorDia
from api.models import Paneles, Baterias, Inversores
import math

def buscar_panel_optimo(consumo_hogar, area_disponible, irradiancia_promedio=4.6):
    paneles = Paneles.objects.all()
    mejor_panel = None
    cantidad_paneles = 0
    menor_costo = float('inf')

    for p in paneles:
        try:
            ancho_m = (p.ancho or 0) / 1000
            alto_m = (p.alto or 0) / 1000
            area_panel = round(ancho_m * alto_m, 2)
            if area_panel <= 0:
                continue

            eficiencia = float(p.eficiencia or 0) / 100
            if eficiencia <= 0 or eficiencia > 1:
                continue

            perdidas = 0.15
            costo = float(p.precio or 0)
            if costo <= 0:
                continue

            energia_generada = round(area_panel * irradiancia_promedio * eficiencia * (1 - perdidas), 2)
            if energia_generada <= 0:
                continue

            paneles_necesarios = math.ceil(consumo_hogar / energia_generada)
            energia_total = energia_generada * paneles_necesarios
            area_total = paneles_necesarios * area_panel
            costo_total = costo * paneles_necesarios

            if area_total <= area_disponible and energia_total >= consumo_hogar:
                if costo_total < menor_costo:
                    mejor_panel = {
                        "id": p.id,
                        "modelo": p.modelo,
                        "potencia": float(p.potencia or 0),
                        "area_panel_m2": area_panel,
                        "eficiencia": eficiencia,
                        "costo_unitario": costo,
                        "energia_generada_por_panel_kwh_dia": energia_generada
                    }
                    cantidad_paneles = paneles_necesarios
                    menor_costo = costo_total

        except:
            continue

    if mejor_panel:
        return {
            "panel": mejor_panel,
            "cantidad": cantidad_paneles,
            "energia_total_kwh_dia": round(cantidad_paneles * mejor_panel["energia_generada_por_panel_kwh_dia"], 2),
            "costo_total_usd": round(menor_costo, 2)
        }
    return None


def buscar_bateria_optima(capacidad_requerida_wh):
    baterias = Baterias.objects.all()
    mejor_bateria = None
    menor_costo = float('inf')

    for b in baterias:
        try:
            capacidad = float(b.capacidad or 0)
            costo = float(b.precio or 0)
            if capacidad <= 0 or costo <= 0:
                continue

            cantidad = math.ceil(capacidad_requerida_wh / capacidad)
            costo_total = cantidad * costo

            if costo_total < menor_costo:
                mejor_bateria = {
                    "id": b.id,
                    "modelo": b.modelo,
                    "capacidad_wh": capacidad,
                    "voltaje": float(b.voltaje or 0),
                    "costo_unitario": costo
                }
                menor_costo = costo_total
                cantidad_baterias = cantidad
        except:
            continue

    if mejor_bateria:
        return {
            "bateria": mejor_bateria,
            "cantidad": cantidad_baterias,
            "costo_total_usd": round(menor_costo, 2)
        }
    return None


def buscar_inversor_optimo(consumo_diario_kwh):
    inversores = Inversores.objects.all()
    mejor_opcion = None
    menor_costo = float('inf')
    cantidad_optima = 0

    potencia_requerida_watts = consumo_diario_kwh * 1000 / 24  # Potencia necesaria en W

    for inv in inversores:
        try:
            potencia = float(inv.potencia or 0)  # en W
            precio = float(inv.precio or 0)      # en USD

            if potencia <= 0 or precio <= 0:
                continue  # datos inválidos

            cantidad = math.ceil(potencia_requerida_watts / potencia)
            potencia_total = cantidad * potencia
            costo_total = cantidad * precio

            if potencia_total >= potencia_requerida_watts and costo_total < menor_costo:
                mejor_opcion = {
                    "id": inv.id,
                    "modelo": inv.modelo,
                    "potencia_unitaria": potencia,
                    "precio_unitario": precio,
                    "cantidad": cantidad,
                    "potencia_total": potencia_total,
                    "costo_total": round(costo_total, 2)
                }
                menor_costo = costo_total
                cantidad_optima = cantidad

        except Exception as e:
            continue  # Silenciar errores por ahora

    return mejor_opcion or {"message": "No se encontró inversor que cumpla los requisitos"}

def buscar_configuracion_optima(consumo_hogar_kwh_dia, area_disponible_m2, capacidad_bateria_requerida_wh):
    return {
        "panel_optimo": buscar_panel_optimo(consumo_hogar_kwh_dia, area_disponible_m2),
        "bateria_optima": buscar_bateria_optima(capacidad_bateria_requerida_wh),
        "inversor_optimo": buscar_inversor_optimo(consumo_hogar_kwh_dia)
    }
