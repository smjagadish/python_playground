class student:
    def __init__(self,fname='',lname='',*args,**kwargs):
        self._fname = fname
        self._lname = lname
        self._rate = args[0]

    @property
    def fname(self):
        return self._fname

    @fname.setter
    def fname(self,fname_upd):
        self._fname = fname_upd

    @property
    def lname(self):
        return self._lname

    @lname.setter
    def lname(self,lname_upd):
        self._lname = lname_upd

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self,rate_upd):
        self._rate = rate_upd

    def getfullName(self):
        return '{} {}'.format(self._fname,self._lname)

    def gethike(self):
        return int(self._rate)*2.5
