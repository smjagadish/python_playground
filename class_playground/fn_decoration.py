def validate_checker(func):
    def check_data(*args):
        print(args)
        print('validator invoked')
        gen_data = (x for x in args if x >= 0)
        ''' use the below if you want to pass the args as a tuple without unpacking
        the below code will cause to loop through each tuple in the list of tuples 
        each retrieved tuple is then looped to get the elements.
        '''
        #gen_data = (x for sub_tpl in args for x in sub_tpl if x >=0)
        data = tuple(gen_data)
        if not data: # wont run unless all the inputs are 0 or less than 0
            print('exception')
            raise ValueError("invalid values for computation")
        else:
            for d in data:
                print(d)
            func(*args) # this is important - actual function invocation happens here
    return check_data

def second_checker(func):
    def check_data(*args):
        print('second validator invoked')
        for x in args:
            if x == 80:
                raise ValueError("value out of bounds")
            else:
                pass
    return check_data

@validate_checker # invokes the decorator that does data validation behind the scenes
def range_compute(*args):
    print(f'sum is: {sum(args)}')

@second_checker # invokes the second decorator. it will be after the validate_checker though
@validate_checker #invokes the decorator
def avg_compute(*args):
    count = sum(args)
    lt = len(args)
    print(f'avg is:{count/lt}')

if __name__ == '__main__':
    data_range = (1,2,3,4,5,80)
    try:

        range_compute(*data_range) # unpacking the tuple so that data is interpreted as tuple of ints in the function
        avg_compute(*data_range) #unpacking the tuple so that data is interpreted as tuple of ints in the function
    except ValueError as e:
        print(f'{e}')
    # decorators are actually as simple as below two lines
    fn = avg_compute # assign fn object
    (second_checker(avg_compute))(1,2,3,4) # invoke the decorator which returns actual fun. invoke that fn with the args.


