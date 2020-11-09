from django.db import models

class animal(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=10, blank = False, null = False)

    # De esta forma especificamos la forma en la que aparece el titulo en la Base de Datos
    class Meta:
        verbose_name = 'animal'
        verbose_name_plural = 'animales'
        ordering = ['nombre']

    # De esta forma se muestra el nombre del objeto en la Base de Datos
    def __str__(self):
        return self.nombre