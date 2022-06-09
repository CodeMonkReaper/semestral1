from django.urls import path
from .views import home, quienes_somos


urlpatterns = [
    path('',home,name="home"),
    path ('quienes-somos/', quienes_somos, name='quienes_somos'),
]
