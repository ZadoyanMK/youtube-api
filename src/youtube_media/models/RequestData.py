from django.db import models


class RequestData(models.Model):
    
    click_count = models.IntegerField(db_index=True, default=0)
    data = models.CharField(max_length=512)
    hash_data = models.CharField(max_field=16, db_index=True)
