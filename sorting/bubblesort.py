"""
bubble sorting code
premise
****
-> the basic premise is to iterate over the list of elements that need sorting 2 elements at a time
-> compare the element and its next neighbor and swap the element if it is larger than the neighbor
-> this continues until the elements are all sorted
-> each iteration of the sorting will have the length of the array to check reduced by 1

properties
*****
time complexity is o(n^2)
the sort is stable - position/ordering at insert time is retained
space complexity - o(1)
swaps is o(n^2) and comparison is o(n^2) - but can be improvised
"""


def doJob():
    print(f'bubble sorting algorithm')
    length = int(input ('enter the number of elements to sort'))
    elements = input('enter the elements to be sorted separated by comma')
    vals = [int(x) for x in elements.split(sep=',')]
    swap = True
    a = 0
    while swap is True:
        swap = False # break the loop if no swap would take place
        for elem in range((length-1)-a):
          if vals[elem] > vals[elem+1]:
              vals[elem],vals[elem+1] = vals[elem+1],vals[elem] # tuple unpacking syntax. avoid unnecessary tmp var
              swap = True
        a +=1
    print(f'sorted array is {vals}')


if __name__ == '__main__':
    doJob()