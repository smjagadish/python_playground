import array
from concurrent.futures.thread import ThreadPoolExecutor

from threadpool_task import doTask
def doJob():
    res = list()
    with ThreadPoolExecutor(max_workers=10,thread_name_prefix="py_thread-") as executor:
        for i in range(0,20):
            res = executor.submit(doTask,i)
        executor.shutdown(cancel_futures=True)

if __name__ == '__main__':
    doJob()
