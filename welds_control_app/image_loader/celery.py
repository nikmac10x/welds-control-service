import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "image_uploader.settings")
app = Celery("image_uploader")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
