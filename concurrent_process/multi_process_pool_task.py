import random
from multiprocessing import current_process
class pool_worker():

    def __init__(self,*args,**kwargs):
        self.tid:int = kwargs['tid']
        self.tname:str = kwargs['tname']
        self.tval:int = kwargs['tval']
        self.tfac:int = kwargs['tfac']

    def mutate_item(self,new_val):
        mval = self.tval * self.tfac
        pval = mval*new_val
        result = {
            'tid': current_process().pid,
            'tname': self.tname,
            'org_val': self.tval,
            'mutated_val': mval,
            'processed_val': pval,
            'pname': current_process().name
        }
        return result

    def __call__(self, new_val):
        return self.mutate_item(new_val)

    @staticmethod
    def doName():
        current_process().name = f'Process-{random.randint(100,1000)}'
