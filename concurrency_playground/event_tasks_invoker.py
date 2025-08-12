import random
import threading

from event_tasks import event_task
def doJob():
    event = threading.Event()
    event_obj = event_task(event=event)
    cthreads = [threading.Thread(target=event_obj.consume) for _ in range(10)]
    pthreads = [threading.Thread(target=event_obj.produce,args=(random.randint(100,6763),)) for idx in range(20)]

    for pthread in pthreads:
        pthread.start()
    for cthread in cthreads:
        cthread.start()


if __name__ == '__main__':
    doJob()

