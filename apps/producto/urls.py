from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name = 'index'),
    path('acerca_de_nosotros/',acerca_de_nosotros, name = 'acerca_de_nosotros'),
    path('productos/',productos, name = 'productos'),
    #### PATHS DE CRUDS ANIMALES ######
    path('crear_animal/',crearAnimal, name = 'crear_animal'),
    path('listar_animal/',listarAnimal, name = 'listar_animal'),
    path('editar_animal/<int:id>',editarAnimal, name = 'editar_animal'), #le estamos pasando el id
    path('eliminar_animal/<int:id>',eliminarAnimal, name = 'eliminar_animal'),
    #### PATHS DE CURDS DE PRODUCTOS ######
    path('crear_producto/',crearProducto, name = 'crear_producto')

]
