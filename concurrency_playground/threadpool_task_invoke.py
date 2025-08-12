import array
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures import as_completed

from threadpool_task import doTask
def doJob():
    with ThreadPoolExecutor(max_workers=10,thread_name_prefix="py_thread-") as executor:
        val = [executor.submit(doTask,i) for i in range(0,20)]
        #res = executor.map(doTask,[1,2,3])
        #print(res)
        for v in as_completed(val):
            print(v.result())

        executor.shutdown(cancel_futures=True)

if __name__ == '__main__':
    doJob()
