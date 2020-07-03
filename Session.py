import os
import datetime as dt
import menu_class
import user_class
import book_class

class session(menu_class.menu, user_class.user, book_class.bookShelf):
    """This class initiates a session with the user"""

    def __init__(self, user, user_type):
        """Initialise session parameters"""
        self.start_time = str(dt.datetime.now()).replace(':','-')
        self.user = user
        self.user_type = user_type

        #Log start of the session
        self.logger("Session with user {} started at {}".format(self.user,str(dt.datetime.now())))

        #Send the main menu screen


    def logger(self,data):
        with open(os.getcwd()+"\\logs\\" + self.user + '_'+ self.start_time + ".txt", "a") as log_file:
            log_file.write(str(dt.datetime.now()) + ":" + data + '\n')













