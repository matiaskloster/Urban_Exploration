from django.contrib import admin
from .models import fotoModel

# Register your models here.


class Photoappadmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(fotoModel, Photoappadmin)
