from django.urls import path
from .views import crearAnimal, listarAnimal, editarAnimal

urlpatterns = [
    path('crear_animal/',crearAnimal, name = 'crear_animal'),
    path('listar_animal/',listarAnimal, name = 'listar_animal'),
    path('editar_animal/<int:id>',editarAnimal, name = 'editar_animal') #le estamos pasando el id 
]