from Lib import * 
from messages import *
from User import *
from dialogFunctions import * 
import locale
from dialog import Dialog
import sqlite3
import sys



def main(): 

    while True: 
        # Begins application and setup procedures
        tag, win = buildDialog()

        if tag == 'SET-UP': 
            """
            Set up procedures for first time users begin with creating dialog objects. 
            Creating setup message objects. Creating User and credentials. 
            """
            buildSetupMessage(win)
            firstName, lastName = getUserFirstNameLastName(win)
            
            # With the information above, create the user and assemble their name
            newUser = buildUserName(firstName, lastName)

            # new user has been created. Show login credentials 
            showLoginCredentials(win, newUser)

            # It's time to create a password and authenticate it





        if code == win.CANCEL: 
            sys.exit(0)


if __name__ == '__main__': 
    main()
