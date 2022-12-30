from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("home",views.index, name="home"),
    path("car", views.cars,name="cars"),
    path("login", views.login, name="login"),
    path("contact", views.contactUs, name="contact"),
    path("signup",views.signUp,name="signup"),
]