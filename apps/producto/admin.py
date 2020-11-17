from django.contrib import admin
from .models import * # * es para importar Todo

class CategoriaAdmin(admin.ModelAdmin): # Personalizaremos la vista de modelos en el Admin de Django
    search_fields = ['nombre'] # Agrega una barra de busqueda para encontrar coincidencias con el atributo de la Clase
    list_display = ('nombre','estado',) # Especificamos los datos y filtros que aparecen en la lista de Administracion de Django

class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','stock','valor',)

admin.site.register(Animal)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)
