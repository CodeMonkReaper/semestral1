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
from django.urls import path
from .views import home

urlpatterns = [
    path('',home,name="home"),
]
>>>>>>> luis-reescrito
