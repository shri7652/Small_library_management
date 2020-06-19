import os
import pickle
import datetime as dt

class session():
    """This class initiates a session with the user"""
    def __init__(self, user, user_type):
        """Initialise session parameters"""
        self.start_time = dt.datetime.now()
        self.user = user
        self.user_type = user_type


