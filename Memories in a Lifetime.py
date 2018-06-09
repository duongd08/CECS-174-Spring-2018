tmedia = {}

class Media:         #media super class which passes down title publisher and author

    def __init__(self,title,publisher,author):
        self.title = title
        self.publisher = publisher
        self.author = author

    def type(self):      #this function is here for future use if needed
        return 'media'

class Book(Media):
    #Book Class. Has information about the specific book. Also contains the inventory amount for specific book (self.avil)s

    rntr = []
    def __init__(self,title,publisher,author,pages):
        super().__init__(title,author,publisher)      #brings in the title author and publisher from media
        self.pages = pages          #unique to book
        self.avail = 1 #how many an individual item is ready to be rented. Number may be increased if stock for said item is also increased
    def __str__(self):
        return '{} written by {}, Publisher: {}, Pages: {}'.format(self.title,self.publisher,self.author,self.pages)

    def name(self):
        return '{} - Written by {}'.format(self.title, self.author)

    def describe(self):
        return '{} by {}, Publisher:{}, Pages: {}'.format(self.title,self.author,self.publisher,self.pages)

    def type(self):   #this function is here for future use if needed. Once more media items are introduced to library
        return 'Book'

    def checkout(self):
        #reduce available amount by 1

        if self.avail > 0:
            self.avail -= 1
        else:
            print('Sorry, this item is already checked out.')

    def checkin(self):
        if self.avail == 0:
           self.avail += 1

class Video(Media):
    avail = 1
    rntr = []
    def __init__(self,title,publisher,author,duration):
        super().__init__(title,publisher,author)           #brings in attributes from media
        self.duration = duration          #duration is unique to video

    def __str__(self):
        return '{}- Directed by {}, Publisher:{}, Running time: {} min'.format(self.title, self.author, self.publisher, self.duration)

    def name(self):
        return '{} - Directed by {}'.format(self.title, self.author)

    def describe(self):
        return'{}- Directed by {}, Publisher:{}, Running time: {} min'.format(self.title, self.author, self.publisher, self.duration)

    def type(self):    #this function is here for future use if needed
        return 'video'

    def checkout(self):
        if self.avail > 0:
            self.avail -= 1
        else:
            print('Sorry, this item is already checked out.')
    def checkin(self):
        if self.avail == 0:
            self.avail +=1
            self.rntr = []
#Books in Library
# B001 = Book('Learning Python','O\'Reilly Media','MARK LUTZ','1648')
B001 = 'B001'
tmedia[B001] = Book('Learning Python','O\'Reilly Media','MARK LUTZ','1648')
# print(tmedia[B001])
# print(tml[0])
B002 = 'B002'
tmedia[B002] = Book('Fluent Python: Clear, Concise, and Effective Programming','O\'Reilly Media','LUCIANO RAMALHO','792')

B003 = 'B003'
tmedia[B003] = Book('Python Crash Course: A Hands-On, Project-Based Introduction to Programming','No Starch','ERIC MATTHES','560')

#Movies in Library

V001 = 'V001'
tmedia[V001] =Video('Winnie the Pooh','Walt Disney Animation Studios','Don Hall','69')

V002 = 'V002'
tmedia[V002] =Video('Avengers','Marvel Studios','Joss" Whedon','143')

V003 = 'V003'
tmedia[V003] =Video('Logan ','20th Century Fox','James Mangold','141')

# print(tmedia)
# print(book1.describe())
#print(video3.describe())
#print(book2.describe())



