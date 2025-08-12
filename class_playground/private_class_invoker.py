from  private_class import  TroubleTicket
def doWork():
    instance = TroubleTicket()
    priority = input('Enter the Trouble ticket priority - must be one of \'a\' or \'b\' or \'c\'')
    isBlocker = input ('Enter True if this TR is a blocker, else skip the input')
    impactedProducts = input('enter the list of impacted products separated by comma')
    impactedProducts = list(impactedProducts.split(','))
    isBlocker = False if isBlocker == '' else isBlocker
    instance.configureTroubleTicket(isBlocker=isBlocker,priority=priority,impactedProducts=impactedProducts)
    #instance._TroubleTicket__id=900 # this hacks the private access of the instance variable , don't do
    instance.printTroubleTicketInfo()
    instance.__repr__()


if __name__=='__main__':
    doWork()


