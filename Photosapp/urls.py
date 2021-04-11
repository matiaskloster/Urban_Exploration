from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.vistafoto, name="Photos"),
    path("view/<str:pk>/", views.view, name="View"),
]
