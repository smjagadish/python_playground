class Closedblueprint:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls) #will call init under the hood , but init does nothing as i just do a pass
        val1 = kwargs['template']
        val2 = kwargs['max_branches']
        object.__setattr__(instance,'template',val1) # this is how we do immutablility
        object.__setattr__(instance,'max_branches',val2)
        return instance

    def __init__(self,*args,**kwargs):
        pass

    def __setattr__(self, key, value):
        raise AttributeError(
            f"cannot change the parameter {key} to set the value {value}"
            f"the instance is immutable. create a new instance should changes be needed"

        )

    def __repr__(self):
        return (
            f"an immutable instance. use the getter to query the contents"

        )
    def get_template(self):
        return self.template

    # Getter for max_branches
    def get_max_branches(self):
        return self.max_branches

    def set_template(self,template): # this will fail
        self.template = template
