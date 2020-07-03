import utils
import pickle
import os
import time

def get_user():
    """Fetch the user details and check if user exists, if exists set the privileges"""
    utils.clear()

    # Welcome
    utils.printMenuHead("Login")

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

class user():

    def addUser(self):
        """This function will add a new user"""

        utils.clear()
        utils.printMenuHead("Add New User")

        #Load user details
        userDetails = pickle.load(open(os.getcwd()+"\\user.p","rb"))

        #Fetch user and password from the user
        user = str(input("Enter username")).strip().lower()
        check_existing_user = [userDict['user'] for userDict in userDetails if userDict['user'] == user ]
        #Check if user Exists
        if check_existing_user:
            utils.clear()
            utils.printMenuHead("User Already Exists")
            print("User Already exists !!!!")
            time.sleep(3)
            return None

        #Ask for password
        password = str(input("Enter Password")).strip()
        check_pwd = str(input("Enter Password again to confirm")).strip()

        while password != check_pwd:
            utils.clear()
            utils.printMenuHead("Invalid Password")
            check_pwd = str(input("Enter Password again to confirm")).strip()

        user_type = str(input("Enter user_type (admin or user)")).strip()
        while user_type not in ['admin', 'user']:
            utils.clear()
            utils.printMenuHead("invalid user_type")
            user_type = str(input("Enter user_type (admin or user)")).strip()



        userDetails = userDetails + [{"user" : user, "user_type" : user_type, "password" : password}]
        pickle.dump(userDetails,open(os.getcwd()+"\\user.p","wb"))

        return True, user


    def removeUser(self):
        """This function removes existing users from the system, Only an admin can remove users"""

        #load user details into memory
        userDetails = pickle.load(open(os.getcwd()+"\\user.p","rb"))

        utils.clear()
        utils.printMenuHead("Remove User")

        #get details of the user to be removed
        user = str(input("Enter username")).strip().lower()
        check_existing_user = [userDict['user'] for userDict in userDetails if userDict['user'] == user]

        #User should be existing to remove
        if not check_existing_user:
            utils.clear()
            utils.printMenuHead("User doesn't exist")
            print("User doesn't exist !!!!")
            time.sleep(3)
            return None

        #remove user
        userDetails = list(filter(lambda x: x['user'] != user, userDetails))

        #Confirm user is removed
        check_existing_user = [userDict['user'] for userDict in userDetails if userDict['user'] == user]
        if not check_existing_user:
            pickle.dump(userDetails,open(os.getcwd()+"\\user.p","wb"))
            utils.clear()
            utils.printMenuHead("User removed")
            print("User removed Succesfully !!!!")
            time.sleep(3)
            return True, user

    def updatePassword(self, user):
        """This function will update password for an existing user"""
        #load user details into memory
        userDetails = pickle.load(open(os.getcwd()+"\\user.p","rb"))

        utils.clear()
        utils.printMenuHead("Update Password")
        #Fetch user and password from the user
        #user = str(input("Enter username")).strip().lower()
        password = str(input("Enter Current Password")).strip()

        getUserInfo = [userDict for userDict in userDetails if userDict['user'] == user]


        i = 0
        while i <= 3:
            if password == getUserInfo[0]['password']:
                break

            utils.clear()
            utils.printMenuHead("Invalid password")
            print("Enter the password again - Only 3 more tries !!!!")
            password = str(input("Enter Current Password")).strip()
            i += 1

        else:
            return False

        new_password = str(input("Enter New Password")).strip()
        check_pwd = str(input("Enter Password again to confirm")).strip()

        while new_password != check_pwd:
            utils.clear()
            utils.printMenuHead("Invalid Password")
            check_pwd = str(input("Enter Password again to confirm")).strip()

        getUserInfo[0]['password'] = new_password
        userDetails = list(filter(lambda x: x['user'] != user, userDetails)) + getUserInfo
        pickle.dump(userDetails,open(os.getcwd()+"\\user.p","wb"))
        utils.clear()
        utils.printMenuHead("password updated")
        print("Password for user {} updated successfully!!!!".format(user))
        time.sleep(3)

        return True, user


