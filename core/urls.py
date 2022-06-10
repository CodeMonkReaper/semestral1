from atexit import register
from django.urls import path
from .views import home, quienes_somos, register, semillas, tierras, tijeras


urlpatterns = [
    path('',home,name="home"),
    path('quienes-somos/', quienes_somos, name='quienes_somos'),
    path('register/', register, name='register'),
    path('semillas/', semillas, name='semillas'),
    path('tierras/', tierras, name='tierras'),
    path('tijeras/', tijeras, name='tijeras')
]   
