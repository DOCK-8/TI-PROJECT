from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Bateria',views.BateriasViewSet)
router.register(r'Inversore',views.InversoresViewSet)
router.register(r'Panele',views.PanelesViewSet)
router.register(r'Irradiacion',views.IrradiacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token', views.get_token_api),
    path('consumo-area', views.generate_model),
    path('solucion-optima', views.solucionOptima),
]
