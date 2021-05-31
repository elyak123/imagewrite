from django.contrib import admin
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Image, Newsletter


class ImagesInline(admin.TabularInline):
    model = Image
    extra = 0


@admin.register(Newsletter)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', )
    inlines = [
        ImagesInline
    ]


@receiver(post_delete, sender=Image)
def delete_images(sender, instance, using, **kwargs):
    instance.image.delete(save=False)
