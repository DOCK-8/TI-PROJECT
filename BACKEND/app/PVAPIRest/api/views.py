from .models import Baterias, Inversores, Paneles, Irradiacion
from rest_framework import permissions, viewsets

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
