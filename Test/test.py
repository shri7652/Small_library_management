import pickle
import datetime as dt
import os
"""
print(str(dt.datetime.now()).split())
bookShelf = [{'Name':'SomeName', 'Author': 'SomeAuthor'}, {'Name':'SomeName1', 'Author': 'SomeAuthor1'}]
pickle.dump(bookShelf,open(os.getcwd()+"\\save.p","wb"))

copiedShelf = pickle.load(open(os.getcwd()+"\\save.p","rb"))
print(copiedShelf)



copiedUser = pickle.load(open(os.getcwd()+"\\user.p","rb"))
print(copiedUser)

a,b,c = (1,2,3)
print(a,b,c)
"""
bookCatalog = []
pickle.dump(bookCatalog,open(os.getcwd()+"\\books.p","wb"))

