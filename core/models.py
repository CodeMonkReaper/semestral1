<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> nuevabranch
from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.forms import ImageField

# Create your models here.
class categoria(models.Model):
    tipo= models.CharField(max_length=50)
    def __str__(self):
        return self.tipo

class producto(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.IntegerField()
    descripcion= models.TextField()
<<<<<<< HEAD
<<<<<<< HEAD
    imagen = models.ImageField(upload_to='core/static/img/productos')
    categoria= models.ForeignKey(categoria, on_delete=models.CASCADE)
=======
    categoria= models.ForeignKey(categoria, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to="productos", null=True)
    def __str__(self):
        return self.nombre
=======
from django.db import models

# Create your models here.
>>>>>>> luis-reescrito
>>>>>>> nuevabranch
=======
    categoria= models.ForeignKey(categoria, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to="productos", null=True)
    def __str__(self):
        return self.nombre
>>>>>>> pedro
