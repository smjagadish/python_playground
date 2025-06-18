import threading

from complex_thread_task import task_exec

def doTask():
    task_exec.doExec()
    my_obj = task_exec()
    t1 = threading.Thread(target=my_obj.doTask,args=('T1',))
    t2 = threading.Thread(target=my_obj.doTask,args=('T2',))
    t1.start()
    t2.start()

if __name__ == '__main__':
    doTask()