

library_members = []

def find_member(name):
    #Checks if a member is registered
    if name in library_members:
        return(True)
    else:
        #print(name + ' not found in library_members!') #Not sure if this is needed here
        return(False)

def register_member(name):
    #Adds a member to library_members
    if not find_member(name):
        library_members.append(name)
        return(True)
    else:
        print(name + ' is already a member')
        return(False)

def testMain():
    register_member('Joe Smith')
    print('Test: register_member')
    print(library_members == ['Joe Smith'])

    print('Test: find_member')
    print('Should be True')
    print(find_member('Joe Smith'))
    print('Should be False')
    print(find_member('John the Baptist'))


if __name__ == '__main__':
    testMain()