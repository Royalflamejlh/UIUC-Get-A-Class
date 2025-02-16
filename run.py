from getpass import getpass
from getEmails import getEmails
from getSchedule import getSchedule
print("To use this script you must have email notifications setup for the class you are trying to register for along with having outlook open to your school email") 

while(True):
    netid = input("NetID: ")
    password = getpass("Password for " + netid + ": ")
    term = input("What term are you registering for (ex. Spring 2023): ")


    CRNDict = {}
    typeClasses = input("Would you like to type in your classes? (True / False): ") == "True"
    if(typeClasses != True):
        print("Loading your classes from class.txt")
        f = open('class.txt', 'r')
        tempArr = []
        for line in f.read().splitlines():
            tempArr = line.split(' ')
            tempArr = [int(number) for number in tempArr ]
            CRNDict.update({tempArr[0]: tempArr})
     
    while(typeClasses):
        tempArr = []
        CRNEmail = int(input("CRN of class you are waiting for email from: "))
        tempArr.append(CRNEmail)
        CRNDict.update({CRNEmail: tempArr})
        i = int(input("Number of classses crosslisted or to register with " + str(CRNEmail) + ": "))
        for x in range(i):
            temp = int(input("CRN of crosslisted class number " + str((x + 1)) + ": "))
            tempArr.append(temp)
            CRNDict.update({CRNEmail: tempArr})
        print(CRNDict[CRNEmail])
        moreClasses = input("Add another class? (True / False): ")
        if moreClasses == "False":
            break
        
    print(CRNDict)
    while(True):
        CRN = 0
        if(len(CRNDict) == 0):
            print("Registered for all classes")
            exit()
            
        print("Waiting for Emails")
        
        while(CRN == 0):
            CRN = getEmails()
         
        print("Email Found for: " + str(CRN))
        
        if CRN in CRNDict:
            print("Attempting to Register")
            e = getSchedule(CRNDict[CRN], netid, password, term)
            print()
            if(e == 1):
                print("Registered for " + str(CRN))
                del CRNDict[CRN]
            elif(e == 0):
                print("Class already taken, waiting for another email")
                
            else:
                print("Error Registering, retry putting in netid, password, and term")
                break
        else:
            print("Email found for " + str(CRN) + " but it was not in list of classes")
    