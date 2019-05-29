from rest_framework import serializers
from ..models import Links


class LinkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Links
        fields = (
            'id', 'url', 'hash_url', 'published_at', 'title',
            'description', 'channel_title')
