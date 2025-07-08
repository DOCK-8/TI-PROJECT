from .models import Baterias, Inversores, Paneles, Irradiacion
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.middleware.csrf import get_token
from logic.TrainerModel import TrainerModel
from logic.ModelAgent import ModelAgent
from logic.buscar_sistema_optimo import buscar_configuracion_optima
from logic.calcular_roi import calcularResumenROIyPayback
from django.conf import settings
from rest_framework import status
import json
import os


from .serializers import BateriasSerializer, InversoresSerializer, PanelesSerializer, IrradiacionSerializer


class BateriasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Baterias.objects.all().order_by('id')
    serializer_class = BateriasSerializer
    permission_classes = [permissions.IsAuthenticated]


class InversoresViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Inversores.objects.all().order_by('id')
    serializer_class = InversoresSerializer
    permission_classes = [permissions.IsAuthenticated]

class PanelesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Paneles.objects.all().order_by('id')
    serializer_class = PanelesSerializer
    permission_classes = [permissions.IsAuthenticated]

class IrradiacionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Irradiacion.objects.all().order_by('id')
    serializer_class = IrradiacionSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET'])
def get_token_api(request):
    token = get_token(request._request)
    return Response({'token':token})

@api_view(['POST'])
def solucionOptima(request):
    try:
        consumo = request.data.get('consumo_total', '')
        area = request.data.get('area_disponible', '')
        
        modelT = TrainerModel(float(area), float(consumo), 0.1898, 0.9405, 0.8931, 0.98)
        modelT.entrenar_modelo_completo()

        LLP_U = 0.01
        modelo = ModelAgent()

        c1 = modelT.c1
        c2 = modelT.c2
        c3 = modelT.c3
        c4 = modelT.c4
        c5 = modelT.c5
        c6 = modelT.c6

        oPP, oCB = modelo.generateOptimoConfig(c1, c2, c3, c4, c5, c6, LLP_U)
        configuracion = buscar_configuracion_optima(oPP, area, oCB)

        costo_total = (
            configuracion['panel_optimo']['costo_total_usd'] * configuracion['panel_optimo']['cantidad'] +
            configuracion['inversor_optimo']['costo_total'] * configuracion['inversor_optimo']['cantidad'] +
            configuracion['bateria_optima']['costo_total_usd'] * configuracion['bateria_optima']['cantidad']
        )

        answer = calcularResumenROIyPayback(costo_total, oPP, float(consumo), 0.70305)

        return Response({"configuracion": configuracion, "roi": answer})
    
    except Exception as e:
        print("ERROR:", str(e))
        return Response(
            {"error": str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )
