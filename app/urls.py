from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',signup),
    path('login/',user_login),
    path('logout/',user_logout),
    path('home/',home),
    path('balance/<int:pk>/',viewBalance),
    path('updateBalance/',updateBalance),
    path('activateWallet/',activateWallet),
    
]
