import random
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

import pytz


class TroubleTicket:
    ticket_prio = ['a','b','c']
    def __init__(self):
        self.__id = 0
        self.__priority = ''
        self.__impactedProducts = []
        self.__isBlocker = False
        self.__creationDate = None
        self.__resolutionDate = None

    def setId(self):
        self.__id= random.randint(1000,10000)

    def getId(self):
        return self.__id

    def setPriority(self,prio):
        if prio not in TroubleTicket.ticket_prio:
            self.__priority = 'c'
        else:
            self.__priority = prio

    def getPriority(self):
        return self.__priority

    def setImpactedProducts(self,prod_list):
        if isinstance(prod_list,list):
            self.__impactedProducts.extend(prod_list)
        else:
            self.__impactedProducts.extend(list(prod_list))

    def getImpactedProducts(self):
        return self.__impactedProducts

    def setBlocker(self,isBlocker):
        self.__isBlocker = isBlocker

    def getBlocker(self):
        return self.__isBlocker

    def setCreationDate(self):
        self.__creationDate = datetime.now(timezone.utc)

    def getCreationDate(self):
        return self.__creationDate.astimezone(pytz.timezone('America/Toronto'))



    def setResolutionDate(self):
        if self.__priority == 'a' :
            self.__resolutionDate = self.__creationDate + timedelta(days=5)
        elif self.__priority == 'b' :
            self.__resolutionDate = self.__creationDate + timedelta(days=10)
        else :
            self.__resolutionDate = self.__creationDate + timedelta(days=25)

    def getResolutionDate(self):
        return self.__resolutionDate.astimezone(pytz.timezone('America/Toronto'))

    def configureTroubleTicket(self,priority,impactedProducts,isBlocker):
        self.setCreationDate()
        self.setId()
        self.setPriority(priority)
        self.setImpactedProducts(impactedProducts)
        self.setBlocker(isBlocker)
        self.setResolutionDate()

    def persistID(self,ID):
        self.__id = ID

    def persistCreationDate(self,creation_date):
        self.__creationDate = creation_date

    def persistResolutionDate(self,resolution_date):
        self.__resolutionDate = resolution_date

    def deserializeTroubleTicket(self,priority,impactedProducts,isBlocker,creation_date,resolution_date,ID):
        self.setPriority(priority)
        self.setImpactedProducts(impactedProducts)
        self.setBlocker(isBlocker)
        self.persistID(ID)
        self.persistCreationDate(creation_date)
        self.persistResolutionDate(resolution_date)


    def printTroubleTicketInfo(self):
        print(f'printing Trouble ticket details:')
        print(f'ID:{self.getId()}')
        print(f'Priority:{self.getPriority()}')
        print(f'Blocker Status:{self.getBlocker()}')
        print(f'Impacted product list:{self.getImpactedProducts()}')
        print(f'Creation Date:{self.getCreationDate()}')
        print(f'Resolution Date:{self.getResolutionDate()}')

