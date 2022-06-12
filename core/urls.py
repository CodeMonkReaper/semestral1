from atexit import register
from django.urls import path
<<<<<<< HEAD
from .views import home, quienes_somos, register, semillas, tierras, tijeras
=======
from .views import home, productos, macetas, quienes_somos, guantes
urlpatterns = [
>>>>>>> pedro

    path('', home, name="home"),
    path('productos/', productos, name="productos"),
    path('quienes-somos/', quienes_somos, name="quienes_somos"),
    path('macetas/', macetas, name="macetas"), 
    path('guantes/',guantes,name="guantes")
    ]

<<<<<<< HEAD
urlpatterns = [
    path('',home,name="home"),
    path('quienes-somos/', quienes_somos, name='quienes_somos'),
    path('register/', register, name='register'),
    path('semillas/', semillas, name='semillas'),
    path('tierras/', tierras, name='tierras'),
    path('tijeras/', tijeras, name='tijeras')
]   
=======
>>>>>>> pedro
