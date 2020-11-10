from django.urls import path
from .views import crearAnimal, listarAnimal

urlpatterns = [
    path('crear_animal/',crearAnimal, name = 'crear_animal'),
    path('listar_animal/',listarAnimal, name = 'listar_animal')
]