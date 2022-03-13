#start
contacts=[]
from collections import namedtuple
#User interface
while True:
    print("_________..:Phonebook:.._________")
    print('___________.:Options:.___________')
    print('''1.Add
2.List
3.Search
0.EXIT''')
    #print('4.Sort')
    #print('5.Edit')
    #print('6.Delete')
    #print('7.Save')
    print('_________________________________')
    option=input()
    if option=='1':
        name = input("Enter new contact name: ")
        mobile = input("Enter new contact mobile number: ")
        email = input("Enter new contact email: ")
        contact = (name, mobile,email)
        contacts.append(contact)
        print('_________________________________')
    elif option=='2':
        print(contacts)
        print('_________________________________')
    elif option=='3':
        result=""
        print('''Search
1.by name
2.by number
3.by e-mail
0.Exit''')
        search_option=input()
        if search_option=='1':
            print('name search')
            name_search=input("enter name: ")
            for i in range (len(contacts)):
                for j in range (len(contacts[i])-1):
                    if name_search==contacts[i][0]:
                        result=contacts[i]
        elif search_option=='2':
            print("number search")
            number_search=input("enter mobile number: ")
            for i in range (len(contacts)):
                for j in range (len(contacts[i])-1):
                    if number_search==contacts[i][1]:
                        result=contacts[i]
        elif search_option=='3':
            print('e-mail search')
            email_search=input("enter e-mail: ")
            for i in range (len(contacts)):
                for j in range (len(contacts)-1):
                    if email_search==contacts[i][2]:
                        result=contacts[i]
        print(result)
        if result=="":
            print('no items match your search')
        print('_________________________________')
    #elif option=='4':
        #print('Sorting')
        #print('1.by name')
        #print('2.by number')
        #print('3.by email')
        #print('0.Exit')
        #s_option=input()
        #if s_option == 1:
            #for x in contacts:
                #for i in  range (len(contacts)-1):
                    #if contacts[i][0]>contacts[i+1][0]:
                        #contacts[i],contacts[i+1]=contacts[i+1],contacts[i]
                        #print('sorted by name')
        #elif s_option==2 :
            #for x in contacts:
                #for i in  range (len(contacts)-1):
                    #if contacts[i][1]>contacts[i+1][1]:
                        #contacts[i],contacts[i+1]=contacts[i+1],contacts[i]
                        #print('sorted by number')
        #elif s_option==3 :
            #for x in contacts:
             #   for i in  range (len(contacts)-1):
              #      if contacts[i][2]>contacts[i+1][2]:
               #         contacts[i],contacts[i+1]=contacts[i+1],contacts[i]
                    #    print('sorted by email')
        #elif s_option==0 :
          #  break
        #print(contacts)
        #print('_________________________________')
    elif option=='0':
        print('Good Luck')
        break
    
