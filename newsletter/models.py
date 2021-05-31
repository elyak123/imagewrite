from django.db import models
from .storages import upload_to, OverwriteStorage


class Newsletter(models.Model):
    pass


class Image(models.Model):
    news_letter = models.ForeignKey(Newsletter, default=None, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=upload_to, verbose_name="Image", storage=OverwriteStorage()
    )
