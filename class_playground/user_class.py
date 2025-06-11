from datetime import datetime


class user:
    def __init__(self):
        self.user_id =''
        self.email = ''
        self.name = ''
        self.given_name = ''
        self.family_name = ''
        self.nickname = ''
        self.last_ip = ''
        self.logins_count = 0
        self.created_at = None
        self.updated_at = None
        self.last_login = None
        self.email_verified = False

    def populateData(self,id,email,name,given_name,family_name,nickname,ip,login_count,creation,updation,last_login,verified):
        self.user_id = id
        self.email = email
        self.name = name
        self.given_name = given_name
        self.family_name = family_name
        self.nickname = nickname
        self.last_ip = ip
        self.logins_count = login_count
        self.created_at = creation
        self.updated_at = updation
        self.last_login = last_login
        self.email_verified = verified

    def printRawData(self):
        print(f'raw data:{self.__dict__}')

