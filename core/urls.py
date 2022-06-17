from .views import home, quienes_somos, api, register, login, comprar, creditodebito
from django.urls import path
urlpatterns = [
    path('', home, name="home"),
    path('quienes-somos/',quienes_somos, name="quienes_somos" ),
    path('register/',register,name="register"),
    path('login/',login,name="login"),
    path('api/',api, name="api"),
    path('comprar/',comprar, name="comprar"),
    path('creditodebito/',creditodebito, name="creditodebito"),
    
    ]