import os

    #Print Headers
def printMenuHead(header):
    print("*******Welcome to Small Library Management - {} ******".format(header))

#Function to clear screen
def clear():

    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux
    else:
        _ = os.system('clear')








