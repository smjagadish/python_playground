import multiprocessing
import random

from multi_process_pool_task import pool_worker
from multiprocessing import Process , Pool , current_process
def doJob():
    c_obj = pool_worker(tname='worker-1',tid=100,tval=1000,tfac=2)
    arg_list = [3,4,7,9]
    with multiprocessing.Pool(initializer=pool_worker.doName) as pool:
        results = pool.map(c_obj,arg_list) # blocks until all process execution is over
        print(results)
        print('process execution in synchronous mode is now complete')

def doAsyncJob():
    c_obj = pool_worker(tname='worker-2',tid=250,tval=500,tfac=3)
    arg_list = [4,8,2,7]
    with multiprocessing.Pool() as pool:
        results = pool.map_async(c_obj,arg_list) # non-blocking . async execution
        print('async execution of multi porcess, no blocking')

        print(results.get()) #blocks . results returns a list which is printed here or can be iterated over if needed

if __name__ == '__main__':
    doJob()
    doAsyncJob()