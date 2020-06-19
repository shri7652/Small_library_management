""" While adding User Check if the user Already exists, if so ask for a change in name, code to be added"""

import os
import pickle

def get_user():

    """Fetch the user details and check if user exists, if exists set the privileges"""

    clear()

    #Welcome
    print("*******Welcome to Small Library Management - Login******" )

    #Fetch user and password from the user
    user = str(input("Enter username")).strip().lower()
    password = str(input("Enter Password")).strip()

    #load user infomation file to memory
    userDetails = pickle.load(open(os.getcwd()+"\\user.p","rb"))

    #Check if user exists
    userData = [(userDict['user'],userDict['user_type']) for userDict in userDetails if (userDict['user'].lower() == user and \
                userDict['password'] == password)]

    if userData:
        return userData[0]


def addUser():
    """This function will add a new user"""

    clear()

    print("*******Welcome to Small Library Management - Add New User******" )

    #Fetch user and password from the user
    user = str(input("Enter username")).strip().lower()
    password = str(input("Enter Password")).strip()
    check_pwd = password = str(input("Enter Password again to confirm")).strip()
    if password != check_pwd:
        clear()
        print("*******Welcome to Small Library Management - Invalid Password******" )
        print("passwords doesn't match - starting over again")
        addUser()

    user_type = str(input("Enter user_type (admin or user)")).strip()
    if user_type not in ['admin', 'user']:
        clear()
        print("*******Welcome to Small Library Management - invalid user_type******" )
        print("invalid user_type, starting over again")

    userDetails = pickle.load(open(os.getcwd()+"\\user.p","rb"))
    userDetails = userDetails + [{"user" : user, "user_type" : user_type, "password" : password}]

    pickle.dump(userDetails,open(os.getcwd()+"\\user.p","wb"))

    return True


#Function to clear screen
def clear():

    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux
    else:
        _ = os.system('clear')



