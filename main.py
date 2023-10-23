############ IMPORT HERE #############
from utilities import *
import sys
from math import floor, ceil

book_collection = {}
start_date = None

############## IMPLEMENT FUNCTIONS HERE ############
def hogwarts_library(readedContent):
    splittedContent = readedContent.split('\n')
    # Remove white space
    splittedContent = [item.lstrip() for item in splittedContent]
    splittedContent = [item.rstrip() for item in splittedContent]

    # Remove Non Commands
    splittedContent = [item for item in splittedContent if (item.upper().startswith('NB') or item.upper().startswith('LI') or item.upper().startswith('DB') or item.upper().startswith('FB') or item.upper().startswith('AS') or item.upper().startswith('LM') or item.upper().startswith('PL') or item.upper().startswith('SD') or item.upper().startswith('CB') or item.upper().startswith('CR') or item.upper().startswith('LA') or item.upper().startswith('DT') or item.upper().startswith('AD') or item.upper().startswith('RB') or item.upper().startswith('HR') or item.upper().startswith('RH') or item.upper().startswith('OR') or item.upper().startswith('PR') or item.upper().startswith('UR') or item.upper().startswith('DR')) ]
    
     # Turn the command, arguments into a tuple
    tupledContent = [(item[:2], item[3:]) for item in splittedContent]
    tupledContent2 = []
 
    # Make the command upper case, trim white space in front of args
    for item in tupledContent:
        k = item[0].upper()
        v = item[1].lstrip()
        tupledContent2.append((k,v))
    
    finalContent = []
    
    # Concatenate command and arg into the same string
    for item in tupledContent2:
        
        if item[1] != '': 
            string = item[0] + ' ' + item[1]
            finalContent.append(string)
        elif item[1] == '':
            finalContent.append(item[0])
            
    ################################################################################################################################################################################################################
    #debugPrint(finalContent)
    
    # Start Commands
    for item in finalContent: 
        
        if item.startswith('NB'):
            command_nb(item)
        elif item.startswith('LI'):
            command_li()
        elif item.startswith('DB'):
            command_db(item)
        elif item.startswith('FB'):
            command_fb(item)
        elif item.startswith('AS'):
            command_as(item)
        elif item.startswith('LM'):
            command_lm(item)
        elif item.startswith('PL'):
            command_pl(item)
        elif item.startswith('SD'):
            command_sd(item)
        elif item.startswith('CB'):
            command_cb(item)
        elif item.startswith('CR'):
            command_cr(item)
        elif item.startswith('LA'):
            command_la()
        elif item.startswith('DT'):
            command_dt()
        elif item.startswith('AD'):
            command_ad()
        elif item.startswith('RB'):
            command_rb(item)
        elif item.startswith('RH'):
            command_rh(item)
        elif item.startswith('HR'):
            command_hr()
        elif item.startswith('OR'):
            command_or()
        elif item.startswith('PR'):
            command_pr()
        elif item.startswith('UR'):
            command_ur(item)
        elif item.startswith('DR'):
            command_dr(item)
        

def debugPrint(content):
    print()
    if type(content) == list:
        for item in content:
            print(item)
    else: 
        print(content)
    print()

def makeArg(stringToProcess):
    stringToProcess = stringToProcess.lstrip()
    stringToProcess = stringToProcess.rstrip()
    
    listArg = [stringToProcess[:2], stringToProcess[3:]]
    
    listArg[0] = listArg[0].upper()
    
    listArg[1] = listArg[1].lstrip()
    
    return listArg[1]
    
def dateToSlash(dateObj):
    day = str(dateObj.day)
        
    if len(day) == 1:
        day = '0'+day
            
    month = str(dateObj.month)
        
    if len(month) == 1:
        month = '0'+month
            
    year = str(dateObj.year)
        
    if len(year) == 1:
        year = '0'+year
        
    dateTuple = (month, day, year)
    dateString = '/'.join(dateTuple)
        
    return dateString

def duration(start, end):
        
    dealta = end - start
        
    return int(dealta.days)

