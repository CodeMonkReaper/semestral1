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
    imagen = models.ImageField(upload_to='core/static/img/productos')
    categoria= models.ForeignKey(categoria, on_delete=models.CASCADE)
<<<<<<< HEAD
    nombrec = models.models.CharField(max_length=64)
    categoriac = models.models.CharField(max_length=32)
    precioc = models.IntegerField()
    def __str__(self):
        return f'{self.nombrec} -> {self.precioc}'      
=======
    def __str__(self):
        return self.nombre
>>>>>>> pedro
