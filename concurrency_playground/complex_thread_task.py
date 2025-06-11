import datetime
import time

import pytz


class task_exec:
    _instance = None
    @classmethod
    def doExec(cls):
        if cls._instance is None:
            cls._instance = list()
            cls._instance.append(datetime.datetime.now(pytz.UTC))
        else:
            pass
    def __init__(self):
        self.lock_obj = False

    def doTask(self,task_name):
        if not self.lock_obj:
          print(f'Thread {task_name} is executing')
          self.lock_obj = True
          time.sleep(15)
          print(f'Thread {task_name} has finished')
        else:
            pass

