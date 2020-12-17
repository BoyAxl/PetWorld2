from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from apps.usuario.models import Usuario
from .forms import FormularioLogin, FormularioUsuario
#token de usuario
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
import json
from fcm_django.models import FCMDevice
# Create your views here.

@csrf_exempt
@require_http_methods(['POST'])
def guardar_token(request):
    #{token:xxxxxx}
    body = request.body.decode('utf-8')
    bodyDict = json.loads(body)

    token = bodyDict['token']

    existe = FCMDevice.objects.filter(registration_id = token, active=True)

    if len(existe)>0:
        return HttpResponseBadRequest(json.dumps({'mensaje':'el token ya existe'}))

    dispositivo = FCMDevice()
    dispositivo.registration_id = token
    dispositivo.active = True
    #si el usuario está logeado procederemos a enlazar
    if request.user.is_authenticated:
        dispositivo.user = request.user

    try:
        dispositivo.save()
        return HttpResponse(json.dumps({'mensaje':'token guardado'}))
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se has podido guardar'}))

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('petworld:index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated: #si ya estamos autenticados
            return HttpResponseRedirect(self.get_success_url()) #nos redirecciona ael index
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

class ListarUsuarios(ListView):
    model = Usuario
    template_name = 'usuarios/listar_usuarios.html'

    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True)

class CrearUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/crear_usuario.html'
    success_url = reverse_lazy('usuarios:listar_usuarios')

class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/registro_usuario.html'
    success_url = reverse_lazy('petworld:index')

def Perfil(request):
    return render (request,'usuarios/perfil.html')
