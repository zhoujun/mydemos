#!usr/bin/env python3
# -*- coding:utf-8 _*-

from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    # 1、创建后台执行的 schedulers
    scheduler = BackgroundScheduler()
    # 2、添加调度任务，触发器选择 interval(间隔)，每隔3秒执行一次
    scheduler.add_job(tick, 'interval', seconds=3)
    # 3、启动调度任务
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()