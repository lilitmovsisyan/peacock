from django.db import models
from django.utils import timezone

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length = 30)

    def __repr__(self):
            return self.name
    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='', null=True)
    name = models.CharField(max_length = 100, default="")
    entry = models.ForeignKey(
        'Entry', 
        on_delete=models.CASCADE,
        related_name='images',
        related_query_name='image'
    )


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




#For help, look up related objects, model fields, 

"""Consider editing path images are saved to using this django example:
For example:

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class MyModel(models.Model):
    upload = models.FileField(upload_to=user_directory_path)
"""