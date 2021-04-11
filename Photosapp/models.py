from django.db import models

# Create your models here.


class fotoModel(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="Photosapp")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "fotoModel"
        verbose_name_plural = "fotoModel"

    def __str__(self):
        return self.title