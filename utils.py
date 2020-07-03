import os
import pickle


def get_user():
    """Fetch the user details and check if user exists, if exists set the privileges"""
    clear()

    # Welcome
    print("*******Welcome to Small Library Management - Login******")

    # Fetch user and password from the user
    user = str(input("Enter username")).strip().lower()
    password = str(input("Enter Password")).strip()

    # load user infomation file to memory
    userDetails = pickle.load(open(os.getcwd() + "\\user.p", "rb"))

    # Check if user exists
    userData = [(userDict['user'], userDict['user_type']) for userDict in userDetails if
                (userDict['user'].lower() == user and \
                 userDict['password'] == password)]

    if userData:
        return userData[0]
    else:
        return None, None

#Function to clear screen
def clear():

    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux
    else:
        _ = os.system('clear')








