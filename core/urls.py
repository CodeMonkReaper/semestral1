from .views import api, home, productos, quienes_somos,  register, login
from django.urls import path
urlpatterns = [
    path('', home, name="home"),
    path('productos/', productos, name="productos"), 
    path('api/',api,name="api"),
    path('api/',api,name="api"),
    ]

