from concrete_class import concrete
def classActions():
    obj = concrete()
    obj.doWork() # concrete impl of abstract method in baseline
    obj.doComputeJob() # concrete impl of abstract method in baseline
    obj.instantiate() # specific method in the concrete class
    obj.callbaseline() # specific method in concrete class but calls upon the impl contained in baseline
    obj.defaultImp() # maybe python specific quirk ? i can call the abstract class non-abstract method directly using the concrete class object

if __name__ == '__main__':
    classActions()