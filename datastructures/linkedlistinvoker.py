from linkedlisthelper import linkedlistHelper
def doJob():
    linkedlistHelper_obj = linkedlistHelper()
    linkedlistHelper_obj.addNode(20)
    linkedlistHelper_obj.addNode(30)
    linkedlistHelper_obj.addNode(40)

    linkedlistHelper_obj.printnodes()

    # reversing
    linkedlistHelper_obj.trigger()
    linkedlistHelper_obj.printnodes()

    # insert after head
    linkedlistHelper_obj.insertafter(25, 20)
    linkedlistHelper_obj.printnodes()

    # insert in middle
    linkedlistHelper_obj.insertafter(78, 30)
    linkedlistHelper_obj.printnodes()

    # insert after tail
    linkedlistHelper_obj.insertafter(145, 40)
    linkedlistHelper_obj.printnodes()

    linkedlistHelper_obj.countnodes()

    #delete head
    linkedlistHelper_obj.deletenode(20)
    linkedlistHelper_obj.printnodes()

    # delete in middle
    linkedlistHelper_obj.deletenode(30)
    linkedlistHelper_obj.printnodes()

    # reversing
    linkedlistHelper_obj.trigger()
    linkedlistHelper_obj.printnodes()

    # delete tail
    linkedlistHelper_obj.deletenode(145)
    linkedlistHelper_obj.printnodes()


if __name__ == '__main__':
    doJob()