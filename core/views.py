from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')
    
def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')

def register(request):
    return render(request, 'core/register.html'),

def semillas(request):
    return render(request, 'core/semillas.html'),

def tierras(request):
    return render(request, 'core/tierras.html'),

def tijeras(request):
    return render(request, 'core/tijeras.html')