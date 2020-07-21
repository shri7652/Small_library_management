import pickle
import os
import utils
import time

class bookShelf():
    """This is an abstract class that will provide functionalities for bookshelfmanagement"""

    def addBook(self):
        """This function will add books to the library catalog"""
        print("In addBook")
        utils.printMenuHead("Add New Book")
        #Initialise the current book
        book = {"Serial_No": "", "Name": "", "Pages": "", "Category": "", "Author": "", "Price": "", "Publisher": "",\
                "Section": "", "Shelf no": "", "is_Here": "", "who has ?": " " }

        #get the catalog
        bookCatalog = pickle.load(open(os.getcwd() + "/books.p", "rb"))
        print(bookCatalog)

        name = str(input("Enter new book name :")).strip().lower()
        check_existing_book = [bookDict['Name'] for bookDict in bookCatalog if bookDict['Name'] == name]
        if check_existing_book:
            utils.printMenuHead("Book Already Exists")
            print("Book Already exists !!!!")
            time.sleep(3)
            self.logger("Tried to add book {} but it already exists".format(book))
            return None
        else:
            serial_no = str(input("Enter serial number :")).strip().lower()
            check_existing_serial = [bookDict['Serial_no'] for bookDict in bookCatalog if bookDict['Serial_no'] == serial_No]
            if check_existing_serial:
                utils.printMenuHead("Book Serial number already Exists")
                print("Book serial number already exists, please enter new serial number !!!!")
                serial_No = str(input("Enter serial number :")).strip().lower()

            pages = str(input("Enter number of pages :")).strip().lower()
            category = str(input("Enter book category :")).strip().lower()
            author = str(input("Enter book's author :")).strip().lower()
            price = str(input("Enter price of the book :")).strip().lower()
            publisher = str(input("Enter name of publisher :")).strip().lower()
            section = str(input("Enter new of the section :")).strip().lower()
            shelf_no = str(input("Enter book shelf number:")).strip().lower()

            is_here = str(input("Is the book here? (Yes/No) :")).strip().lower()
            while is_here not in ['yes', 'no']:
                utils.printMenuHead("invalid value")
                is_here = str(input("Is the book here? (Yes/No) :")).strip()

            who_has = str(input("Enter the personal who has the book name :")).strip().lower()

        print("*****Verify Addition*****")
        print("Name of book:          ",name)
        print("Serial# of book:       ",serial_no)
        print("Number of pages:       ",pages)
        print("Book category:         ",category)
        print("Book's author:         ",author)
        print("Price of the book:     ",price)
        print("Publisher of the book: ", publisher)
        print("Section of the book:   ",section)
        print("Book shelf number:     ",shelf_no)
        print("Is the book here:      ",is_here)
        print("Who has the book:      ",who_has)
        print()
        add_cnf = input("Confirm addition?(y/n)").strip().lower()
        if add_cnf == 'y':
            bookCatalog = bookCatalog + [{"Serial_No": serial_no, "Name": name, "Pages": pages, "Category": category, "Author": author, "Price": price, "Publisher": publisher,\
                    "Section": section, "Shelf no": shelf_no, "is_Here": is_here, "who has ?": who_has }]
            pickle.dump(bookCatalog,open(os.getcwd()+"/book.p","wb"))

            utils.printMenuHead("Added book Successfully")
            self.logger("Added the book {} Successfully".format(name))
        else:
            print("Enter values again")
        #not_finished = True
        #current_book = dict()
        #while not_finished:

#            for key in book:

#                if key not in ["is_Here", "who has ?"]:
#                    current_book[key] = str(input("Enter the {} of the book {}      :".format(key, "current value is " \
#                        + current_book[key] if current_book[key] else "")))

#                elif key == "is_Here":
#                    incorrect_value = True

#                    while incorrect_value:
#                        response = str(input("Is the book here ? (Yes / No)    :")).strip()
#                        if response.lower() not in ["yes", "no"]:
#                            utils.printMenuHead("Invalid value, please correct")
#                            print("Please choose either Yes or No")

#                        else:
#                            current_book[key] = response
#                            incorrect_value = False

#                else:
#                    current_book[key] = str(input("Who has the book ?     :".format(key)))

#                utils.printMenuHead("Review Details of the book")
#                for key,value in book.items():
#                    print(key,":",value)
#                try:
#                    incorrect_choice = True
#                    while incorrect_choice:
#                        choice = str(input("Do you want to update details? Yes / No?    :")).strip()
#                        if choice.lower() not in ["yes", "no"]:
#                            utils.printMenuHead("Invalid value, please correct")
#                            print("Please choose either Yes or No")
#                            time.sleep(2)

#                        elif choice.lower() == "no":
#                            incorrect_choice = False
#                            not_finished = False

#                        else:
#                            incorrect_choice = False
#                            self.addBook()

#                except Exception:
#                    print("Exception Occured")
#                    return

#                finally:
#                    bookCatalog = bookCatalog + current_book
#                    pickle.dump(bookCatalog, open(os.getcwd() + "/books.p", "wb"))
#                    utils.printMenuHead("Added book Successfully")
#                    self.logger("Added the book {} Successfully".format(current_book["Name"]))















