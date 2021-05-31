from django.db import models
from .storages import upload_to, remote_storage


class Newsletter(models.Model):

    image_1 = models.ImageField(upload_to=upload_to)
    image_2 = models.ImageField(upload_to=upload_to, storage=remote_storage, null=True, blank=True)
    image_3 = models.ImageField(upload_to=upload_to, storage=remote_storage, null=True, blank=True)
    image_4 = models.ImageField(upload_to=upload_to, storage=remote_storage, null=True, blank=True)

