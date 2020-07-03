import pickle
import os
import utils
import time

class bookShelf():
    """This is an abstract class that will provide functionalities for bookshelfmanagement"""

    def addBook(self):
        """This function will add books to the library catalog"""

        #Initialise the current book
        book = {"Serial_No": "", "Name": "", "Pages": "", "Category": "", "Author": "", "Price": "", "Publisher": "",\
                "Section": "", "Shelf no": "", "is_Here": "", "who has ?": " " }

        #get the catalog
        bookCatalog = pickle.load(open(os.getcwd() + "\\books.p", "rb"))

        #Construct the book details
        not_finished = True
        current_book = dict()
        while not_finished:

            for key in book:

                if key not in ["is_Here", "who has ?"]:
                    current_book[key] = str(input("Enter the {} of the book {}      :".format(key, "current value is " \
                        + current_book[key] if current_book[key] else "")))

                elif key == "is_Here":
                    incorrect_value = True

                    while incorrect_value:
                        response = str(input("Is the book here ? (Yes / No)    :")).strip()
                        if response.lower() not in ["yes", "no"]:
                            utils.printMenuHead("Invalid value, please correct")
                            print("Please choose either Yes or No")

                        else:
                            current_book[key] = response
                            incorrect_value = False

                else:
                    current_book[key] = str(input("Who has the book ?     :".format(key)))

                utils.printMenuHead("Review Details of the book")
                for key,value in book.items():
                    print(key,":",value)
                try:
                    incorrect_choice = True
                    while incorrect_choice:
                        choice = str(input("Do you want to update details? Yes / No?    :")).strip()
                        if choice.lower() not in ["yes", "no"]:
                            utils.printMenuHead("Invalid value, please correct")
                            print("Please choose either Yes or No")
                            time.sleep(2)

                        elif choice.lower() == "no":
                            incorrect_choice = False
                            not_finished = False

                        else:
                            incorrect_choice = False
                            self.addBook()

                except Exception:
                    print("Exception Occured")
                    return

                finally:
                    bookCatalog = bookCatalog + current_book
                    pickle.dump(bookCatalog, open(os.getcwd() + "\\books.p", "wb"))
                    utils.printMenuHead("Added book Successfully")
                    self.logger("Added the book {} Successfully".format(current_book["Name"]))















