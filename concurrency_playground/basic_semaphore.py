import datetime
import py
import time

import pytz
import threading


def doTask(sem):
    s_time = datetime.datetime.now(pytz.UTC)
    with sem:
        time.sleep(5)
        # do nothing
    e_time = datetime.datetime.now(pytz.UTC)
    delta = e_time - s_time
    val = delta.total_seconds()
    print(f'total time taken for thread {threading.current_thread().name} is {val}')
