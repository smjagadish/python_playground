"""
this code demonstrates binary search impl using python.
the code will first leverage quicksort to do the sorting and then feed the sorted list to binary search for the retrieval
the complexity is o(logn)
"""
def doquickSort(vals):
    left_arr = []
    right_arr = []
    if len(vals) <=1:
        return vals
    pivot = vals[-1]
    for elem in range(len(vals)-1):
        if vals[elem] < pivot:
            left_arr.append(vals[elem])
        else:
            right_arr.append(vals[elem])
    return doquickSort(left_arr) + [pivot] + doquickSort(right_arr)

def doSearch(elem,vals):
    if len(vals) == 1:
        if elem == vals[0]:
            print(f' the element:{elem} is present in the list')
        else:
            print(f' the element:{elem} is not present in the list')
        return
    mid = len(vals) // 2
    if elem == vals[mid]:
        print(f' the element:{elem} is present in the list')
        return
    if elem > vals[mid]:
        doSearch(elem,vals[mid+1:])
    else:
        doSearch(elem,vals[0:mid])

def doJob():
    print(f'demonstrating binary search in python')
    length = int(input('enter the number of elements in the list'))
    elements = input('enter the elements in the list separated by a comma')
    vals = [int(x) for i,x in enumerate(elements.split(sep=',')) if i<length]
    res = doquickSort(vals)
    print(f' will now search on the sorted dataset :{res}')
    elem = int(input('enter the number you wish to search'))
    doSearch(elem,res)

if __name__ == '__main__':
    doJob()