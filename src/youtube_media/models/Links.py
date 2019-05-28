from django.db import models


class Links(models.Model):
    
    visit_count = models.IntegerField(default=0, db_index=True)
    url = models.CharField(max_length=512)
    hash_url = models.CharField(max_length=16, db_index=True)
