import os
import pickle
import datetime as dt

class session():
    """This class initiates a session with the user"""
    def __init__(self, user, user_type):
        """Initialise session parameters"""
        self.start_time = str(dt.datetime.now()).replace(':','-')
        self.user = user
        self.user_type = user_type

        #Log start of the session
        self.logger("Session with user {} started".format(self.user))



    def logger(self,data):
        with open(os.getcwd()+"\\logs\\" + self.user + '_'+ self.start_time + ".txt", "a") as log_file:
            log_file.write(data + '\n')


    def theMenu(self):
        if self.user_type == 'admin':
            menu = """
            1. User Management
            2. Book Shelf Management
            3. Book Shelf browse
            4. update password
            5. Quit
            """

        else:
            menu = """
            1. Book Shelf browse
            2. update password
            3. Quit
            """
        return menu






