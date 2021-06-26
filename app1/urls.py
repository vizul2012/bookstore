from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.Registerpage,name="regration"),
    path("login",views.Loginpage,name="Loginpage"),
    path("reg-user",views.Registeruser,name="regsteruser"),
    path("log-user",views.Loginuser,name="loguser")
]
