from django.db import models


class Links(models.Model):
    
    visit_count = models.IntegerField(default=0, db_index=True)
    url = models.CharField(max_length=512)
    hash_url = models.CharField(max_length=16, db_index=True)
    etag = models.CharField(max_length=256)
    published_at = models.DateTimeField(db_index=True)
    channel_id = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    description = models.TextField()
    channel_title = models.CharField(max_length=128)

    updated_at = models.DateTimeField(db_index=True, auto_now=True)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}'
