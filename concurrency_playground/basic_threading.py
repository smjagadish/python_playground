import threading
import time

def doTask(name=""):
    print(f'starting thread with name: {name}')
    print(threading.current_thread())
    time.sleep(20)
    print(f' thread {name} finished execution')

if __name__ == '__main__':
    print('demonstrating threading example')

    t1 = threading.Thread(target=doTask, args=('T1',),name='T1')
    t2 = threading.Thread(target=doTask, args=('T2',),name='T2')
    t1.start()
    t1.join() # sequential execution
    t2.start() # not started until T1 completes
    t2.join()