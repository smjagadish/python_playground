from abstract_class import baseline
class concrete(baseline):
    def doWork(self):
        print(f'the concrete impl for doWork')
    def doComputeJob(self):
        print(f'the concrete impl for doComputeJob')
    def instantiate(self):
        print(f' this invocation is unique to the concrete class')
    def callbaseline(self):
        super().defaultImp()
    