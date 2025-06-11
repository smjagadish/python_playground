"""
insertion sort code
premise
*******
-> the basic premise is to go through the list of elements in the array and compare an element with its neighbor
-> if the neighbor is less than the element , then swap the element with the neighbor. only if that is true, do next 2 steps else do nothing and take next iteration
-> after the swap , also compare the swapped element in prev step with the previous element(s) traversed earlier  and do the swap if lesser
-> above action must continue progressively as we go backwards through all the traversed elements

properties
****
time complexity -> o(n^2)
stable sort - ordering guarantees is ensured
space complexity -> o(1)
swaps is o(n^2) and comparison is o(n^2) - but can be improvised

"""

def doJob():
    print(f'insertion sorting algorithm')
    length = int(input('enter the number of elements to sort'))
    elements = input('enter the elements to be sorted separated by comma')
    vals = [int(x) for x in elements.split(sep=',')]

    for elem in range(length-1):
            if vals[elem] > vals[elem+1]:
                vals[elem],vals[elem+1] = vals[elem+1] , vals[elem]
                for inner_elem in range(elem,0,-1):
                        if vals[inner_elem] < vals[inner_elem-1]:
                            vals[inner_elem],vals[inner_elem-1] = vals[inner_elem-1],vals[inner_elem]
                            inner_swap = True
                        else:
                            break
    print(f'the sorted array is {vals}')



if __name__ == '__main__':
    doJob()