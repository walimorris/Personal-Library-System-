from Lib import * 
from messages import *
from User import * 
import locale
from dialog import Dialog 
import sys



def main(): 

    while True: 
        # Begins application and setup procedures
        locale.setlocale(locale.LC_ALL, '')
        win = Dialog(dialog='dialog')
        win.set_background_title('The Home Library')

        code, tag = win.menu('LIBRARY SET-UP SCREEN', 
                              title = 'SET-UP', 
                              choices = [('SET-UP', 'SET-UP LIBRARY'), 
                                         ('LOGIN', 'LOGIN CREDENTIALS')])

        if tag == 'SET-UP': 
            """
            Set up procedures for first time users begin with creating dialog objects. 
            Creating setup message objects. Creating User and credentials. 
            """
            setup = Message()
            setupMessage = setup.sendSetupMessage()
            win.msgbox(setupMessage, height = 60, width = 90)
            code, firstName = win.inputbox('Enter First Name', height = None, width = None)
            code, lastName = win.inputbox('Enter Last Name', height = None, width = None)
            
            # With the information above, create the user and assemble their name
            newUser = User(firstName, lastName)
            newUser.createUser()
            newUser.assembleUserFullName()

            # new user has been created. It's time to generate a password 
            newUserName = newUser.getUserName()
            win.msgbox('    Welcome ' + newUser.getUserFullName() + '!')


        if code == win.CANCEL: 
            sys.exit(0)


if __name__ == '__main__': 
    main()
