from multiprocessing import Process , current_process , Array , Value
from typing import List

def square(num:int,result,sum_of_squares:int,idx:int)->None:
    print(f'computing the square of {num} in process: {current_process().name} with id: {current_process().pid}')
    result[idx] = num*num
    with sum_of_squares.get_lock(): # lock is needed , else wont work
        sum_of_squares.value+= result[idx]

def doJob()-> None:
    num_list:List[int] = [2,3,4,5]
    result = Array("i",4)
    sum_of_squares = Value("i",0)
    for i,num in enumerate(num_list):
        p = Process(name=f'Process-{i}',target=square,args=(num,result,sum_of_squares,i))
        p.start()
        p.join()
    print(f' dumping the final array from main process: {[r for r in result]}')
    print(f' dumping the final sum from main process: {sum_of_squares.value}')

if __name__ == '__main__':
    doJob()
