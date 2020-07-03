import utils
import sys


class menu():
    """ Abstract Class for Menu """

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
            menuFunc = {"1": self.userManagement, "2": "bookShelfManagement", "3": "bookShelfBrowse", \
                        "4": "updatePassword()", "5": sys.exit}

        else:

            menu = """
            1 Book Shelf browse
            2 update password
            3 quit
            """
            menuFunc = {"1": "bookShelfBrowse", "2": "updatePassword", "3": sys.exit}

        utils.clear()
        utils.printMenuHead("Main Menu")
        print(menu)

        try:
            menuFunc[str(input("Enter your choice   :")).strip()]()
        except KeyError:
            utils.clear()
            utils.printMenuHead("Invalid option entered")
            self.theMainMenu()



    def userManagement(self):
        userMenu = """
        1 Add User
        2 Remove User
        3 Go back to main menu
        4 quit
        """
        menuFunc = {"1": self.addUser, "2": self.removeUser, "3": self.theMainMenu, "4": sys.exit}

        utils.clear()
        utils.printMenuHead("User Management")
        print(userMenu)
        try:
            menuFunc[str(input("Enter your choice   :")).strip()]()
        except KeyError:
            utils.clear()
            utils.printMenuHead("Invalid option entered")
            self.userManagement()

        self.userManagement()


