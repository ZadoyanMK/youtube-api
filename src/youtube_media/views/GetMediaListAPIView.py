from rest_framework import generics, permissions
from rest_framework.response import Response
from ..serializers import *
from helpers import YoutubeAPIConnector


class GetMediaListAPIView(generics.GenericAPIView):

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LinkSerializer

    def post(self, request, *a, **kw):
        q = request.data.get('q', '')
        max_results = request.data.get('max_results', 25)
        page_token = request.data.get('page_token', None)
        region_code = request.data.get('region_code', None)
        q = q.replace(' ', '+')
        ctx = {
            'q': q,
            'max_results': max_results
        }
        if page_token:
            ctx['page_token'] = page_token
        if region_code:
            ctx['region_code'] = region_code

        media_list = YoutubeAPIConnector.send_request(**ctx)

        return Response({
            'q': q,
            'data': media_list
        })
