"""
shell sort code
*****
premise :
-> shell sort is an optimization/improvisation on top of insertion sort. i.e. its a dive and conquer strategy
-> the idea is to split the unsorted list into sub-lists and subject insertion sort for each of those sub-lists
-> the break-down of the unsorted lists into sub-lists happens using what is called as gap-seq
-> for instance, if the length of list is 10, we could first have a sub-list that considers every 2nd element and sort it. then another sub-list that considers every 3rd elenment and sort it.
-> this continues until we are ended up with a list that is nearly sorted and do insertion sort with every element being considered
-> no rule of thumb for gap seq. one option is to use knuth's seq which splits usb-lists into (3^k-1)/2 with k starting from 1. the resultant values as long as not greater than n are considered with n being length of list
a list of length ( n = 100 ). You would calculate gaps as follows:

( k = 1 ), gap = ((3^1 - 1) / 2 = 1)
( k = 2 ), gap = ((3^2 - 1) / 2 = 4)
( k = 3 ), gap = ((3^3 - 1) / 2 = 13)
( k = 4 ), gap = ((3^4 - 1) / 2 = 40)
*********
complexity
space complexity - o(1)
time complexity - anywhere between o(n) and o(n^2)
stable and adaptive
"""
def doSort(vals,gap):
    print(f' processing sub-list with gap seq:{gap}')
    for elem in range(gap,len(vals),gap):
        if elem+gap > len(vals)-1:
            break
        if vals[elem] > vals[elem+gap]:
            vals[elem],vals[elem+gap] = vals[elem+gap],vals[elem]
        for inner_elem in range(elem,0,-gap):
            if inner_elem - gap < 0:
                break
            else:
                if vals[inner_elem] < vals[inner_elem-gap]:
                    vals[inner_elem],vals[inner_elem-gap] = vals[inner_elem-gap],vals[inner_elem]
                else:
                    break

    print(vals)
def doJob():
    print(f'shell sorting a user provided data set')
    length = int(input('enter the number of elements in the data set'))
    elements = input('enter the elements in a comma separated format')
    vals = [int(x) for i,x in enumerate(elements.split(sep=',')) if i <10]
    gaps =list()
    for k in range(1,length):
        gap = (pow(3,k)-1)//2
        if gap > length:
            break
        else:
            gaps.append(gap)
    gaps.sort(reverse=True)
    for seq in gaps:
        doSort(vals,seq)
    print(f' the sorted list is :{vals}')
if __name__ == '__main__':
    doJob()