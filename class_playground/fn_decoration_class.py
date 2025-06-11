def doDecoration(func):
    def beautify(*args):
        # *args is a tuple with args[0] being the object on which method is called
        if len(args) == 2:
            val = args[1]
            if val == 'detailed':
                print(f'the instance method is getting decorated')
                func(*args)
            else:
                func(*args)
        else:
            print(args)
            raise Exception
    return beautify

def doSimpleDecoration(func):
    def simpledecor():
        print(f'a simple decoration')
        return func() # use the return if the original function will return a result
    return simpledecor

class fn_decorator:
    def __init__(self):
        self.markerData = 1
        self.subRegion = 'East'
        self.isValid = False

    def getData(self):
        print(f'the properties of the instance are:')
        print(f'markerData:{self.markerData}, subRegion:{self.subRegion} and validity:{self.isValid}')

    @doDecoration
    def getDecoratedData(self,style):
        print(f'the properties of the instance are:')
        print(f'markerData:{self.markerData}, subRegion:{self.subRegion} and validity:{self.isValid}')

    @property
    def getSecondDecoration(self):
        @doSimpleDecoration
        def printmethod():
            print(f'second decoration has been called')
        return printmethod

if __name__ == '__main__':
    obj = fn_decorator()
    obj.getData()
    obj.getDecoratedData('detailed')
    obj.getSecondDecoration()