import time
from multiprocessing import Process , current_process
from typing import  List
def square(num:int)-> None:
    print(f'computing square of : {num}')
    print(f'the process id for computation is : {current_process().pid}')
    print(f'the process name is : {current_process().name} ')
    print(f'the result is {num*num}')

def doJob():
    num_list:List[int] = [1,2,3,4]
    st = time.time()
    for i,num in enumerate(num_list):
        p = Process(name=f'(process-{i})',target=square,args=(num,))
        p.start()

    et = time.time()
    print(f'total execution time is: {et-st}')


if __name__ == '__main__':
    doJob()
