from django.urls import path
<<<<<<< HEAD
from .views import home, productos

urlpatterns = [
    path('', home, name="home"),
    path('productos/', productos, name="productos"),
=======
from .views import home, quienes_somos


urlpatterns = [
    path('',home,name="home"),
    path ('quienes-somos/', quienes_somos, name='quienes_somos'),
>>>>>>> camilo
]


