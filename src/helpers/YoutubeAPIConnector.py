import requests
from django.conf import settings


class YoutubeAPIConnector:

    _main_url = "https://content.googleapis.com/youtube/v3/search?"
    _headers = {
        'part': 'snippet',
        'key': settings.YOUTUBE_API_KEY,
        'q': '',
        'type': 'video',
        'maxResults': 25,
    }

    @classmethod
    def send_request(cls, q, max_results=25, page_token=None, region_code=None):
        headers = cls._headers
        if page_token:
            headers['pageToken'] = page_token
        if region_code:
            headers['regionCode'] = region_code
        headers['maxResults'] = max_results
        headers['q'] = q

        r = requests.get(url=cls._main_url, params=headers)

        return r.json()
