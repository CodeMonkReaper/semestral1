from .views import home, productos, macetas, guantes, semillas, tierras, tijeras
from django.urls import path
[
    path('', home, name="home"),
    path('productos/', productos, name="productos"),
    path('macetas/', macetas, name="macetas"), 
    path('guantes/',guantes,name="guantes"),
    path('tierras/',tierras,name="tierras"),
    path('semillas/',semillas,name="semillas"),
    path('tijeras/',tijeras,name="tijeras"),

    ]

