"""
merge sort code
************
premise :
-> yet another divide and conquer strategy, but very different to shell sort in terms of philosophy
-> the intent is to recursively divide an unsorted list into sub-lists . this continues until we are left with sub-list of length 0 or 1
-> in general we start by divinding the list in half and start from there (i.e. divide further by half and so on)
-> once the divide phase is done, we start recursively merging the sub-lists and we merge them back in sorted order
-> the merging is unique and not comparable to insertion sort or so -- refer the code ofr further info
-> the merge continues until we end up with fully sorted list
complexity
time -> o(nlogn) as worst case complexity. this is better than shell , insertion and bubble or selection sorts
sort is not adaptive -> the process repeats even if we pass a sorted list
stable -> yes
space -> o(n) due to the process of creating multiple sub-lists
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Find the midpoint
    mid = len(arr) // 2

    # Recursively split the list into two halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left,right):
    merged = []
    i = j = 0

    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements from the left half
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Append any remaining elements from the right half
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged




def doJob():
    print(f'merge sorting an unsorted list')
    length = int(input('enter the number of elements in the length'))
    elements = input('enter the elements in unsorted list separated by a comma')
    vals = [int(x) for i,x in enumerate(elements.split(sep=',')) if i <10]
    res = merge_sort(vals)
    print(res)



if __name__ == '__main__':
    doJob()