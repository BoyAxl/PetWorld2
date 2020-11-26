from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.usuario.views import ListarUsuarios, CrearUsuario

urlpatterns = [
    path('listar_usuarios/',login_required(ListarUsuarios.as_view()),
        name='listar_usuarios'),
    path('crear_usuario/',login_required(CrearUsuario.as_view()),
        name='crear_usuario'),
]
