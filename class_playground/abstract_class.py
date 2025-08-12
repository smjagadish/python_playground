from abc import ABC , abstractmethod
class baseline(ABC):
    @abstractmethod
    def doWork(self):
        pass
    @abstractmethod
    def doComputeJob(self):
        pass
    def defaultImp(self):
        print(f'this snippet is a default implementation. swap with a concrete use later')