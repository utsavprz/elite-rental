from django.urls.conf import include
from django.urls import path

from . import views

app_name='accounts'

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.loginPage, name="loginPage"),
    path("logout", views.loginPage, name="logout"),
    path("success", views.success, name="success")
]