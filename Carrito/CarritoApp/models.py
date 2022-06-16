from django.db import models

# Create your models here.

nombrec = models.models.CharField(max_length=64)
categoriac = models.models.CharField(max_length=32)
precioc = models.IntegerField()
def __str__(self):
    return f'{self.nombrec} -> {self.precioc}'