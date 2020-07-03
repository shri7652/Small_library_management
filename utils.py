import os

#Function to clear screen
def clear():

    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux
    else:
        _ = os.system('clear')

#Print Headers
def printMenuHead(header):
    clear()
    print("*******Welcome to Small Library Management - {} ******".format(header))










