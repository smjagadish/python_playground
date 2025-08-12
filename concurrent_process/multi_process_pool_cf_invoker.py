import concurrent.futures
import multiprocessing
from concurrent.futures import as_completed

from multi_process_pool_cf_task import pool_cf_task,process_task
from multiprocessing import Pool , Manager , Process , current_process

def doJob():
    with multiprocessing.Manager() as manager:
        lock = manager.Lock()
        vals = input('enter the task list data separated by comma')
        slist = manager.list([int(v) for v in vals.split(',')])
        c_obj = pool_cf_task(tid=400,tname='task sorter',tdata=slist,lock=lock)
        with concurrent.futures.ProcessPoolExecutor(max_workers=4,initializer=pool_cf_task.doName) as executor:
            futures = [executor.submit(c_obj) for _ in range(len(slist))]

            #futures = executor.map(c_obj,range(len(slist)))

            #futures = [executor.submit(process_task(shared_list=slist,lock=lock)) for _ in range(len(vals))]



if __name__ == '__main__':
    doJob()

