from django.urls import path
from . import views

urlpatterns = [
    path("<str:name>", views.index, name="index"),
    path("view/", views.view, name="index"),
    path("create/", views.create, name="create"),
    path("", views.home, name="home")
]