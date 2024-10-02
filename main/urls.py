from django.urls import path
from django.contrib.auth.views import LogoutView
import main.views as main

app_name = "main"

urlpatterns = [
    path("", main.index, name="index"),
]