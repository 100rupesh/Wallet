from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',signup),
    path('login/',user_login),
    path('logout/',user_logout),
    path('home/',home),
    path('get-user-balance/<int:pk>/',viewBalance),
    path('update-user-balance/',updateBalance),
    path('activate-user-wallet/',activateWallet),
    
]


