from django.urls import path
from django.conf import settings
from homeapp import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="Home"),
    path("books/", views.books, name="Books"),
    path("photos/", views.vistafoto, name="Photos"),
    path("view/<str:pk>/", views.view, name="View"),
    path("contact/", views.contact, name="Contact"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
