from django.shortcuts import render
from Photosapp.models import fotoModel

# Create your views here.


def home(request):
    return render(request, "homeapp/home.html")


def books(request):
    return render(request, "homeapp/books.html")


def vistafoto(request):
    resuqueryfotos = fotoModel.objects.all()
    return render(request, "homeapp/photos.html", {"resuqueryfotos": resuqueryfotos})


def view(request, pk):
    resuqueryfoto = fotoModel.objects.get(id=pk)
    return render(request, "homeapp/view.html", {"resuqueryfoto": resuqueryfoto})


def contact(request):
    return render(request, "homeapp/contact.html")
