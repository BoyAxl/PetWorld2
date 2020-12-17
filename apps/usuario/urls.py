from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.usuario.views import ListarUsuarios, CrearUsuario, RegistrarUsuario, Perfil, guardar_token

urlpatterns = [
    path('listar_usuarios/',login_required(ListarUsuarios.as_view()),
        name='listar_usuarios'),
    path('crear_usuario/',login_required(CrearUsuario.as_view()),
        name='crear_usuario'),
    path('registro_usuario/',RegistrarUsuario.as_view(),
        name='registro_usuario'),
    path('perfil/',Perfil, name = 'perfil'),
    path('guardar-token/',guardar_token, name='guardar_token')
]
