from django.contrib import admin
from .models import Irradiacion, Paneles, Baterias, Inversores

# Register your models here.
admin.site.register(Irradiacion)
admin.site.register(Paneles)
admin.site.register(Baterias)
admin.site.register(Inversores)
