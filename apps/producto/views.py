from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AnimalForm, ProductoForm
from .models import Animal, Producto
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
class home(TemplateView):  #Esta es una Vista basada en una Clase <3
    template_name = 'index.html'
    def get(self,request,*args,**kwargs):
        productos = Producto.objects.all()
        return render (request,self.template_name,{'productos':productos}) #funcion que renderiza, pinta un template con la información que deseamos

def acerca_de_nosotros(request):
    return render (request,'acerca_de_nosotros.html')

def administracion(request):
    return render (request,'administracion.html')

def productos(request):
    productos = Producto.objects.all()

    paginator = Paginator(productos,10)  # cuantos productos se muestran por página
    page = request.GET.get('page') #guarda la pagina actual
    productos= paginator.get_page(page) #le enviamos al template los productos de la pagina page
    return render (request,'productos.html',{'productos':productos})

def productos_perro(request):
    productos = Producto.objects.filter(animal_id = Animal.objects.get(nombre__iexact = 'Perro'))
    return render (request,'productos.html',{'productos':productos})

def productos_gato(request):
    productos = Producto.objects.filter(animal_id = Animal.objects.get(nombre__iexact = 'Gato'))
    return render (request,'productos.html',{'productos':productos})

def detalleProducto(request,slug):
    producto = get_object_or_404(Producto,slug = slug)
    return render(request,'producto.html',{'producto':producto})

###################  CRUDS Animales ####################
# que nos permite crear un objeto del tipo Animal
def crearAnimal(request):
    if request.method == 'POST':
        animal_form = AnimalForm(request.POST)
        if animal_form.is_valid():
            animal_form.save()
            return redirect('petworld:index')
    else:
        animal_form = AnimalForm()
    return render(request,'producto/crear_animal.html',{'animal_form':animal_form})

# que nos permite listar los objetos de tipo Animal
def listarAnimal(request):
    animales = Animal.objects.all()
    return render(request,'producto/listar_animal.html',{'animales':animales})

# que nos permite editar un objeto del tipo Animal
def editarAnimal(request,id):
    animal_form = None
    error = None
    try:
        animal = Animal.objects.get(id = id)
        if request.method == 'GET': #preguntamos si se está trayendo la información para renderizarla y editarla. Si el metodo es Get entonces
            animal_form = AnimalForm(instance = animal) #formulario será llenado con la informacion del objeto encontrado
        else: #si no obtuvimos un GET, siginifica que procederemos a Guardar la información
            animal_form = AnimalForm(request.POST, instance = animal)
            if animal_form.is_valid(): # si es valido el formulario
                animal_form.save() # se guarda en la base de datos
            return redirect('petworld:index') # luego nos redirecciona al index
    except ObjectDoesNotExist as e:
        error = e
    return render(request,'producto/crear_animal.html',{'animal_form':animal_form, 'error':error})

def eliminarAnimal(request,id):
    animal = Animal.objects.get(id = id)
    if request.method == 'POST':
        animal.delete()
        return redirect('petworld:listar_animal')
    return render(request,'producto/eliminar_animal.html',{'animal':animal})
##############################################################

###################  CRUDS Productos ####################

# que nos permite crear un objeto del tipo Producto
class crearProducto(CreateView):
    model = Producto
    template_name = 'producto/crear_producto.html'
    form_class = ProductoForm

#que nos permite listar los objetos de tipo Producto.
class listarProductos(ListView):
    model = Producto
    template_name = 'producto/listar_productos.html'
    context_object_name = 'productos'
    queryset = Producto.objects.all()

class editarProducto(UpdateView):
    model = Producto
    template_name = 'producto/crear_producto.html'
    form_class = ProductoForm

class eliminarProducto(DeleteView):
    model = Producto
    template_name = 'producto/eliminar_producto.html'
    success_url = reverse_lazy('petworld:listar_productos')
