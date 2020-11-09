from django.urls import path
from .views import crearAnimal

urlpatterns = [
    path('crear_animal/',crearAnimal, name = 'crear_animal')
]