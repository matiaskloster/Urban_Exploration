from django.shortcuts import render
from Photosapp.models import fotoModel


# Create your views here.


def vistafoto(request):
    resuqueryfotos = fotoModel.objects.all()
    return render(request, "Photosapp/photos.html", {"resuqueryfotos": resuqueryfotos})


def view(request, pk):
    resuqueryfoto = fotoModel.objects.get(id=pk)
    return render(request, "Photosapp/view.html", {"resuqueryfoto": resuqueryfoto})