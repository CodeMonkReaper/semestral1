<<<<<<< HEAD
<<<<<<< HEAD
from .views import home,  quienes_somos, api, register, login, productos, comprar, creditodebito, agregarprod
=======
<<<<<<< HEAD
from .views import home,  quienes_somos, api, register, login, productos, comprar, creditodebito, agregarprod
from django.urls import path
urlpatterns = [
    path('', home, name="home"),
    path('quienes-somos/',quienes_somos, name="quienes_somos" ),
    path('register/',register,name="register"),
    path('login/',login,name="login"),
    path('productos/', productos,name="productos"),
    path('api/',api, name="api"),
    path('comprar/',comprar, name="comprar"),
    path('creditodebito/',creditodebito, name="creditodebito"),
    path('agregarprod/',agregarprod, name="agregarprod"),
    ]

=======
>>>>>>> nuevabranch
from django.urls import path
=======
from xml.etree.ElementInclude import include
from .views import home,  quienes_somos, api, register, login, productos, comprar, creditodebito, agregarprod
from django.urls import path, include
from django.contrib import admin 


>>>>>>> pedro
urlpatterns = [
    path('', home, name="home"),
    path('quienes-somos/',quienes_somos, name="quienes_somos" ),
    path('register/',register,name="register"),
    path('login/',login,name="login"),
    path('productos/', productos,name="productos"),
    path('api/',api, name="api"),
    path('comprar/',comprar, name="comprar"),
    path('creditodebito/',creditodebito, name="creditodebito"),
<<<<<<< HEAD
    path('productos/',productos, name="productos"),
]
>>>>>>> luis-reescrito
=======
    path('agregarprod/',agregarprod, name="agregarprod"),
    path('accounts/', include('django.contrib.auth.urls')), 
    ]

>>>>>>> pedro
