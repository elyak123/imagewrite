import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def upload_to(instance, filename):
    return "newsletter/volume{0}/volume{0}-image-{1}".format(
        instance.news_letter.pk, filename
    )


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=100):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name
