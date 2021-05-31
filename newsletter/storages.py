from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os


def upload_to(instance, filename):
    dir_name = 'volume-'+str(instance.pk)
    filename = 'volume-'+str(instance.pk)+'-image_1'+filename[-4:]
    return '%s/%s' % (dir_name, filename)


remote_storage = FileSystemStorage(
                    location='/Users/tiffanybillard/Documents/dev/mediatest/',
                    base_url='/Users/tiffanybillard/Documents/dev/mediatest/'
                                )


class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_REMOTE, name))
        return name

