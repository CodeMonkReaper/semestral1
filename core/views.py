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
