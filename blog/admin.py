from django.contrib import admin
from .models import Entry, Tag, Image

# Register your models here.
admin.site.register(Entry)
admin.site.register(Tag)
admin.site.register(Image)