from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Formmode
from .forms import Formulario
from .forms import forms
from django.contrib import messages

# Create your views here.


def vistaform(request):
    if request.method == "POST":
        form = Formulario(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            newform = Formmode(name=name, email=email, message=message)
            newform.save()
            messages.success(request, "Thank you!!")
            return redirect("/form")

    else:
        form = Formulario()
    return render(request, "Appform/contact.html", {"form": form})
