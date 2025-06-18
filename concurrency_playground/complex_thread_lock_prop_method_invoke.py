import threading

from complex_thread_lock_prop_method import complex_task

def doJob():
    my_obj = complex_task()
    t1 = threading.Thread(target=complex_task.set_val,args=(my_obj,45,),name='T1')
    t2 = threading.Thread(target=complex_task.set_val, args=(my_obj,55,),name='T2')
    t3 = threading.Thread(target=complex_task.set_val, args=(my_obj,65,),name='T3')
    t4 = threading.Thread(target=complex_task.set_val, args=(my_obj,75,),name='T4')

    t1.start()
    printdata(my_obj)
    t2.start()
    printdata(my_obj)
    t3.start()
    printdata(my_obj)
    t4.start()
    printdata(my_obj)
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()


def printdata(my_obj):
    print()
    print(my_obj.value)

if __name__ == '__main__':
    doJob()