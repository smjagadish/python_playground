from getter_setter_ex import stock

def doJob(sym,price,category):
    obj = stock()
    obj.sym = sym
    obj.price = price
    obj.category = category
    return obj

def getinfo(obj):
    print(f'the stock symbol:{obj.sym}')
    print(f'the stock price:{obj.price}')
    print(f'the category:{obj.category}')

if __name__ == '__main__':
    sym = input('enter stock symbol')
    price = input('enter stock price')
    category = input('enter the stock category')
    obj = doJob(sym.strip(),float(price.strip()),category.strip())
    print(f'added entry with details below')
    getinfo(obj)
    obj.__repr__()

