from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'producto/index.html') #funcion que renderiza, pinta un template con la información que deseamos
