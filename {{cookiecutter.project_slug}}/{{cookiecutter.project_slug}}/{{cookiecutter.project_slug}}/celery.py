from celery import Celery
from {{ cookiecutter.project_slug }} import settings
from celery.schedules import crontab


app = Celery('itmo_choice')
app.config_from_object(settings, namespace='CELERY')
