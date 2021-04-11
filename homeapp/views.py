from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, "homeapp/home.html")


def books(request):
    return render(request, "homeapp/books.html")


def contact(request):
    return render(request, "homeapp/contact.html")
