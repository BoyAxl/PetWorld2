from django.shortcuts import render, redirect
from .forms import AnimalForm

# Create your views here.
def Home(request):
    return render(request,'index.html') #funcion que renderiza, pinta un template con la información que deseamos

def crearAnimal(request):
    if request.method == 'POST':
        animal_form = AnimalForm(request.POST)
        if animal_form.is_valid():
            animal_form.save()
            return redirect('index')
    else:
        animal_form = AnimalForm()
    return render(request,'producto/crear_animal.html',{'animal_form':animal_form})