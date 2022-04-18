from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("tirth",views.tirth, name="tirth"),
    path("janki", views.janki, name="janki"),
    path("<str:name>", views.greet, name = "greet")
]