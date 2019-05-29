from django.db import models
from .Links import Links


class Thumbnails(models.Model):

    link = models.ForeignKey(
        to=Links, on_delete=models.CASCADE
    )
    type = models.CharField(max_length=64)
    url = models.CharField(max_length=512)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.type}'
