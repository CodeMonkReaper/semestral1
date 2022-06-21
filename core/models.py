from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.forms import ImageField

# Create your models here.
class categoria(models.Model):
    tipo= models.CharField(max_length=50)
    def str(self):
        return self.tipo

class producto(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.IntegerField()
    descripcion= models.TextField()
    categoria= models.ForeignKey(categoria, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to="productos", null=True)
    def str(self):
        return self.nombre