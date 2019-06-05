from main.celery import app
from ..models import (
    Links, Featured
)
from django.contrib.auth.models import User


def save_featured_link(data):
    link = Links.objects.get(video_id=data['video_id'])
    user = User.objects.get(id=data['user_id'])
    Featured.objects.create(
        link=link, user=user
    )


def remove_featured_link(data):
    link = Links.objects.get(video_id=data['video_id'])
    user = User.objects.get(id=data['user_id'])
    f = Featured.objects.get(link=link, user=user)
    f.delete()


@app.task
def featured_links(data, is_saving=True):
    """
    Two methods defined in this task because
    if it will be splitted, often will be errors like
    removing item, before it was saved.

    :param data:
    :param is_saving:
    :return:
    """
    if is_saving:
        save_featured_link(data)
    else:
        remove_featured_link(data)

    return "Completed!"
