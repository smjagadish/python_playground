'''
this code snippet is a super simple code for area calculation
>>> triangle(3,4)
6.0
>>> rectangle(3,4)
12
>>> square(3)
9
>>> quadrilateral()
Traceback (most recent call last):
....
Exception: undefined shape
'''
def triangle (height , base):
    return 0.5 * height * base

def square (side):
    return side*side

def rectangle(length,breadth):
    return length * breadth

'''
intentional exception raising function
we leverage ellipsis to match only predictable content and catch random/dynamic data
'''
def quadrilateral():
    raise Exception("undefined shape")