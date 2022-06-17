from django.shortcuts import render

from core.models import producto

# Create your views here.
def home(request):
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
    productos= producto.objects.all()
    data = {
        'productos':productos
    }
    return render (request,'core/productos.html', data)

def comprar(request):
    return render(request,'core/comprar.html')

def creditodebito(request):
    return render(request,'core/creditodebito.html')

def agregarprod(request):
    return render(request,'core/agregarprod.html')



