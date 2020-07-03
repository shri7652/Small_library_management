from Session import session
import utils
import time
import sys
import user_class

def main():
    """Execution start point for library management"""

    #send login screen to get valid user name and user type
    user, user_type = user_class.get_user()
    if not user:
        utils.clear()
        utils.printMenuHead("Invalid User")
        print("Entered user doesn't exist, quitting")
        time.sleep(3)
        sys.exit(1)

    Session = session(user, user_type)

    #send Main Menu
    Session.theMainMenu()

if __name__ == '__main__':
    main()
