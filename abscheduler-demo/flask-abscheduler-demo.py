#!usr/bin/env python3
# -*- coding:utf-8 _*-


from flask import Flask
from flask_apscheduler import APScheduler


app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


@app.route('/')
def welcome():
    return 'Welcome to flask_apscheduler demo', 200


@app.route('/tasks')
def list_tasks():
    jobs = app.apscheduler.get_jobs()
    print(jobs)
    return 'Ok', 200


@app.route('/pause')
def pause():
    app.apscheduler.pause_job('job-1')
    return 'Ok', 200


@app.route('/resume')
def resume():
    app.apscheduler.resume_job('job-1')
    return 'Ok', 200


@app.route('/run-tasks')
def add_tasks():
    app.apscheduler.add_job(func=scheduled_task, trigger='cron', second='*/5', args=[1], id='job-' + str(1))
    app.apscheduler.add_job(func=scheduled_task, trigger='cron', second='*/10', args=[2], id='job-' + str(2))
    return 'Scheduled several long running tasks.', 200


def scheduled_task(task_id):
    print('Task {} running'.format(task_id))


app.run(host='0.0.0.0', port=5050)
