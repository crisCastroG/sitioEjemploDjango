from django.urls import path, include
from .views import hola, index, saludo

urlpatterns = [
    #URLS DE APLICACION
    path('', index, name='index'),
    path('saludo/', saludo),
    path('hola/', hola)
]
