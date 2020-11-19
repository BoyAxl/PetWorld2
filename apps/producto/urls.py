from django.urls import path
from .views import *

urlpatterns = [
    #path('',home, name = 'index'),
    path('',home.as_view(), name = 'index'),
    path('acerca_de_nosotros/',acerca_de_nosotros, name = 'acerca_de_nosotros'),
    path('productos/',productos, name ='productos'),
    path('productos/perro',productos_perro, name = 'productos_perro'),
    path('productos/gato',productos_gato, name = 'productos_gato'),
    path('producto/<slug:slug>/',detalleProducto, name = 'detalleProducto'),
    #### PATHS DE CRUDS ANIMALES ######
    path('crear_animal/',crearAnimal, name = 'crear_animal'),
    path('listar_animal/',listarAnimal, name = 'listar_animal'),
    path('editar_animal/<int:id>',editarAnimal, name = 'editar_animal'), #le estamos pasando el id
    path('eliminar_animal/<int:id>',eliminarAnimal, name = 'eliminar_animal'),
    #### PATHS DE CURDS DE PRODUCTOS ######
    #path('crear_producto/',crearProducto, name = 'crear_producto'),
    path('crear_producto/',crearProducto.as_view(), name = 'crear_producto'),
    #path('listar_productos/',listarProductos, name = 'listar_productos'),
    path('listar_productos/',listarProductos.as_view(), name = 'listar_productos'),
    #path('editar_producto/<int:id>',editarProducto, name = 'editar_producto'),
    path('editar_producto/<int:pk>',editarProducto.as_view(), name = 'editar_producto'),
    path('eliminar_producto/<int:pk>',eliminarProducto.as_view(), name = 'eliminar_producto'),

]
