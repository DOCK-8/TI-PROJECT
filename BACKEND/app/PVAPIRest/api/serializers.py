from rest_framework import serializers
from .models import User, Book

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id','nombre', 'correo']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['url','id', 'titulo', 'autor', 'disponible', 'usuario_id']
