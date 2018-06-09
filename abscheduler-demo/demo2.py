#!usr/bin/env python3
# -*- coding:utf-8 _*-

from pytz import utc
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR


def tick():
    print('Tick! The time is: %s' % datetime.now())


# 选择MongoDB作为任务存储数据库
jobstores = {
    'mongo': MongoDBJobStore(),
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}

# 默认使用线程池
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}

# 默认参数配置
job_defaults = {
    'coalesce': False,  # 积攒的任务是否只跑一次，是否合并所有错过的Job
    'max_instances': 3,  # 默认同一时刻只能有一个实例运行，通过max_instances=3修改为3个。
    'misfire_grace_time': 30  # 30秒的任务超时容错
}


def my_listener(event):
    if event.exception:
        print('The job() crashed :('.format(event.job_id))  # or logger.fatal('The job crashed :(')
    else:
        print('The job() worked :)'.format(event.job_id))


scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
scheduler.add_job(tick, 'interval', seconds=3)
scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
scheduler.start()





