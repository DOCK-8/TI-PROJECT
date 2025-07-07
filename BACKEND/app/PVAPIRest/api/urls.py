from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Baterias',views.BateriasViewSet)
router.register(r'Inversores',views.InversoresViewSet)
router.register(r'Paneles',views.PanelesViewSet)
router.register(r'Irradiacion',views.IrradiacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
