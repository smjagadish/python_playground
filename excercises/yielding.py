import random


'''
super simple code to demonstrate yield. the yield keyword will lazily evaluate the contained expression
it returns an iterable which can be iterated over by the calling code
memory efficient as it doesn't 'store' the data being generated/produced 
'''
def yield_gen(bounds):
    count = 0
    while count < bounds:
        yield random.randrange(start=10,stop=25,step=1)
        count +=1

def static_yield():
    yield 1
    yield 2
    print('will yield further')
    yield 3
    print(' last yield')
    yield 4
def dict_yield():
    for i in range(1,10):
        key = 'k'+ str(i)
        yield key,i



if __name__ == '__main__':
    bounds = input('enter the bounds')
    bounds = int(bounds.strip())
    for i in yield_gen(bounds):
        print(f'yielding:{i}')
    val = (x+1 for x in static_yield())
    for tval in val:
        print(tval)

    vals = ((x,y) for x,y in dict_yield()) #dict_yield returns tuples
    print(dict(vals)) # construct a dict from the key value tuples

