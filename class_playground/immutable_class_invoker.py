from immutable_class import Closedblueprint
def doJob(x,y):
    obj = Closedblueprint(template=x,max_branches=y)
    print(repr(obj))
    print(obj.get_max_branches())
    print(obj.get_template())
    obj.set_template('dummy') #fail since class is immutable

if __name__ == '__main__':
    doJob('v1_draft',10)