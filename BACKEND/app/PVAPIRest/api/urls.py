from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Usuarios',views.UserViewSet)
router.register(r'Libros',views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
