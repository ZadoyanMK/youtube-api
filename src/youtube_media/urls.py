from django.conf.urls import url
from .views import GetMediaListAPIView


urlpatterns = [
    url(r'^api/get-media/$', GetMediaListAPIView.as_view())
]
