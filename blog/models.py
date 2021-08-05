from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """ 
    Models.Model shows, that Post is model of Django.

    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # link to another model
    title = models.CharField(max_length=200)    #text field with limited fields
    text = models.TextField()   # field for unlimited sized text
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title