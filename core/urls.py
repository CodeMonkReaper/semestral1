
from django.urls import path
from .views import home, api, guantes
urlpatterns = [
    path('',home,name="home"),
    path('api/',api,name="api"),
    path('guantes',guantes,name="guantes")
]
