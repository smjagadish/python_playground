class stock:
    def __init__(self):
        self.__sym = ''
        self.__price = 0.0
        self.__category = ''

    @property
    def sym(self):
        return self.__sym
    @sym.setter
    def sym(self,sym):
        self.__sym = sym
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,price):
        self.__price = price
    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self,catgeory):
        self.__category = catgeory
    # override the repr method to print the object
    def __repr__(self):
        print(f'this object content is:{self.__sym} and {self.__category} with price={self.__price}')
