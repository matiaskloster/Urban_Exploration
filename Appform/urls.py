from django.urls import path
from . import views


urlpatterns = [
    path("", views.vistaform, name="Form"),
]