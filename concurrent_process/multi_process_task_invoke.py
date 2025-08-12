import multiprocessing
import random

from multi_process_task import process_task
from multiprocessing import Process , Manager
from typing import List

def doJob(id,name,lst):
    with Manager() as manager:
        llst:List[int]= manager.list()
        llst.extend(lst)
        llst.pop()
        c_obj = process_task(id=id,task_name=name,task_list=llst)
        processes = []
        for val in range(1,10):
            p = Process(name=f'Process-{val}',target=c_obj.add_tlist,args=(val,))
            processes.append(p)
        for p in processes:
            p.start()
        for p in processes:
            p.join()
        print(c_obj.tlist)
        print(c_obj.name)

if __name__ == '__main__':
    lst = [23,35,67]
    doJob(1,"mp_task",lst)