def command_nb(string): 
    
    # Add a new book
    
    argument = makeArg(string)
    
    argumentList = argument.split(',')
    
    finalList = []
    
    for item in argumentList:
        splittedItem = item.split('=')
        finalList.append(splittedItem[1])
    
    title = finalList[0]
    author = finalList[1]
    year_published = int(finalList[2])
    subject = finalList[3]
    section = finalList[4]
    
    def newBook(title, author, year_published, subject, section):
        
        if title not in book_collection.keys(): 
            bookTuple = Book(title, author, year_published, subject, section)
            book_collection[title] = bookTuple
            
        elif title in book_collection.keys():
            print(title, 'already present.')
            print()
        
    newBook(title, author, year_published, subject, section)
    

def command_li():
    
    # List inventory
    
    def listInventory():
        
        sortedDictTuple = sorted(book_collection.items())
        
        numBook = len(book_collection.keys())
        
        print('*********************LIBRARY INVENTORY**********************')
        print('Number of books available: ', numBook)
        print('------------------------------------')
        
        for item in sortedDictTuple:
            bookTuple = item[1]
            
            title = bookTuple.title
            author = bookTuple.author
            date = bookTuple.year_published
            subject = bookTuple.subject
            section = bookTuple.section
            
            print('Title:', title)
            print('Author:', author)
            print('Date:', date)
            print('Subject:', subject)
            print('Section:', section)
            print('------------------------------------')
        
    listInventory()

def command_db(string):
    
    # Delete Book
    title = ''
    
    argument = makeArg(string)
    
    argumentList = argument.split('=')
    
    if len(argumentList) != 1:
        title = argumentList[1]
    elif len(argumentList) == 1:
        title = argument
    
    def deleteBook(title):
        
        if title in checkouts.keys():
            del checkouts[title]     
            
        if title in reservations.keys():
            del reservations[title]  
        
        if title not in book_collection.keys():
            print(title, 'Not Found. Cannot be deleted.')
        
        elif title in book_collection.keys():
            del book_collection[title]
            
    
    deleteBook(title)

def command_fb(string):
    
    # Find Books
    
    argument = makeArg(string)
    argumentList = argument.split(',')
    dictionary = {}
    findedBookDict = {}
    
    for item in argumentList:
        splittedItem = item.split('=')
        if len(splittedItem) == 2:
            dictionary[splittedItem[0]] = splittedItem[1]
            
    title = None
    author = None
    year = None
    subject = None
    section = None
    
    for item in dictionary.keys():
        if item == 'title':
            title = dictionary[item]
            
        elif item == 'author':
            author = dictionary[item]
            
        elif item == 'year_published':
            year = int(dictionary[item])
            
        elif item == 'subject':
            subject = dictionary[item]
            
        elif item == 'section':
            section = dictionary[item]
    
    def findBookFunction(title, author, year_published, subject, section):
        
        for key, bookTuple in book_collection.items():
            if bookTuple.title == title:
                findedBookDict[key] = bookTuple
            elif bookTuple.author == author:
                findedBookDict[key] = bookTuple
            elif bookTuple.author == author:
                findedBookDict[key] = bookTuple
            elif bookTuple.year_published == year:
                findedBookDict[key] = bookTuple
            elif bookTuple.subject == subject:
                findedBookDict[key] = bookTuple
            elif bookTuple.section == section:
                findedBookDict[key] = bookTuple
        
        for key, bookTuple in findedBookDict.copy().items():
            
            if title != None:
                if bookTuple.title != title:
                    del findedBookDict[key]
    
            if author != None:
                if bookTuple.author != author:
                    del findedBookDict[key]
                    
            
            if year != None:
                if bookTuple.year_published != int(year):
                    del findedBookDict[key]
                    
            
            if subject != None:
                if bookTuple.subject != subject:
                    del findedBookDict[key]
                   
            
            if section != None:
                if bookTuple.section != section:
                    del findedBookDict[key]
                    
                
    findBookFunction(title, author, year, subject, section)
    
    numBook = len(findedBookDict.keys())
    
    def printResult(title, author, year_published, subject, section):
        print('************************BOOK SEARCH*************************')
        
        if title == None and author == None and year_published == None and subject == None and section == None:
            sortedDictTuple = sorted(book_collection.items())
        
            num = len(book_collection.keys())
        
            print('Number of books found: ', num)
            print('------------------------------------')
        
            for item in sortedDictTuple:
                bookTuple = item[1]
            
                title = bookTuple.title
                author = bookTuple.author
                date = bookTuple.year_published
                subject = bookTuple.subject
                section = bookTuple.section
            
                print('Title:', title)
                print('Author:', author)
                print('Date:', date)
                print('Subject:', subject)
                print('Section:', section)
                print('------------------------------------')
        
        elif numBook == 0:
            print('No Books Found.')
            print('------------------------------------')
        
        else:
            print('Number of books found: ', numBook)
            print('------------------------------------')
        
            for item in findedBookDict.keys():
                bookTuple = book_collection[item]
            
                title = bookTuple.title
                author = bookTuple.author
                date = bookTuple.year_published
                subject = bookTuple.subject
                section = bookTuple.section
            
                print('Title:', title)
                print('Author:', author)
                print('Date:', date)
                print('Subject:', subject)
                print('Section:', section)
                print('------------------------------------')
    
    printResult(title, author, year, subject, section)


