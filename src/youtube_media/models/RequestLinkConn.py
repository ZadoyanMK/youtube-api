from django.db import models
from .Links import Links
from .RequestData import RequestData


class RequestLinkConn(models.Model):
    link = models.ForeignKey(
        to=Links, on_delete=models.CASCADE
    )
    request_data = models.ForeignKey(
        to=RequestData, on_delete=models.CASCADE
    )