class Member():

    mem_data = []

    def __init__(self, name):
        self.name = name
        self.rental_number = 2
        self.rentedItems = []


    def __str__(self):
        #Prints the name of member and how many rentals they have available (max 2)
        return 'Name: %s, Number of rentals available: %s' % (self.name , self.rental_number)

    def name(self):
        # Prints the name of member and how many rentals they have available (max 2)
        return 'Name: %s, Number of rentals available: %s' % (self.name, self.rental_number)

    def checkout(self,item):
        #appends rented item to member's rented item list
        #decrements rentals available to member by 1
        self.rentedItems.append(item)
        self.rental_number -= 1

    def checkIn(self,item):
        for i in range(0,len(self.rentedItems)-1):
            if self.rentedItems[i] == item:
                del self.rentedItems[i]
                self.rental_number += 1

    def rented(self, item):
        self.item = item
        # if item.Book.

        self.rentedItems.append(item)

    def rentLimit(self):
        if self.rental_number == 0:
            print('You have reached the rental limit. You must return an item before you can check something out again.')
        elif self.rental_number >= 1:
            self.rental_number -= 1
        else:
            pass

    def updateData(self, name):
        self.mem_data[name] = Member(name)

mem_data = {}      #empty dictionary used to store

#member1 = 'james iwamasa'
#member1 = member1.upper()
#mem_data[member1] = Member(member1)
totalmem = 0