def command_as(string):
    
    # Add Student
    
    argument = makeArg(string)
    
    argumentList = argument.split(',')
    
    finalList = []
    
    for item in argumentList:
        splittedItem = item.split('=')
        finalList.append(splittedItem[1])
    
    student_name = finalList[0]
    house = finalList[1]
    checked_out_books = 0
    
    studentTuple = Student(student_name, house, checked_out_books)
    
    def addStudent():
        
        if student_name in library_members.keys():
            print(student_name, 'is already present.')
        
        elif student_name not in library_members.keys():
            library_members[student_name] = studentTuple
    
    addStudent()


def command_lm(string):
    
    # List Members
    
    memberDict = {'Gryffindor':[], 'Hufflepuff':[], 'Ravenclaw':[], 'Slytherin':[]}
    
    def listMember():
        for name, memberTuple in library_members.items():
            
            if memberTuple.house in memberDict.keys():
                
                if name not in memberDict[memberTuple.house]:
                    memberDict[memberTuple.house].append(name)
            
            elif memberTuple.house not in memberDict.keys():
                memberDict[memberTuple.house] = [name]
        
    
    def printResult():
        
        print('**********************LIBRARY MEMBERS***********************')
        
        for house, nameList in memberDict.items():
            print('{:>11}'.format(house+':'))
            
            string1 = '{:>30}'.format('No Registered Members')
            
            if len(memberDict[house]) == 0:
                print(string1)
                
            else: 
                nameList = tuple(nameList)
                nameList = sorted(nameList)
                nameList = list(nameList)
                
                for name in nameList:
                    string = '{:>30}'.format(name)
                    print(string)
    
    listMember()
    printResult()


def command_pl(string):
    
    # Print Lines
    
    arg = makeArg(string)
    
    def printLine(argument):
        if argument == '':
            pass
        else:
            print(argument)
    
    printLine(arg)

def command_sd(string):
    
    # Start Date
    
    argument = makeArg(string)
    
    dateList = argument.split('/')
    
    month = int(dateList[0])
    date = dateList[1]
    year = int(dateList[2])
    
    d = datetime.date(year, month, int(date))
    
    global start_date
    
    start_date = d
    
    weekday = d.strftime("%A")
    monthString = d.strftime("%B")
    
    if len(date) == 1:
        date = str(0) + date
    
    date = date.lstrip()
    date = date.rstrip()
    
    print('*************HOGWARTS LIBRARY MANAGEMENT SYSTEM*************')
    stringTemp = weekday + ' ' + date + ', ' + monthString + ' ' + str(year)
    num = (60 - len(stringTemp))/2
    print('*' * floor(num) + stringTemp + '*' * ceil(num))


