from django.db import models

class animal(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=10, blank = False, null = False)
