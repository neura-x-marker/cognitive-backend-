from django.urls import path
from api.views import register, login

urlpatterns = [
    path('register/', register),
    path('login/', login),
]
