from rest_framework import serializers
from .models import Baterias, Inversores, Paneles, Irradiacion

class BateriasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Baterias
        fields = ['url', 'id', 'modelo', 'precio', 'largo', 'ancho', 'alto', 'voltaje', 'eficiencia', 'capacidad', 'tipo', 'consumo_mensual']

class InversoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inversores
        fields = ['url', 'id', 'modelo', 'precio', 'potencia', 'tension_admisible', 'consumo_mensual', 'tiempo_vida', 'eficiencia']

class PanelesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paneles
        fields = ['url', 'id', 'modelo', 'precio', 'potencia', 'consumo_mensual', 'tiempo_vida', 'eficiencia', 'ancho', 'alto']

class IrradiacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Irradiacion
        fields = ['url', 'id', 'year', 'month', 'value']
