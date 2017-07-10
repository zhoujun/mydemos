import time
from celery import Celery

celery = Celery('tasks', broker='redis://127.0.0.1:6379/0')

@celery.task
def sendmail(mail):
    print('sending mail to %s...' % mail['to'])
    time.sleep(2.0)
    print('mail sent.')
