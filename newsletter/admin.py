from django.contrib import admin
from .models import Newsletter


@admin.register(Newsletter)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_1', 'image_2')


