from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from.models import Producto



# Create your views here.
def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'core/home.html')

def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')

def api(request):
    return render(request,'core/api.html')

def register(request):
    return render(request,'core/register.html')

def login(request):
    return render(request,'core/login.html')

def productos(request):
    return render(request,'core/productos.html')

def carrito(request):
    return render(request,'core/carrito.html')

def creditodebito(request):
    return render(request,'core/creditodebito.html')

def agregarprod(request):
    return render(request,'core/agregarprod.html')