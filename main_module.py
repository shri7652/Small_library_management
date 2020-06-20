import pickle
import os
import time
import sys
from utils import *
from Session import *

def main():
    """Execution start point for library management"""

    #send login screen to get valid user name and user type
    user, user_type = get_user()
    if not user:
        clear()
        print("*******Welcome to Small Library Management - Invalid user******")
        print("Entered user doesn't exist, quitting")
        time.sleep(3)
        sys.exit(1)

    Session = session(user, user_type)


if __name__ == '__main__':
    main()
