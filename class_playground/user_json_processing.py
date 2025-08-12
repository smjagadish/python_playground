import json
from datetime import datetime, timedelta
from json import JSONDecodeError

import dateutil.parser
import pytz

from user_class import user
import ijson
from pathlib import Path

objs = list()
def createObject(json_dict):




    user_id = json_dict['user_id']
    email = json_dict['email']
    name = json_dict['name']
        #print(json_dict['name'])
    given_name = json_dict['given_name']
    family_name = json_dict['family_name']
    nickname = json_dict['nickname']
    last_ip = json_dict['last_ip']
    logins_count = json_dict['logins_count']
    created_at = dateutil.parser.isoparse(json_dict['created_at']) #strptime cant handle UTC expressed as Z
        #created_at = datetime.strptime(json_dict['created_at'],"%Y-%m-%dT%H:%M:%S.%f%z")
        #print(created_at)
    created_at = created_at.astimezone(pytz.UTC)
        #updated_at = datetime.strptime(json_dict['updated_at'],"%Y-%m-%dT%H:%M:%S.%f%z")
    updated_at = dateutil.parser.isoparse(json_dict['updated_at'])
    updated_at = updated_at.astimezone(pytz.UTC) + timedelta(hours=2)
        #last_login = datetime.strptime(json_dict['last_login'],"%Y-%m-%dT%H:%M:%S.%f%z")
    last_login = dateutil.parser.isoparse(json_dict['last_login'])
    last_login = last_login.astimezone(pytz.UTC)
    email_verified = json_dict['email_verified']
    obj = user()
    obj.populateData(id=user_id,email=email,name=name,family_name=family_name,given_name=given_name,ip=last_ip
                         ,login_count=logins_count,creation=created_at,updation=updated_at,verified=email_verified
                         ,last_login=last_login,nickname=nickname)
    #objs.append(obj)
        #print(obj.printRawData())
    #print(obj.printRawData())
    #objs.append(obj)
    return obj




def doProcessing(file_path):
    dir = Path(file_path)
    file = dir.joinpath('users.json')
    obj_ret = list()
    try:
        with open(file,mode='r',encoding='utf-8') as f:
            obj_ret= json.load(f,object_hook=createObject)
            for ob in obj_ret:
                print(ob.printRawData())
    except JSONDecodeError as e:
        print(f'the json decode errored out:{e}')

    except FileNotFoundError as fe:
        print(f'invalid file with error:{fe}')

    except Exception as ee:
        print(f'indeterminate error:{ee}')

if __name__ == '__main__':
    dirpath = 'C:\\Users\\esmjaga\\dir_for_python_stubs'
    doProcessing(dirpath)


