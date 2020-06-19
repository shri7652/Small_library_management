import pickle
import datetime as dt
import os

print(str(dt.datetime.now()).split())
bookShelf = [{'Name':'SomeName', 'Author': 'SomeAuthor'}, {'Name':'SomeName1', 'Author': 'SomeAuthor1'}]
pickle.dump(bookShelf,open(os.getcwd()+"\\save.p","wb"))

copiedShelf = pickle.load(open(os.getcwd()+"\\save.p","rb"))
print(copiedShelf)