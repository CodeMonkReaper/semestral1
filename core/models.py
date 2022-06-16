from email.mime import image
from django.db import models

# Create your models here.
class categoria(models.Model):
    tipo= models.CharField(max_length=50)
    def __str__(self):
        return self.tipo

class producto(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.IntegerField()
    descripcion= models.TextField()
    categoria= models.ForeignKey(categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre