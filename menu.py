#This module contains menu options
import sys
from utils import *
#main_menu
def theMainMenu(user_type):
    """Takes in the user_type and sends the main menu screen accordingly"""
    if user_type == 'admin':
        menuFunc = {"1" : "userManagement()", "2": "bookShelfManagement()", "3" : "bookShelfBrowse()", "4": "updatePassword()",
                    "5" : "exit"}
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
    clear()
    print("*******Welcome to Small Library Management - Main Menu******")
    print(menu)
    choice = str(input("Enter your choice")).strip()

    if menuFunc[choice] == "exit":
        print("quitting")
        time.sleep(3)
        sys.exit(0)
    else:
        print(menuFunc[choice])
        time.sleep(3)









#def userManagement():

