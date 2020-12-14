from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse



##### Aquí se crean las Clases de la Base de Datos #####
class Animal(models.Model):
    id = models.AutoField(primary_key = True) # Clave primaria de la clase generada automáticamente
    nombre = models.CharField(max_length=10, blank = False, null = False)

    # De esta forma especificamos la forma en la que aparece el titulo en la Base de Datos
    class Meta:
        verbose_name = 'Animal' #Cuando se menciona en forma Singular
        verbose_name_plural = 'Animales' # Forma Plural
        ordering = ['nombre'] #se ordena por nombre

    # De esta forma se muestra el nombre del objeto en la lista de objetos creados
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del Producto', max_length = 50, blank = False, null = False)
    slug = models.CharField('Slug', max_length = 100, blank = False, null = False)
    descripcion = RichTextField('Descripcion', blank = False, null = False)
    peso = models.CharField('Peso', max_length = 10, blank = True, null = True)
    valor = models.IntegerField('Valor', blank = False, null = False)
    animal_id = models.ManyToManyField(Animal) #Relación Muchos a Muchos (pueden haber varios productos correspondientes a varios tipos de animales)
    imagen = models.ImageField('Imagen', blank = False, null = False)
    stock = models.BigIntegerField('Stock', blank = False, null = False)
    #falta añadir un campo de imagen

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre ##por defecto muestra el nombre

    def get_absolute_url(self):
        return reverse('petworld:listar_productos')

    def get_image_url(self):
        if self.imagen and hasattr(self.imagen, 'url'):
            return self.imagen.url
        else:
            return "/static/images/dog.jpg"
