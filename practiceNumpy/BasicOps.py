import math

import numpy as np
from numpy.ma.core import shape

"""
basic operations with the numpy module in python
these are just scratching the surface. more examples will be added as i learn
"""
def doJob():
    arr = np.array(1) # scalar , so this stmtm will return a 0-d array
    print(arr)
    lst = [1,2,3]
    print(np.expand_dims(arr,0)) # convert scalar to 1-d array
    print(arr.reshape(-1)) # also a way to convert scalar to 1-d array
    print(arr[np.newaxis]) # also a wayto convert scalar to 1-d array
    lst_arr = np.array(lst)
    print(f' first array from list:{lst_arr}')
    sec_lst = [10,11,12]
    sec_lst_arr = np.array(sec_lst)
    print(f'second array from list:{sec_lst_arr}')
    res_arr = lst_arr + sec_lst_arr  # this is an example of vectorization. the array elements of 1st and 2nd array are added
    print(res_arr)
    combined_arr = np.concatenate((lst_arr,sec_lst_arr))
    print(f' an array concatenated using first and second array is :{combined_arr}')
    res_arr[0] = 41 # mutation allowed just as with lists . access is possible using indices
    print(f' demonstrating the printing using slicing:{res_arr[1:]}') # same as with lists , use slicing to extract parts of the original DS
    third_lst = [20]
    third_arr = np.array(third_lst)
    print(res_arr+third_arr)


def doMoreJob():
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])  # a 2-d array
    print(f' printing the 2-d array:{a}')
    print(f' printing the dimension of the array:{a.ndim} ')
    print(f' printing the row and column count of the 2-d array:{a.shape}')
    print(f' now retrieving the 2nd element in 2nd row of the 2-d array:{a[1,1]}')
    print(f' the total number of elements in the 2-d array is: {a.size}')
    b = np.array([   # a 3-d array with 2 2-d array with the 2-d array containing 2 rows and 4 columns
        [
            [11,12,13,14],
            [31,32,33,34]
        ],
        [
            [21,22,23,24],
            [41,42,43,44]
        ]

    ])
    print (f' the dimension of b-array is:{b.ndim}')

def doFillers():
    arr = np.zeros(4,dtype=np.int64) # an array with 0's
    print(f' an array populated using the zeros function:{arr}')
    another_arr = np.ones((2,2),dtype=np.int64) # a 2-d array with all elements set to 1
    print(f' a 2-d array filled with 1\'s:{another_arr}')
    empty_arr = np.empty((1,1),dtype=np.int64) # a 2-d array with either 0 or random data
    print(f' a 2-d array constructed using the empty constructs:{empty_arr}')
    arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
    print(f' the sorted equivalent of the array:{arr} is {np.sort(arr)}')
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6]])
    print('concatenating array along axis-0')
    print(np.concatenate((x, y), axis=0)) # this statement combines the 2-d array in x and y on the row axis
    #print(np.concatenate((x,y),axis=1)) # this statement will fail because the combining is on column axis and y array isn't same shape
    y = np.array([[5,6],[7,8]])
    print('concatenating array along axis-1')
    print(np.concatenate((x, y), axis=1))  # this statement combines the 2-d array in x and y on the column axis
    arr1 = np.array([[1,1],
                    [2,2]])
    arr2 = np.array([[3,3],
                     [4,4]])
    print('concatenating array using vstack, which is same as concat with axis=0')
    print(np.vstack((arr1,arr2)))   #vstack is similar to concatenation along vertical (i.e. axis=0)

    print('concatenating array using hstack, which is same as concat with axis=1')
    print(np.hstack((arr1,arr2)))

    new_arr = np.hstack((arr1,arr2))



if __name__ == '__main__':
    doJob()
    doMoreJob()
    doFillers()