from .views import home, productos, macetas, guantes, semillas, tierras, tijeras, quienes_somos, portamangueras, mangueras, palas
from django.urls import path
urlpatterns = [
    path('', home, name="home"),
    path('productos/', productos, name="productos"),
    path('macetas/', macetas, name="macetas"), 
    path('quienes-somos/',quienes_somos, name="quienes_somos" ),
    path('guantes/',guantes,name="guantes"),
    path('tierras/',tierras,name="tierras"),
    path('semillas/',semillas,name="semillas"),
    path('tijeras/',tijeras,name="tijeras"),
    path('portamangueras/',portamangueras,name="portamangueras"),
    path('mangueras/',mangueras,name="mangueras"),
    path('palas/',palas,name="palas"),

    ]

