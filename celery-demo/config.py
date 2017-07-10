#!/usr/bin/python
#-*-coding:utf-8-*-

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'select_populate_book': {
    'task': 'favorite_book.select_populate_book',
    'schedule': timedelta(seconds=5),
    },
}
