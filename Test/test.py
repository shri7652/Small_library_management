import pickle
import datetime as dt
import os
"""
print(str(dt.datetime.now()).split())
bookShelf = [{'Name':'SomeName', 'Author': 'SomeAuthor'}, {'Name':'SomeName1', 'Author': 'SomeAuthor1'}]
pickle.dump(bookShelf,open(os.getcwd()+"\\save.p","wb"))

copiedShelf = pickle.load(open(os.getcwd()+"\\save.p","rb"))
print(copiedShelf)

userDetails = [{"user" : "gkvvnm", "user_type" : "admin", "password" : "amma2013"}, \
               {"user" : "ranju1729", "user_type" : "user", "password" : "Vrinda8@"}]
pickle.dump(userDetails,open(os.getcwd()+"\\user.p","wb"))

copiedUser = pickle.load(open(os.getcwd()+"\\user.p","rb"))
print(copiedUser)

a,b,c = (1,2,3)
print(a,b,c)
"""
b = 'abcd'
a = ""
while a != b:
    a = str(input("Entter a"))

menu = """
        1. Book Shelf browse
        2. update password
        3. Quit
        """
menuFunc = {"1" : "bookShelfBrowse()", "2": "updatePassword()", "3" : sys.exit(0)}

