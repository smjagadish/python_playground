import queue
def doJob():
    print(f' demonstrating a queue using the native python DS')
    num_queue = queue.Queue(maxsize=10)
    for i in range(10):
        num_queue.put(1,block=True,timeout=20)
    cons = num_queue.get(block=True,timeout=20)
    print(f'the queue maxsize is :{num_queue.maxsize}')
    print(f' the queue current size is :{num_queue.qsize()}')

if __name__ == '__main__':
    doJob()