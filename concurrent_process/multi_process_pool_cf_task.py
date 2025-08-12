import random
import time

from multiprocessing import current_process
from typing import List
from random import randint


def process_task(shared_list, lock):

    with lock:
      if shared_list:
        val = shared_list.pop()
        print(f"Process {current_process().pid} processed value: {val}")

class pool_cf_task():

    def __init__(self,*args,**kwargs):
        self._tid:int = kwargs['tid']
        self._tname:str = kwargs['tname']
        self._tdata:List[int] = kwargs['tdata']
        self._lock = kwargs['lock']

    @property
    def tid(self) -> int:
        return self._tid

    @tid.setter
    def tid(self,tid:int):
        self._tid = tid

    @property
    def tname(self)->str:
        return self._tname

    @tname.setter
    def tname(self,tname:str):
        self._tname = tname

    @property
    def tdata(self)->List[int]:
        return self._tdata

    @tdata.setter
    def tdata(self,tdata:List[int]):
        if len(self._tdata) == len(tdata):
            self._tdata = tdata
        else:
            pass

    @staticmethod
    def doName():
        current_process().name = f'Process-{random.randint(100,3456)}'

    def doJob(self):
        with self._lock:
            if self._tdata:
                val = self._tdata.pop()
                print(f'the process with id :{current_process().pid} and name: {current_process().name} has processed the data :{val}')
                print(f'process shall quit')
                time.sleep(3)

    def __call__(self, *args, **kwargs):
        self.doJob()


