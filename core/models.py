from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=2800, null=True)
    url = models.CharField(max_length=2800, null=True)
    thumbnail = models.CharField(max_length=2800, null=True)
    def __str__(self):
        return self.title

    def __init__(self, title, url, thumbnail):
        super().__init__()
        self.title = title
        self.url = url
        self.thumbnail = thumbnail