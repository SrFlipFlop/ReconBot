#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crontab import CronTab #https://code.tutsplus.com/tutorials/managing-cron-jobs-using-python--cms-28231

def add_corn_task():
    cron = CronTab(user='user')
    job = cron.new(command='python /home/jay/writeDate.py')
    job.minute.every(1)
    cron.write()

def update_cron_task():
    pass

def remove_cron_task():
    pass