def command_cb(string):
    
    # Checkout Book
    
    argument = makeArg(string)
    
    argumentList = argument.split(',')
    
    finalArgDict = {}
    
    for item in argumentList:
        splittedItem = item.split('=')
        finalArgDict[splittedItem[0]] = splittedItem[1]
    
    title = finalArgDict['title']
    student_name = finalArgDict['student_name']
    
    number_of_days = None
    
    if 'number_of_days' in finalArgDict.keys():
        number_of_days = int(finalArgDict['number_of_days'])
    else:
        number_of_days = 14
    
    global start_date
    
    due_date = start_date + datetime.timedelta(days=number_of_days)  
        
    pass_code = None
    
    if 'pass_code' in finalArgDict.keys():
        pass_code = finalArgDict['pass_code']
        
    if student_name not in library_members.keys():
        print(student_name, 'is not a registered library member.')
        return
    
    if title not in book_collection.keys():
        print(title, 'not in inventory.')
        return
    
    if title in checkouts.keys():
        print(title, 'is currently unavailable to be checked out.')
        return
    
    if book_collection[title].section == 'Restricted':
        
        if pass_code in library_passcodes:
            checkoutTuple = Checkout(title, student_name, due_date)
            checkouts[title] = checkoutTuple
        
        else:
            print(title, 'is a Restricted book, and requires a pass code to be checked out.')
            return
        
    elif book_collection[title].section == 'Non-Restricted':
        checkoutTuple = Checkout(title, student_name, due_date)
        checkouts[title] = checkoutTuple
     

def command_cr(string):
    
    # Checkout Report
    # Report of books checked out needs to be organized by each school name sorted alphabetically, then each student name sorted alphabetically, and each book title sorted alphabetically. 
    
    d = start_date
    
    dateString = dateToSlash(d)
    
    def finalPrint(checkoutTuple):
        
        title = checkoutTuple.book
        
        shortTitle = ''
        
        if len(title) > 30:
            shortTitle = title[:30]
        else:
            shortTitle = title
        
        name = checkoutTuple.student
        
        due_date = dateToSlash(checkoutTuple.due_date)
        
        print(checkout_report_format_string.format(title = shortTitle, name = name, due_date = due_date))
    
    print('***' + 'CURRENT CHECKOUT REPORT' + '**************' + dateString + '**********')
    
    if len(checkouts.keys()) == 0:
        print('                   No Books Checked Out.                    ')
    
    print(checkout_report_format_string.format(title = 'Book Title', name = 'Student Name', due_date = 'Due Date'))
    print('------------------------------------------------------------')
    
    Gryffindor = []
    Hufflepuff = []
    Ravenclaw = []
    Slytherin = []

    
    for title, checkoutTuple in checkouts.items():
        
        house = library_members[checkoutTuple.student].house
        
        if house == 'Gryffindor':
            Gryffindor.append((checkoutTuple.student, checkoutTuple.book))
        elif house == 'Hufflepuff':
            Hufflepuff.append((checkoutTuple.student, checkoutTuple.book))
        elif house == 'Ravenclaw':
            Ravenclaw.append((checkoutTuple.student, checkoutTuple.book))
        elif house == 'Slytherin':
            Slytherin.append((checkoutTuple.student, checkoutTuple.book))
    
    Gryffindor.sort()
    Hufflepuff.sort()
    Ravenclaw.sort()
    Slytherin.sort()
    
    for tuples in Gryffindor:
        checkoutTuple = checkouts[tuples[1]]
        
        finalPrint(checkoutTuple)
    
    for tuples in Hufflepuff:
        checkoutTuple = checkouts[tuples[1]]
        
        finalPrint(checkoutTuple)
        
    for tuples in Ravenclaw:
        checkoutTuple = checkouts[tuples[1]]
        
        finalPrint(checkoutTuple)
        
    for tuples in Slytherin:
        checkoutTuple = checkouts[tuples[1]]
        
        finalPrint(checkoutTuple)
        
    if len(checkouts.keys()) != 0:
        
        print()
    
    

