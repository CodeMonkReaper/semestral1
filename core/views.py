from django import http
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True) 
    if queryset:
        posts = Post.objects.filter(

        )
    return render(request, 'core/home.html', {'posts':posts})

def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')

def api(request):
    return render(request,'core/api.html')

def register(request):
    return render(request,'core/register.html')

def login(request):
    return render(request,'core/login.html')

def productos(request):
    #return render(request,'core/productos.html') 
    return HttpResponse ("Hola Pythonizando")

def comprar(request):
    return render(request,'core/comprar.html')

def creditodebito(request):
    return render(request,'core/creditodebito.html')