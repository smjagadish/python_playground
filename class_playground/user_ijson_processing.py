from json import JSONDecodeError

import ijson
from user_class import user
from pathlib import  Path
def process_with_ijson(path):
    file_path = Path(path).joinpath('users.json')
    try:
        with open(file_path,mode='r',encoding='utf-8') as f:
            for user in ijson.items(f,'item'): # item is a specific keyword that is used when we are fetching arrays
                # since the json file being loaded is an array of user objects, i use the 'item' to get the array and traverse over each user object
                print(user)
                # fetching individual attr is same as getting the data from the dict
                email = user.get('email','no_email')
                print(email)
    except FileNotFoundError as fe:
        print(f' the file is invalid:{fe}')
    except JSONDecodeError as je:
        print(f'error in decoding json:{je}')

def process_full_file_with_ijson(path):
    file_path = Path(path).joinpath('users.json')
    try:
        with open(file_path,mode='r',encoding='utf-8') as f:
            for prefix,event,value in ijson.parse(f):
                if prefix == 'item.user_id' and event == 'string': # i'm reading an arry of dicts which has user_id as one of its prop , so use item.key
                    print (f'user name is :{value}')
                else:
                    continue
    except Exception as e:
        print(f'errored out with:{e}')

if __name__ == '__main__':
    dirpath = 'C:\\Users\\esmjaga\\dir_for_python_stubs'
    process_with_ijson(dirpath)
    process_full_file_with_ijson(dirpath)


