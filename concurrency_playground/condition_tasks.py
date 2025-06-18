import threading
import time
from typing import List
class condition_task:
    task_list : List[int] = list()
    def __init__(self,*args,**kwargs):
        self._condition = kwargs['condition']

    def produce(self,task_data):
        time.sleep(5)
        with self._condition:
            condition_task.task_list.append(task_data)
            self._condition.notify_all()

    def consume(self):
        with self._condition:
            time.sleep(2)
            self._condition.wait()
            if condition_task.task_list:
                print(f'consuming task with data {condition_task.task_list.pop()} by thread {threading.current_thread().name}')

