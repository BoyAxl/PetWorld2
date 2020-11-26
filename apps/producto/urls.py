from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    #path('',home, name = 'index'),
    path('',home.as_view(), name = 'index'),
    path('acerca_de_nosotros/',acerca_de_nosotros, name = 'acerca_de_nosotros'),
    path('administracion/',login_required(administracion), name ='administracion'),
    path('productos/',productos, name ='productos'),
    path('productos/perro',productos_perro, name = 'productos_perro'),
    path('productos/gato',productos_gato, name = 'productos_gato'),
    path('producto/<slug:slug>/',detalleProducto, name = 'detalleProducto'),
    #### PATHS DE CRUDS ANIMALES ######
    path('crear_animal/',login_required(crearAnimal), name = 'crear_animal'),
    path('listar_animal/',login_required(listarAnimal), name = 'listar_animal'),
    path('editar_animal/<int:id>',login_required(editarAnimal), name = 'editar_animal'), #le estamos pasando el id
    path('eliminar_animal/<int:id>',login_required(eliminarAnimal), name = 'eliminar_animal'),
    #### PATHS DE CURDS DE PRODUCTOS ######
    #path('crear_producto/',crearProducto, name = 'crear_producto'),
    path('crear_producto/',login_required(crearProducto.as_view()), name = 'crear_producto'),
    #path('listar_productos/',listarProductos, name = 'listar_productos'),
    path('listar_productos/',login_required(listarProductos.as_view()), name = 'listar_productos'),
    #path('editar_producto/<int:id>',editarProducto, name = 'editar_producto'),
    path('editar_producto/<int:pk>',login_required(editarProducto.as_view()), name = 'editar_producto'),
    path('eliminar_producto/<int:pk>',login_required(eliminarProducto.as_view()), name = 'eliminar_producto'),

]
