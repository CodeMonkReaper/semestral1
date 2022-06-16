<<<<<<< HEAD
<<<<<<< HEAD
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
=======
from .views import api, comprar, creditodebito, home, productos, quienes_somos,register, login
api
=======
from .views import home, quienes_somos, api, register, login, productos, comprar, creditodebito, agregar_prod
>>>>>>> Luis
from django.urls import path
urlpatterns = [
    path('', home, name="home"),
>>>>>>> pedro
    path('quienes-somos/',quienes_somos, name="quienes_somos" ),
    path('register/',register,name="register"),
    path('login/',login,name="login"),
<<<<<<< HEAD
    path('ofertas/',ofertas,name="ofertas"),
>>>>>>> camilo
=======
    path('productos/', productos,name="productos"),
    path('api/',api, name="api"),
    path('comprar/',comprar, name="comprar"),
    path('creditodebito/',creditodebito, name="creditodebito"),
<<<<<<< HEAD
>>>>>>> pedro
=======
    path('agregarprod/',agregar_prod, name="agregarprod"),
>>>>>>> Luis
    ]

