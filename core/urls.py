from django.urls import path
from .views import home, productos, macetas, quienes_somos, guantes
urlpatterns = [

    path('', home, name="home"),
    path('productos/', productos, name="productos"),
    path('quienes-somos/', quienes_somos, name='quienes_somos'),
    path("macetas/", macetas, name="macetas"), 
    path('guantes',guantes,name="guantes")
    ]

