import random
import threading

from condition_tasks import condition_task
def doJob():
    condition = threading.Condition()
    c_obj = condition_task(condition=condition)
    p_threads = [threading.Thread(name=f'Thread-{i}', target=c_obj.produce, args=(random.randint(100, 3560),)) for i in range(10)]
    c_threads = [threading.Thread(name=f'Thread-{i}',target=c_obj.consume) for i in range(10)]

    for thread in p_threads:
        thread.start()

    for thread in c_threads:
        thread.start()

if __name__ == '__main__':
    doJob()
