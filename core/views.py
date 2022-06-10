from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')
def api(request):
    return render(request,'core/api.html')
def guantes(request):
    return render(request,'core/guantes.html')