def command_la():
    
    # List Available
    availableDict = book_collection.copy()
    
    for title in checkouts.keys():
        del availableDict[title]
    
    numBook = len(availableDict.keys())
    
    print('Number of books in available: ', numBook)
    print('------------------------------------')
    
    for title in sorted(availableDict.keys()):
        
        bookTuple = book_collection[title]
        
        title = bookTuple.title
        author = bookTuple.author
        date = bookTuple.year_published
        subject = bookTuple.subject
        section = bookTuple.section
        
        print('Title:', title)
        print('Author:', author)
        print('Date:', date)
        print('Subject:', subject)
        print('Section:', section)
        print('------------------------------------')
        

def command_dt():
    
    # Due Today
    
    global start_date
    
    slashDate = dateToSlash(start_date)
    print('*******BOOKS DUE TODAY******************' + slashDate + '**********')
    
    dueToday = {}
    titleList = []
    
    for title, checkoutTuple in checkouts.items():
        if checkoutTuple.due_date == start_date:
            dueToday[title] = checkoutTuple.student
            titleList.append(title)
    
    titleList = sorted(titleList)
    
    if len(dueToday.keys()) == 0:
        print('                    No books due today.                     ')
    else:
        for title in titleList:
            if len(title) > 35:
                shortTitle = title[:35] 
                name = checkouts[title].student
                
                print(due_today_format_string.format(title = shortTitle, name = name))
            
            else:
                name = checkouts[title].student
                print(due_today_format_string.format(title = title, name = name))  
    
    if len(checkouts.keys()) != 0:
        print()
            

penaltyDict = {}

def command_ad():
    
    # Advance Date
    global start_date
    start_date = start_date + datetime.timedelta(days=1)
    
    weekday = start_date.strftime("%A")
    monthString = start_date.strftime("%B")
    
    date = str(start_date.day)
    
    if len(date) == 1:
        date = str(0) + date
    
    year = start_date.year
    
    date = date.lstrip()
    date = date.rstrip()
    
    print('*************HOGWARTS LIBRARY MANAGEMENT SYSTEM*************')
    stringTemp = weekday + ' ' + date + ', ' + monthString + ' ' + str(year)
    num = (60 - len(stringTemp))/2
    print('*' * floor(num) + stringTemp + '*' * ceil(num))
    
    for title, tuples in checkouts.items():
        
        if tuples.due_date < start_date:
            
            days = abs(duration(tuples.due_date, start_date))
            
            studentName = tuples[1]
            
            houseName = library_members[studentName].house
            
            if days == 6:
                days -= 1
    
            penalty = penalties[days]
            
            points = penalty.point_deduction
            
            curse = penalty.curse
            
            bookTitle = title
            
            house_penalties[houseName] += points
            
            penaltyDict[studentName] = (houseName, curse)
    

def command_rh(string):
    
    # Request Hold
    
    argument = makeArg(string)
    
    argumentList = argument.split(',')
    
    finalArgDict = {}
    
    for item in argumentList:
        splittedItem = item.split('=')
        finalArgDict[splittedItem[0]] = splittedItem[1]
    
    title = finalArgDict['title']
    student_name = finalArgDict['student_name']
    
    if title not in book_collection.keys():
        print(title, 'not in inventory.')
        return
    
    if student_name not in library_members.keys():
        print(student_name, 'is not a registered library member.')
        return
    
    if title not in checkouts.keys():
        print(title, 'is available to be checked out. Use command to checkout book.')
        return
    
    if title in checkouts.keys():
        
        if checkouts[title].student == student_name:
            print(student_name, 'currently has checked out', title + '.')
            return
    
    if title in reservations.keys():
        
        resvTupleList = reservations[title]
        
        resvNameList = []
        
        for tuples in resvTupleList:
            resvNameList.append(tuples[0])
        
        if student_name in resvNameList:
            print(student_name, 'has already requested a hold for', title + '.')
            return
        
    
    number_of_days = None
    
    if 'number_of_days' in finalArgDict.keys():
        number_of_days = int(finalArgDict['number_of_days'])
    else:
        number_of_days = 14
        
    global start_date
    
    end_date = start_date + datetime.timedelta(days=number_of_days)  
    
    infoTuple = (student_name, start_date, end_date)
    
    if title in reservations.keys():
        
        resList = reservations[title]
        
        resList.append(infoTuple)
        
        reservations[title] = resList
    
    elif title not in reservations.keys():
        
        reservations[title] = [infoTuple]
        

