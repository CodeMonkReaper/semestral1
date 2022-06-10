<<<<<<< HEAD
from django.urls import path
from .views import home, productos, macetas, quienes_somos
=======
>>>>>>> Luis

from django.urls import path
from .views import home, api, guantes
urlpatterns = [
<<<<<<< HEAD
    path('', home, name="home"),
    path('productos/', productos, name="productos"),
    path('quienes-somos/', quienes_somos, name='quienes_somos'),
    path("macetas/", macetas, name="macetas")
    ]
=======
    path('',home,name="home"),
    path('api/',api,name="api"),
    path('guantes',guantes,name="guantes")
]
>>>>>>> Luis
