from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AnimalForm, ProductoForm
from .models import Animal, Producto

# Create your views here.
def home(request):
    productos = Producto.objects.all()
    return render(request,'index.html',{'productos':productos}) #funcion que renderiza, pinta un template con la información que deseamos

def acerca_de_nosotros(request):
    return render (request,'acerca_de_nosotros.html')

def productos(request):
    productos = Producto.objects.all()
    return render (request,'productos.html',{'productos':productos})

def productos_perro(request):
    productos = Producto.objects.filter(animal_id = Animal.objects.get(nombre = 'Perro'))
    return render (request,'productos.html',{'productos':productos})

def productos_gato(request):
    productos = Producto.objects.filter(animal_id = Animal.objects.get(nombre = 'Gato'))
    return render (request,'productos.html',{'productos':productos})
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
def crearProducto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, request.FILES)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('petworld:index')
    else:
        producto_form = ProductoForm()
    return render(request,'producto/crear_producto.html',{'producto_form':producto_form})
