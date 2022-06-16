from django.shortcuts import render, HttpResponse

# Create your views here.

def tienda(request):
    #return render(request,'core/tienda.html') 
    #return HttpResponse ("Hola Pythonizando")
    return render(request,'tienda.html') 

