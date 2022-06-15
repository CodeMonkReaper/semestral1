from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def productos(request):
    return render(request, 'core/productos.html')

def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')

def macetas(request):
    return render(request, 'core/macetas.html')

def api(request):
    return render(request,'core/api.html')
    
def guantes(request):
    return render(request,'core/guantes.html')

def tierras(request):
    return render(request,'core/tierras.html')

def tijeras(request):
    return render(request,'core/tijeras.html')

def semillas(request):
    return render(request,'core/semillas.html')

def portamangueras(request):
    return render(request,'core/portamangueras.html')

def mangueras(request):
    return render(request,'core/mangueras.html')

def palas(request):
    return render(request,'core/palas.html')

def register(request):
    return render(request,'core/register.html')

def login(request):
    return render(request,'core/login.html')

def ofertas(request):
    return render(request,'core/ofertas.html')