from celery import shared_task


@shared_task(bind=True)
def save_items(self, request, items):
    pass
