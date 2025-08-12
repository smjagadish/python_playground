from student import student
def doJob():
    object = student('john','wark',300)
    print(object.fname)
    print(object.lname)
    print(object.getfullName())
    print(object.gethike())

if __name__ == '__main__':
    doJob()