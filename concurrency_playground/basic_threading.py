import threading
import time

def doTask(name=""):
    print(f'starting thread with name: {name}')
    time.sleep(20)
    print(f' thread {name} finished execution')

if __name__ == '__main__':
    print('demonstrating threading example')
    t1 = threading.Thread(target=doTask, args=('T1',))
    t2 = threading.Thread(target=doTask, args=('T2',))
    t1.start()
    t2.start()