def command_hr():
    
    # Hold Requests Report
    
    global start_date
    dateString = dateToSlash(start_date)
    
    print('*****' + 'HOLD REQUEST REPORT' + '****************' + dateString + '**********')
    print('Student Name                         # of Days Requested    ')
    print('------------------------------------------------------------')


    def shortTitle(titleToShorten):
        
        shortTitle = titleToShorten
        
        if len(shortTitle) > 60:
            shortTitle = shortTitle[:60]
        else:
            shortTitle = shortTitle
            
        return shortTitle
    
    
    def finalPrint(name, days):
        
        print(hold_report_format_string.format(name = name, number_of_days = days))

    titleList = []
    
    for title in reservations.keys():
        
        titleList.append(title)
    
    titleList.sort
    
    for title in titleList:
        print(shortTitle(title))
        
        tupleList = reservations[title]
        
        nameDict = {}
        
        for tuples in tupleList:
            
            name = tuples[0]
            
            start_date = tuples[1]
            
            end_date = tuples[2]
            
            d = duration(start_date, end_date)
            
            nameDict[name] = d
        
        nameList = []
        
        for name in nameDict.keys():
            nameList.append(name)
            
        nameList.sort
        
        for name in nameList:
            
            n = '   ' + name
            
            
            days = nameDict[name]
            
            finalPrint(n, days)
            
        print('------------------------------------------------------------')
    
    if len(titleList) == 0:
        print('                    No Holds Requested.                     ')
    
    print()
        

def command_rb(string):
    
    # Return Book
    
    global checkouts
    
    argument = makeArg(string)
    
    splitted = argument.split('=')
    
    title = splitted[1]
    
    if title not in book_collection.keys():
        print('Invalid Return Request for', title)
        return
    
    if title in checkouts.keys():
        del checkouts[title]
    
    if title in reservations.keys():
        
        resList = reservations[title]
        
        name = resList[0][0]
        end_date = resList[0][2]
        
        resList.pop(0)
        
        if len(resList) == 0:
            del reservations[title]
        
        elif len(resList) > 0:
            reservations[title] = resList
            
        checkoutTuple = Checkout(book = title, student = name, due_date = end_date)
        
        checkouts[title] = checkoutTuple

def command_or():
    
    # Overdue Report
    def shorten(string, length):
        
        shortTitle = string
        
        if len(shortTitle) > length:
            shortTitle = shortTitle[:length]
        else:
            shortTitle = shortTitle
            
        return shortTitle
    
    
    global start_date
    dateString = dateToSlash(start_date)
    
    format_string = "{title:<36}{name:<16}{days:<8}"
    
    print('********' + 'OVERDUE REPORT' + '*************' + dateString + '*******# Days**')
    
    titleList = []
    
    for title, checkoutTuple in checkouts.items():
        if checkoutTuple.due_date < start_date:
            titleList.append(title)
    
    titleList.sort()
    
    if len(titleList) == 0:
        print('                  No books overdue today.                   ')
    
    else:
        for title in titleList:
            name = checkouts[title].student
            
            name = shorten(name, 15)
            
            end = checkouts[title].due_date
            days = abs(duration(start_date, end))
            
            print(format_string.format(title = title, name = name, days = days))  
   
    print()

def command_pr():
    
    global start_date
    dateString = dateToSlash(start_date)
    
    print('********' + 'PENALTY REPORT' + '******************' + dateString + '**********')
    
    houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    
    houseFormat = "{house:>29}{pts:<2}"
    
    for house in houses:

        if house_penalties[house] == 0:
            
            string = house + ' Point Deductions: '
            
            pts = house_penalties[house]
            
            print(houseFormat.format(house = string, pts = pts))
        
        elif house_penalties[house] != 0:
            string = house + ' Point Deductions: '
            
            pts = house_penalties[house]
            
            print(houseFormat.format(house = string, pts = pts))
            
            for name, tuples in penaltyDict.items():
                
                if tuples[0] == house:
                    
                    string = name + 'Curse:'
                    
                    curse = penaltyDict[name][1]
                    
                    strFormat = "{string:>27}{curse:>25}"
                    print(strFormat.format(string = string, curse = curse))
            
