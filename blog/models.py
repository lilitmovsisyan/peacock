from django.db import models
from django.utils import timezone

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length = 30)
    
    def __repr__(self):
            return self.name
    def __str__(self):
        return self.name

class Entry(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    date_published = models.DateTimeField(default=timezone.now) #need to import django.utils.timezone and use timezone.now WITHOUT brackets after now().
    text = models.TextField(default="")
    #attachments = 
    tags = models.ManyToManyField(Tag)

    def __repr__(self):
        return self.title
    def __str__(self):
        return self.title



