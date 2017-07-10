#!/usr/bin/python
#-*-coding:utf-8-*-

from celery import Celery
import time

app = Celery('select_populate_book', broker="redis://127.0.0.1:6379/0")
app.config_from_object('config')

@app.task
def select_populate_book():
    print 'Start to select_populate_book task at {0}'.format(time.ctime())
    time.sleep(2)
    print 'Task select_populate_book succeed at {0}'.format(time.ctime())
    return True
