#start
contacts=[]
#User interface
while True:
    print("_________..:Phonebook:.._________")
    print('___________.:Options:.___________')
    print('1.Add')
    print('2.List')
    print('3.Search by name')
    print('4.Search by mobile')
    #print('5.Save')
    #print('0.EXIT')
    print('_________________________________')
    option=input()
    if option=='1':
        name = input("Enter new contact name: ")
        mobile = input("Enter new contact mobile number : ")
        contact = (name, mobile)
        contacts.append(contact)
        print('_________________________________')
    elif option=='2':
        print(contacts)
        print('_________________________________')
    elif option=='3':
        print('Name Search')
        name_search=input("enter name: ")
        for i in range(len(contacts)):
            for j in range (len(contacts[i])):
                if name_search==contacts[i][j]:
                    print(contacts[i])
                #else:
                    #print('no items match your search')
        print('_________________________________')
    elif option=='4':
        print("number search")
        number_search=input("enter mobile number: ")
        for i in range (len(contacts)):
            for j in range (len(contacts[i])):
                if number_search==contacts[i][j]:
                    print(contacts[i])
                #else:
                    #print('no items match your search')
        print('_________________________________')
    
