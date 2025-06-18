import datetime
import time
import typing
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

    def doTask(self,task_name) :
        if not self.lock_obj:
          print(f'Thread {task_name} is executing and class method created at {self._instance[0]}')
          self.lock_obj = True
          time.sleep(15)
          print(f'Thread {task_name} has finished')
        else:
            pass

