import threading
import time


class event_task:
    task_list = list()

    def __init__(self,*args,**kwargs):
        self._event = kwargs['event']

    def produce(self,task_data):
        time.sleep(5)
        #if not self._event.is_set():
        event_task.task_list.append(task_data)
        self._event.set()

    def consume(self):

        if not self._event.is_set():
            self._event.wait()
        while self._event.is_set():
            time.sleep(2)
            if event_task.task_list:
              print(f'consuming task with data {event_task.task_list.pop()} by thread {threading.current_thread().native_id}')
            self._event.clear()



