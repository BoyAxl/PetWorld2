from django.contrib import admin
from .models import * # * es para importar Todo


class ProductoAdmin(admin.ModelAdmin):# Personalizaremos la vista de modelos en el Admin de Django
    search_fields = ['nombre'] # Agrega una barra de busqueda para encontrar coincidencias con el atributo de la Clase
    list_display = ('nombre','stock','valor',)# Especificamos los datos y filtros que aparecen en la lista de Administracion de Django

admin.site.register(Animal)
admin.site.register(Producto,ProductoAdmin)