def command_ur(string):
    
    #User Report
    
    argument = makeArg(string)
    
    argumentList = argument.split(',')
    
    student = ''
    
    for item in argumentList:
        splittedItem = item.split('=')
        student = splittedItem[1]
        
    if student not in library_members.keys():
        print(student, 'is not a registered member of the library.')
        print()
        return

    stringTemp = 'USER REPORT for ' + student
    num = 46 - len(stringTemp)
    print('*' * 15 + stringTemp + '*' * num)
    
    if student in penaltyDict.keys():
        
        curse = penaltyDict[student][1]
        
        string = student + ' Curse: ' + curse
        
        if student == 'Y':
            pass
        else:
            print('{:^60}'.format(string))
    
    print('-------------------------CHECKOUTS--------------------------')
    
    titleList = []
    
    for title, tuples in checkouts.items():
        if tuples[1] == student:
            titleList.append(title)
    
    titleList.sort()

    
    if len(titleList) == 0:
        print('                       No checkouts.                        ')
    else:
        for title in titleList:
            dueDate = dateToSlash(checkouts[title].due_date)
            
            print(user_report_format_string.format(title = title, due_date = dueDate))
    
    print()
                
    
    print('---------------------------HOLDS----------------------------')

    titleList = []
    
    for title, tupleList in reservations.items():
        
        for tuples in tupleList:
            if tuples[0] == student:
                titleList.append(title)
    
    titleList.sort()

    
    if len(titleList) == 0:
        print('                         No holds.                          ')
    else:
        for title in titleList:
            
            resvList = reservations[title]
            
            start = None
            
            end = None
            
            for tuples in resvList:
                
                if tuples[0] == student:
                    
                    start = tuples[1]
                    
                    end = tuples[2]
            
            dur = duration(start, end)
            
            print('{title:<30}{num:>30}'.format(title = title, num = dur))
    
    print()
    

def command_dr(string):
    
    # List All Books Due Between Two Dates
    
    argument = makeArg(string)
    
    argumentList = argument.split(',')
    
    aList = []
    
    start_date = None
    
    end_date = None
    
    for item in argumentList:
        splittedItem = item.split('=')
        aList.append(splittedItem[1])
    
    start_date = aList[0]
    end_date = aList[1]
    
    print('***BOOKS DUE BETWEEN********' + str(start_date) +  ' to ' + str(end_date) + '********')
    
    def slashToDate(string):
        
        sep = string.split('/')
        
        date = datetime.date(int(sep[2]), int(sep[0]), int(sep[1]))
        
        return date
    
    startDateOBJ = slashToDate(start_date)
    endDateOBJ = slashToDate(end_date)
    
    titleList = []
    
    if startDateOBJ> endDateOBJ:
        print('             No books due for the given dates.              ')
        return
    
    while startDateOBJ != endDateOBJ:
        
        dueDate = startDateOBJ
        
        for title, checkoutTuple in checkouts.items():
            
            if checkoutTuple.due_date - datetime.timedelta(days=1) == dueDate:
                
                titleList.append(title)
    
        startDateOBJ = startDateOBJ + datetime.timedelta(days=1)
    
    titleList.sort()
    
    if len(titleList) == 0:
        print('             No books due for the given dates.              ')
        return

    
    for title in titleList:
        
        name = checkouts[title].student
        
        print('{title:<30}{student:>30}'.format(title = title, student = name))
    
    print()
               
    
    
if __name__ == "__main__": 
    
    fileName = ''
    
    if False:
        fileName = sys.argv[1]
        
    else: 
        fileName = 'Stage2_CB_CR_LA.txt'
    
    with open(fileName, 'r+') as fileContent:
        readedContent = fileContent.read()
        hogwarts_library(readedContent)
    

