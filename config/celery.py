from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


# FIXME celery -A config worker --loglevel=info (run this command in terminal)
app = Celery("config")  # app = Celery('config', broker='redis://localhost:6379/0')


# Configure Celery using settings from Django settings.py.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load tasks from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# For terminal debugging
@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
