from django.urls import path
from django.contrib.auth.models import User
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('logout/',userlogout,name='logout'),
    path('login/',userlogin,name="login"),
    path('register/',register,name='register'),
    path('profile/',profile,name='profile'),
    path('changeinfo/',changeinfo,name='changeinfo'),
    path('passwordreset/',passwordreset,name='passwordreset'),
]
