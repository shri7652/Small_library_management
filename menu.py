#This module contains menu options
import sys
from utils import *
#main_menu
def theMainMenu(user_type):
    """Takes in the user_type and sends the main menu screen accordingly"""
    if user_type == 'admin':

        menu = """
        1. User Management
        2. Book Shelf Management
        3. Book Shelf browse
        4. update password
        5. Quit
        """



    else:
        menuFunc = {"1" : "bookShelfBrowse()", "2": "updatePassword()", "3" : "exit"}
        print(menuFunc)
        menu = """
        1 Book Shelf browse
        2 update password
        3 quit
        """

    menuFunc = [{1 : userManagement(), 2: "bookShelfManagement()", 3 : "bookShelfBrowse()", 4: "updatePassword()",  5 : "exit"}]
    clear()
    print("*******Welcome to Small Library Management - Main Menu******")
    print(menu)
    choice = int(str(input("Enter your choice")).strip())

    if menuFunc[0][choice] == "exit":
        print("quitting")
        time.sleep(3)
        sys.exit(0)
    else:
        print(menuFunc[0][choice])
        time.sleep(3)




def userManagement():
    userMenu = """
    1 Add User
    2 Remove User
    3 Go back to main menu
    4 quit
    """
    menuFunc = {"1" : addUser(), "2" : removeUser(), "3" : theMainMenu(Session.user_type), "4" : "exit"}

    clear()
    print("*******Welcome to Small Library Management - User Management******")
    print(userMenu)
    choice = str(input("Enter your choice")).strip()

    if menuFunc[choice] == "exit":
        print("quitting")
        time.sleep(3)
        sys.exit(0)
    else:
        menuFunc[choice]
        time.sleep(3)


