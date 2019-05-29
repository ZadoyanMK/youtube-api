from rest_framework import serializers
from ..models import Thumbnails


class ThumbnailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnails
        fields = '__all__'
