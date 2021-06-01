import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def upload_to_image_1(instance, filename):
    from .models import Newsletter
    if instance.pk:
        pk = instance.pk
    else:
        my_instance = Newsletter.objects.all().order_by("-pk").first()
        if not my_instance:
            pk = 1
        else:
            pk = my_instance.pk + 1
    return f"newsletter/volume{pk}/volume{pk}-image-1.{filename.split('.')[-1]}"


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=100):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class OverwriteStorageImage1(FileSystemStorage):
    def get_available_name(self, name, max_length=100):
        if self.exists(name):
            os.remove(os.path.join(settings.UPLOAD_ROOT, name))
        return name


Image1Storage = OverwriteStorageImage1(location=settings.UPLOAD_ROOT, base_url="/apache")
