"""
quicksort code
************
premise
-> yet another divide and conquer strategy that works with a pivot element. no special rule to choose the pivot, one option is to go with last elem
-> with the pivot, split the list into left and right with elements less than and greater than pivot
-> do the above recursively, choosing a pivot for the left and right arr at each stage. this continues until we are left with single element arrays
->combine the single element left arr , pivot and right arr
complexity
time -> o(nlongn) # this may become o(n^2) if the pivot is bad. although i use pviot as last elem, better alternatives are out there
space -> probably o(n) in my impl due to left/right arr. maybe there is in-place modifs which will be o(1)
stable -> no
adaptive -> no
"""

def doSort(vals):
    left_arr = []
    right_arr = []
    if len(vals) <=1:
        return vals
    pivot = vals[len(vals)-1]
    for elem in range(len(vals)-1):
        if vals[elem]< pivot:
            left_arr.append(vals[elem])
        else:
            right_arr.append(vals[elem])

    return doSort(left_arr) + [pivot] + doSort(right_arr)


def doJob():
    length = int(input('enter the number of elements in the list'))
    elements = input('enter the elements in the list separated by comma')
    vals = [int(x) for i,x in enumerate(elements.split(sep=',')) if i<length]
    res=doSort(vals)
    print(f'the sorted list is {res}')

if __name__ == '__main__':
    print(f'quick sorting algorithm')
    doJob()