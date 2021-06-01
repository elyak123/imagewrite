from django.db import models
from .storages import upload_to_image_1, OverwriteStorage, Image1Storage


class Newsletter(models.Model):
    def upload_to_image_2(self, filename):
        if self.pk:
            pk = self.pk
        else:
            instance = Newsletter.objects.all().order_by("-pk").first()
            if not instance:
                pk = 1
            else:
                pk = instance.pk + 1
        return f"newsletter/volume{pk}/volume{pk}-image-2.{filename.split('.')[-1]}"

    def upload_to_image_3(self, filename):
        if self.pk:
            pk = self.pk
        else:
            instance = Newsletter.objects.all().order_by("-pk").first()
            if not instance:
                pk = 1
            else:
                pk = instance.pk + 1
        return f"newsletter/volume{pk}/volume{pk}-image-3.{filename.split('.')[-1]}"

    def upload_to_image_4(self, filename):
        if self.pk:
            pk = self.pk
        else:
            instance = Newsletter.objects.all().order_by("-pk").first()
            if not instance:
                pk = 1
            else:
                pk = instance.pk + 1
        return f"newsletter/volume{pk}/volume{pk}-image-4.{filename.split('.')[-1]}"

    image_1 = models.ImageField(upload_to=upload_to_image_1, storage=Image1Storage)
    image_2 = models.ImageField(upload_to=upload_to_image_2, storage=OverwriteStorage(), null=True, blank=True)
    image_3 = models.ImageField(upload_to=upload_to_image_3, storage=OverwriteStorage(), null=True, blank=True)
    image_4 = models.ImageField(upload_to=upload_to_image_4, storage=OverwriteStorage(), null=True, blank=True)
