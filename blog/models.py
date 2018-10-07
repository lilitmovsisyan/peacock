from django.db import models

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length = 200)
    #author = 
    date_published = models.DateTimeField
    text = models.TextField
    #attachments = 
    #tags = 