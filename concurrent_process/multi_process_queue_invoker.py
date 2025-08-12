import random

from multi_process_queue import multi_task_queue
from multiprocessing import Process , current_process , Queue

if __name__ == '__main__':
    val = int(input('enter process count'))
    tqueue = Queue(maxsize=100)
    id = random.randint(10,234)
    cp_obj = multi_task_queue(id=id,region='RNAM',inventory=tqueue)
    processes = []
    for _ in range(val):
        vals = random.randint(1,10000)
        p1 = Process(name='Producer', target=cp_obj.add_element, args=(vals,))
        p2 = Process(name='Consumer',target=cp_obj.get_element)
        processes.extend([p1,p2])
    for p in processes:

        p.start()
    for p in processes:
        p.join()

    print(f'process execution over')
    print(cp_obj.inventory)