from django.forms import ModelForm
from django import forms
from .models import Formmode


class Formulario(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Formmode
        fields = ("name", "email", "message")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
        }

        error_messages = {
            "name": {
                "required": ("Required!"),
            },
            "email": {
                "required": ("Required!"),
            },
        }