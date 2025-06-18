import datetime
import threading

import pytz


def doTask(val):
    for i in range (0,val):
        print(threading.current_thread().name)
        print(datetime.datetime.now(pytz.UTC))