'''
selection sort code
premise
-> compare each element in unsorted array with rest of the elements that follow
-> the least element in this traversal is swapped with the element for which search was done
-> continue this until all elements in unsorted array have been taken up for searching
*******
properties
********

* time complexity - o(n^2)
* not a stable sort (i.e. wrt equal value elements)
* space complexity is o(1) as we update in place
* swaps is o(n) and comparison is o(n^2)

/// TODO
doJob logic can be super simplified to the below:
 for index in range(len(value)):
        min_idx = index
        for iindex in range(index + 1, len(value)):
            if value[iindex] < value[min_idx]:
                min_idx = iindex

        # Swap the found minimum element with the first element
        value[index], value[min_idx] = value[min_idx], value[index]

    print(f'The sorted data is: {value}')

'''
def doJob():
    length = int(input('enter the number of elements to sort'))
    vals = input('enter the elements in comma separated fashion')
    value = vals.split(sep=',')
    value = [int(elem) for idx,elem in enumerate(value) if idx <=length]
    print(f' the unsorted elements: {value}')
    print(f' starting in-place selection sort')

    for index,num in enumerate(value):
        lindex = index+1
        min_num = None
        min_idx = None
        for iindex,inum in enumerate(value[lindex:],lindex):
            if num > inum:
                if min_num is not None and min_num > inum:
                    min_num = inum
                    min_idx = iindex

                elif min_num is None:
                    min_num = inum
                    min_idx = iindex
                else:
                    pass
            else:
                if min_num is None:
                    if inum < num:
                        min_num = inum
                        min_idx = iindex
                    else:
                        pass
                elif inum < min_num:
                    min_num = inum
                    min_idx = iindex

        if min_num is not None:
            tmp = value[index]
            value[index] = min_num
            value[min_idx] = tmp
    print(f'the sorted data is :{value}')
if __name__ == '__main__':
    doJob()