ill = ')(*&^%$#@!-=_+[]{},.<>/?1234567890'
class Menu():
    total_mem = 0  # keeps count of total members that have been added

    def __init__(self):
        menuOptions = 1

        while menuOptions != '0':
            # intial menu options
            self.rowdivider(100)
            menuOptions = input('\nLibrary Media Rental Menu. \nPlease select an option to continue.\n \n'
                                '(1) Add member \n'
                                '(2) Check Out \n'
                                '(3) Check in \n'
                                '(4) View members \n'
                                '(5) View all media  \n'
                                '(6) View available media \n'
                                '(7) View media rented by all members \n'
                                '(8) View media rented by an individual member \n'
                                '(9) Remove member \n'
                                '(0) To quit \n'
                                '\nMenu Selection: ')
            print()
            self.rowdivider(100)

            if menuOptions == '1':
                self.addMember()
            elif menuOptions == '2':
                self.checkOut()
            elif menuOptions == '3':
                self.checkIn()
            elif menuOptions == '4':
                self.viewMembers()
            elif menuOptions == '5':
                self.viewAll()
            elif menuOptions == '6':
                self.viewAvail()
            elif menuOptions == '7':
                self.viewRented()
            elif menuOptions == '8':
                self.viewMemRent()
            elif menuOptions == '9':
                self.remMember()
            elif menuOptions == '998':      #   test function to get help of someones name
                self.funhel()
            elif menuOptions == '0':
                pass
            else:
                print('Sorry that was not a valid option. \n')
        else:
            print('Thank you, don\'t forget to set the alarm before you leave home')

    def rowdivider(self, x):
        # used for aesthetics. Adds given number of * in a line
        print(x * '*')

    def addMember(self):
        memberName = []  # empty list for storing member name

        while True:                                               #Name verification while loop
            userIn = input('Please enter the first name of the new member \n')  # first name
            userIn = userIn.strip(ill)    #removes whitespace around input
            userIn = userIn.strip()       #removed illegal characters around input
            if userIn == '':
                print('First name cannot be blank. Please star over.')
                continue
            memberName.append(userIn.upper())
            userIn = input('Please enter the last name of the new member\n')  # extra last name input
            userIn = userIn.strip()   #removes whitespace around input
            userIn = userIn.strip(ill)  #removed illegal characters around input
            if userIn == '':
                print(' Last name cannot be blank. Please start over.')
                continue
            memberName.append(userIn.upper())
            mem_name = (memberName[0] + ' ' + memberName[1])
            print(mem_name)
            userIn = input('Is this name correct? (Y)es or (N)o  or (Q)uit\n')
            if userIn.upper() == 'Y':
                mem_name = (memberName[0] + ' ' + memberName[1])
                if mem_name not in mem_data:                          #if name is not in the database name is added to database
                    mem_data[mem_name] = Member(mem_name)  # mem_name assigned to Member class
                    print('\nMember:', mem_name, 'has been added.')
                    break
                elif (mem_name) in mem_data:
                    print('This person is already a member!')                  #if name is in database returns this message
                    break
            # print(memberName)    test line to print member line list
            elif userIn.upper() == 'N':                             #incorrect name results in loop running again
                memberName = []                             #member name list is replaced with an empty list
                pass
            elif userIn.upper() == 'Q':
                memberName = []
                break
            else:
                print('Invalid input. Please start over.')
                memberName = []

        # mem_data[mem_name] = [Member(mem_name)]
        # mem_datl.append(mem_name)
        # print(mem_name)
        # print(Member(mem_name))
        # print(help(mem_name))            #prints mem_name data  testing to see if class was assigned and is correct
        # print(mem_data[mem_name])          #prints membership dictionary
        # print(mem_data)
        # print(mem_datl[0])
        # print(mem_name)
        # for name in memberName:      for name in memnberName list assigns each name to the Member class instead i changed it to assigning the combination of list to the memberclass
        #     name = Member(name)

        # print('New member was added: ', memberName[0], memberName[1])

        Menu()

    def checkOut(self):
        # user input
        memberName = []  # empty list
        while True:                  #name verification loop
            userIn = input('Please enter your first name\n')  # first name
            userIn = userIn.strip(ill)  # removes whitespace around input
            userIn = userIn.strip()  # removed illegal characters around input
            memberName.append(userIn.upper())

            userIn = input('Please enter your last name\n')  # extra last name input
            userIn = userIn.strip(ill)  # removes whitespace around input
            userIn = userIn.strip()  # removed illegal characters around input
            memberName.append(userIn.upper())
            mem_name = memberName[0] + ' ' + memberName[1] #member name string
            print(mem_name)
            userIn = input('Is this name correct? (Y)es or (N)o   Press \'Q\' to quit.\n')
            if userIn.upper() == 'Y':
                if mem_name in mem_data: #Check to see if member exists
                    if mem_data[mem_name].rental_number > 0:
                        print('What you like to you rent?\n') #for every member class in the mem_data dictionary (member name -> member class instance)

                        #
                        #Will display to user a list of available media items. Does not show items that are currently being rented
                        for i in tmedia: #for media id(eg. B001) in media dictionary ( media id -> media class)

                            if tmedia[i].avail >= 1: #changed from avail == 1. What if more than 1 available? Checks to see if media instock
                                print(i, ':', tmedia[i])


                        userIn = input('\nEnter the item\'s reference # you would like to rent.\n')
                        if userIn.upper() in tmedia and tmedia[userIn.upper()].avail >= 1: #if user desired checkout is in the media dictionary and if that media item is available to be rented (avail >= 1)
                            #Member Class updates
                            mem_data[mem_name].checkout(tmedia[userIn.upper()]) #performs the check out. calls checkout from member class
                            #mem_data[mem_name].rentedItems.append(tmedia[userIn.upper()])   #adds the checked out item to rented item list for the member

                            #
                            #Media Class Updates
                            tmedia[userIn.upper()].checkout()  #decrements media inventory by 1
                            tmedia[userIn.upper()].rntr.append(mem_name)  # adds the member name to the renter list in the items class

                            #
                            #Output
                            print(mem_name, 'has checked out:', tmedia[userIn.upper()].name())
                            break
                            # for i in mem_data:
                            #     if i == mem_name:
                            #         mem_data[i].checkout(tmedia[userIn.upper()])
                            #         # mem_data[(memberName[0] + ' ' + memberName[1])].rentedItems.append(tmedia[userIn.upper()])       #adds the checked out item to rented item list for the member
                            #         # mem_data[(memberName[0] + ' ' + memberName[1])].rentLimit()                    #runs the rent limit function in the member class which subtracts the rental number by 1
                            #         tmedia[userIn.upper()].checkout()  # runs the check out function of the checked out item
                            #         tmedia[userIn.upper()].rntr.append((memberName[0] + ' ' + memberName[1]))  # adds the member name to the renter list in the items class
                            #         print('You have checked out:', tmedia[userIn.upper()].name())
                            # # print(memberName)                                 ##test code
                            # # print(mem_data[mem_name].rentedItems)            ##test code
                            # # print(mem_data[mem_name].rental_number)             #test code
                            # # print(tmedia[userIn.upper()].avail)                 #test code
                            # # print(tmedia[userIn.upper()].rntr)                   #test code

                        elif userIn.upper() not in tmedia:
                            print()
                            print('Incorrect reference number')
                            break
                        else:
                            print('This item is already checked out.')
                            break
                    else:
                        print()
                        print('Sorry you have reached your rental limit.')
                        print('Please return one or all of the following:\n')
                        for i in mem_data[(memberName[0] + ' ' + memberName[1])].rentedItems:
                            print(i)
                        print('\n')
                        break
                # if (memberName[0]+memberName[1]) in mem_data:
                #     if mem_name.rental_number == 2:
                #         print('You have two rentals available.')
                #     elif mem_name.rental_number == 1:
                #         print('You have 1 rental left.')
                #     elif mem_name.rental_number == 0:
                #         print('Sorry, you have 0 rentals left. You must return an item before you are able to check something out again.')
                # Member.rentLimit(memberName)

                else: #if (mem_name) not in mem_data:
                    print('This person is not a member.')
                    memberName = []
                    break
            elif userIn.upper() == 'N':  # incorrect name results in loop running again
                memberName = []  # member name list is replaced with an empty list
                pass
            elif userIn.upper() == 'Q':
                memberName = []
                break
            else:
                print('Invalid input. Please start over.')
                memberName = []
    def viewMembers(self):
        if len(mem_data) == 0:
            print('There are 0 members.')
        elif len(mem_data) == 1:
            print('There is 1 member.')
            for i in mem_data:
                print(i)
        elif len(mem_data) >= 2:
            print('There is a total of', len(mem_data), 'members.')
            for i in mem_data:
                print(i)

    def checkIn(self):
        # user input
        memberName = []  # empty list
        while True:           #name verification loop
            userIn = input('Please enter your first name\n')
            userIn = userIn.strip(ill)  # removes whitespace around input
            userIn = userIn.strip()  # removed illegal characters around input
            memberName.append(userIn.upper())

            userIn = input('Please enter your last name\n')
            userIn = userIn.strip(ill)  # removes whitespace around input
            userIn = userIn.strip()  # removed illegal characters around input
            memberName.append(userIn.upper())
            mem_name = memberName[0] + ' ' + memberName[1]
            print(mem_name)
            userIn = input('Is this name correct? (Y)es or (N)o   Press \'Q\' to quit.\n')
            if userIn.upper() == 'Y':
                if mem_name in mem_data:
                    if len(mem_data[
                               mem_name].rentedItems) == 2:  # if rented items is 2 then this menu is displayed for check in
                        print('You have these items checked out:')
                        print('1:', mem_data[mem_name].rentedItems[0])  # first item within rentedItems list
                        print('2:', mem_data[mem_name].rentedItems[1])  # second item within rentedItems list
                        userIn = input('Which item are you returning?\n'
                                       'Type 1 for option #1 or 2 for option #2\n')

                        if userIn.upper() == '1':  # first option
                            # mem_data[mem_name].rentedItems.pop(0)               #test code
                            print('Thank you for returning', mem_data[mem_name].rentedItems[0].name())
                            mem_data[mem_name].checkIn(mem_data[mem_name].rentedItems[
                                                           0])  # runs check in function within member class for the first item within the rentedItems list in the member class
                            #     print(mem_data[mem_name].rentedItems)                 #test code
                            #     print(len(mem_data[mem_name].rentedItems))            #test code
                            #     print(mem_data[mem_name].rentedItems[0])              #test code
                            #     print(mem_data[mem_name].rental_number)               #test code
                            for i in tmedia:  # runs check in functino for media
                                if tmedia[i] == mem_data[mem_name].rentedItems[0]:
                                    tmedia[i].checkin()
                            break

                        elif userIn.upper() == '2':
                            print('Thank you for returning', mem_data[mem_name].rentedItems[1].name())
                            mem_data[mem_name].checkIn(mem_data[mem_name].rentedItems[
                                                           1])  # runs check in function within member class for the second item within the rentedItems list in the member class
                            for i in tmedia:  # runs check in function for media
                                if tmedia[i] == mem_data[mem_name].rentedItems[1]:
                                    tmedia[i].checkin()
                            break
                                    # print(mem_data[mem_name].rentedItems)
                                    # print(mem_data[mem_name].rental_number)
                        # elif userIn.upper() == 'B':
                        #     for i in range(0,len(mem_data[mem_name].rentedItems)-1):
                        #         mem_data[mem_name].checkIn(mem_data[mem_name].rentedItems[i])
                        #         for x in tmedia:                                                            #runs checkin function for media
                        #             if tmedia[x] == mem_data[mem_name].rentedItems[i]:
                        #                 tmedia[x].checkin()

                        #     print(mem_data[mem_name].rentedItems[0])
                        #     print(mem_data[mem_name].rental_number)
                        else:
                            print('2')

                    elif len(mem_data[mem_name].rentedItems) == 1:
                        print('You have this item checked out:')
                        print('1:', mem_data[mem_name].rentedItems[0])
                        userIn = input('Would you like to return it? Type \'Y\' for yes or \'N\' for no.\n')
                        if userIn.upper() == 'Y':
                            print('Thank you for returning', mem_data[mem_name].rentedItems[0].name())
                            mem_data[mem_name].checkIn(mem_data[mem_name].rentedItems[0])
                            #     print(mem_data[mem_name].rentedItems)                 #test code
                            #     print(len(mem_data[mem_name].rentedItems))            #test code
                            #     print(mem_data[mem_name].rentedItems[0])              #test code
                            #     print(mem_data[mem_name].rental_number)               #test code
                            for i in tmedia:
                                if tmedia[i] == mem_data[mem_name].rentedItems[0]:
                                    tmedia[i].checkin()
                            print('\n')
                            break
                        else:
                            break
                    elif len(mem_data[mem_name].rentedItems) == 0:
                        print('You don\'t have anything checked out. You can check out 2 items.')
                        break
                    else:
                        pass
                elif mem_name not in mem_data:
                    print('This person is not a member.')
                    break

        # print(memberName)    test line to print member line list
            elif userIn.upper() == 'N':  # incorrect name results in loop running again
                memberName = []  # member name list is replaced with an empty list
                pass
            elif userIn.upper() == 'Q':
                memberName = []
                break
            else:
                print('Invalid input. Please start over.')
                memberName = []

    def viewAll(self):
        for i in tmedia:
            print(i, ':', tmedia[i])
        print('\n')

    def viewAvail(self):
        books = 0
        videos = 0
        for i in tmedia:
            if tmedia[i].avail == 1:
                print(i, ':', tmedia[i])
                if i[0].upper() == 'B':
                    books += 1
                if i[0].upper() == 'V':
                    videos += 1
        print(books, 'books are available.')
        print(videos, 'videos are available.')
        print('\n')

    def viewRented(self):
        total = 0 #Total media items currently being rented by members
        tmem = 0

        for i in tmedia:
            if tmedia[i].avail == 0:
                print(i, ':', tmedia[i]) #prints specific media that has been checked out
                print()
                print('Is rented by:', tmedia[i].rntr[0])
                print()
                total += 1

        for i in mem_data:
            if mem_data[i].rental_number < 2:
                tmem += 1

        if total == 0:
            print('0 items are rented.')
        elif total == 1:
            print('1 item is rented.')
        elif total >= 2:
            print('A total of', total, 'items are rented')
        if tmem == 0:
            pass
        elif tmem == 1:
            print('By 1 member.')
        elif tmem >= 2:
            print('By a total of', tmem, 'members.')
        print('\n')

    def viewMemRent(self):
        memberName = []  # empty list
        while True:                     # name verification while loop
            userIn = input('Please enter your first name\n')
            userIn = userIn.strip(ill)  # removes whitespace around input
            userIn = userIn.strip()  # removed illegal characters around input
            memberName.append(userIn.upper())

            userIn = input('Please enter your last name\n')
            userIn = userIn.strip(ill)  # removes whitespace around input
            userIn = userIn.strip()  # removed illegal characters around input
            memberName.append(userIn.upper())

            mem_name = memberName[0] + ' ' + memberName[1]
            userIn = input('Is this name correct? (Y)es or (N)o   Press \'Q\' to quit.\n')
            if userIn.upper() == 'Y':
                if mem_name in mem_data:
                    if len(mem_data[mem_name].rentedItems) == 2:  # if rented items is 2 then this menu is displayed for check in
                        print('Member:', mem_name, 'Has these items checked out:\n')
                        print('1:', mem_data[mem_name].rentedItems[0])  # first item within rentedItems list
                        print('2:', mem_data[mem_name].rentedItems[1])  # second item within rentedItems list
                        print(mem_name, 'has reached the checkout limit and cannot check out anymore items.')
                        break
                    elif len(mem_data[mem_name].rentedItems) == 1:
                        print('Member:', mem_name, 'has this item checked out: \n')
                        print(mem_data[mem_name].rentedItems[0])
                        print(mem_name, 'can check out 1 more item.')
                        break
                    elif len(mem_data[mem_name].rentedItems) == 0:
                        print('Member:', mem_name, 'doesn\'t have anything checked out.')
                        print(mem_name, 'can check out 2 items.')
                        break
                    print('\n')
                elif mem_name not in mem_data:
                    print('This person is not a member.')
                    print('\n')
                    break
            elif userIn.upper() == 'N':
                memberName = []
                pass
            elif userIn.upper() == 'Q':
                memberName = []
                break
            else:
                print('Invalid input. Pleas start over.')
                memberName = []
    def remMember(self):
        memberName = []  # empty list
        while True:      # name verification while loop
            userIn = input('Please enter the first name of the member you would like to remove.\n')
            userIn = userIn.strip(ill)  # removes whitespace around input
            userIn = userIn.strip()  # removed illegal characters around input
            memberName.append(userIn.upper())

            userIn = input('Please enter the last name of the member you would like to remove\n')
            userIn = userIn.strip(ill)  # removes whitespace around input
            userIn = userIn.strip()  # removed illegal characters around input
            memberName.append(userIn.upper())

            mem_name = memberName[0] + ' ' + memberName[1]
            userIn = input('Is this name correct? (Y)es or (N)o   Press \'Q\' to quit.\n')
            if userIn.upper() == 'Y':
                if mem_name in mem_data:
                    if mem_data[mem_name].rental_number == 2:
                        print('Are you sure you would like to remove the member:', mem_name)
                        userIn = input('(Y)es or (N)o\n')
                        if userIn.upper() == 'Y':
                            print('Member:', mem_name, 'has been removed.')
                            del mem_data[mem_name]
                            break
                        elif userIn.upper() == 'N':
                            print(mem_name, 'is still a member.')
                            break
                    else:
                        print('Member:', mem_name, 'cannot be removed.')
                        print(mem_name, 'needs to return the following items before they can be removed from the database.')
                        for i in mem_data[mem_name].rentedItems:
                            print(i)
                        print('\n')
                        break
                elif mem_name not in mem_data:
                    print('This person is not a member.')
                    break
            elif userIn.upper() == 'N':
                memberName = []
                pass
            elif userIn.upper() == 'Q':
                memberName = []
                break
            else:
                print('Invalid input. Please start over.')
                memberName = []
    def funhel(self):
        memberName = []  # empty list

        userIn = input('Please enter the first name of the member you would like to remove.\n')
        userIn = userIn.strip(ill)  # removes whitespace around input
        userIn = userIn.strip()  # removed illegal characters around input
        memberName.append(userIn.upper())

        userIn = input('Please enter the last name of the member you would like to remove\n')
        userIn = userIn.strip(ill)  # removes whitespace around input
        userIn = userIn.strip()  # removed illegal characters around input
        memberName.append(userIn.upper())

        mem_name = memberName[0] + ' ' + memberName[1]
        if (memberName[0] + ' ' + memberName[1]) in mem_data:
            print(help(mem_data[memberName[0] + ' ' + memberName[1]]))
            print(mem_data)


Menu()

