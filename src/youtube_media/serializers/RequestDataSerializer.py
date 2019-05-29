from rest_framework import serializers
from ..models import RequestData


class RequestDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RequestData
        fields = ('id', 'data', 'next_page', 'prev_page')
