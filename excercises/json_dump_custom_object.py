import json
from datetime import datetime

import pytz

from class_playground.private_class import TroubleTicket
def doDeserialization(json_dict):
    print(f'de-serializing the json payload to class object')
    obj1 = TroubleTicket()
    creation_date = datetime.strptime(json_dict['creation_date'],"%Y-%m-%d %H:%M:%S.%f%z")
    creation_date = creation_date.astimezone(pytz.UTC)
    resolution_date = datetime.strptime(json_dict['resolution_date'], "%Y-%m-%d %H:%M:%S.%f%z")
    resolution_date = resolution_date.astimezone(pytz.UTC)
    obj1.deserializeTroubleTicket(json_dict['priority'],json_dict['impacted_products']
                                 ,json_dict['blocker'],creation_date
                                 ,resolution_date,json_dict['ID'])
    return obj1

def printObjectInfo(obj):
    obj.printTroubleTicketInfo()

if __name__ == '__main__':
    dict_data = '''{"ID":4567,"priority": "A","blocker": true,"impacted_products":["enb","msrbs"]
                 ,"creation_date":"2025-03-08 14:23:23.459906-05:00",
                 "resolution_date":"2025-04-02 15:23:23.459906-04:00"}'''
    obj = json.loads(dict_data,object_hook=doDeserialization)


    printObjectInfo(obj)