<<<<<<< HEAD
from unicodedata import name
from django.urls import path
from .views import home, productos, macetas, quienes_somos, guantes,api
=======
from .views import home, productos, macetas, guantes, semillas, tierras, tijeras, quienes_somos, portamangueras, mangueras, palas, register, login,ofertas
from django.urls import path
>>>>>>> camilo
urlpatterns = [
    path('', home, name="home"),
    path('productos/', productos, name="productos"),
    path('macetas/', macetas, name="macetas"), 
<<<<<<< HEAD
    path('guantes/',guantes,name="guantes"),
    path('api/',api,name="api"),
=======
    path('quienes-somos/',quienes_somos, name="quienes_somos" ),
    path('guantes/',guantes,name="guantes"),
    path('tierras/',tierras,name="tierras"),
    path('semillas/',semillas,name="semillas"),
    path('tijeras/',tijeras,name="tijeras"),
    path('portamangueras/',portamangueras,name="portamangueras"),
    path('mangueras/',mangueras,name="mangueras"),
    path('palas/',palas,name="palas"),
    path('register/',register,name="register"),
    path('login/',login,name="login"),
    path('ofertas/',ofertas,name="ofertas"),
>>>>>>> camilo
    ]

