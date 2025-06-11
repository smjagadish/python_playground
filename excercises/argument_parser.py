import argparse
def doOperation():
    args = argparse.ArgumentParser("a super simple script that will explore the usage of the args parse module in python")
    args.add_argument("--first","-f",type=str,required=True,help="The first argument to be passed to the script, must be a string"
                      ,default="def_val",action='store')
    args.add_argument("--second","-s",type=int,required=False,help="optional second arg , must be an int if used"
                      ,default=25,action='store')
    args.add_argument("--third","-th",type=str,required=False,help="optional third arg that can be specified multiple times, must be a string"
                      ,action='append')
    args.add_argument("--fourth","-fo",required=False,action='store_false',help="an optional boolean arg. if value not provided , false will be the default")

    arg_val = args.parse_args()
    print(f'the first arg value is:{arg_val.first}')
    print(f'the second arg value is :{arg_val.second}')
    print(f'the third arg value is:{arg_val.third}')
    print(f'the fourth arg value is:{arg_val.fourth}')


if __name__ == '__main__':
    doOperation()