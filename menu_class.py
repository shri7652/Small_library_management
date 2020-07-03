import utils
import os
import sys


class menu():
    """ Abstract Class for Menu """

    def printMenuHead(self, header):
        print("*******Welcome to Small Library Management - {} ******".format(header))

    def clear(self):

        # for windows
        if os.name == 'nt':
            _ = os.system('cls')

        # for mac and linux
        else:
            _ = os.system('clear')

    def theMainMenu(self):
        """Takes in the user_type and sends the main menu screen accordingly"""
        if self.user_type == 'admin':

            menu = """
            1. User Management
            2. Book Shelf Management
            3. Book Shelf browse
            4. update password
            5. Quit
            """
            menuFunc = {1: self.userManagement, 2: "bookShelfManagement", 3: "bookShelfBrowse", \
                        4: "updatePassword()", 5: sys.exit}

        else:

            menu = """
            1 Book Shelf browse
            2 update password
            3 quit
            """
            menuFunc = {"1": "bookShelfBrowse", "2": "updatePassword", "3": sys.exit}

        self.clear()
        self.printMenuHead("Main Menu")
        print(menu)
        menuFunc[int(str(input("Enter your choice")).strip())]()

    def userManagement(self):
        userMenu = """
        1 Add User
        2 Remove User
        3 Go back to main menu
        4 quit
        """
        menuFunc = {"1": self.addUser, "2": "removeUser()", "3": "theMainMenu(Session.user_type)", "4": sys.exit}

        self.clear()
        self.printMenuHead("User Management")
        print(userMenu)
        menuFunc[str(input("Enter your choice")).strip()]()

