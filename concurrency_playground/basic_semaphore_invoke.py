import threading
from basic_semaphore import doTask

def doJob():
    sem = threading.Semaphore(value=4)
    threads = [threading.Thread(name='T'+str(p),target=doTask,args=(sem,)) for p in range(10)]
    for t in threads:
        t.start()

if __name__ == '__main__':
    doJob()