from Lib import * 
from messages import * 
from User import* 
import locale
from dialog import Dialog
import sqlite3
import sys

"""
A list of functions to use for dialog main. This grouping of functions take advantage of the built-in 
Library Management system classes, methods and accessors. Dialog is a framework programmed with console 
TUI(Terminal User Interfaces) in mind, so many components of a interfacereuires being built from "empty 
shell", that is, as a programmer using dialog you are responsible for building windows, msg boxes, etc 
yourself. To interface with your application. Building functions to ease the process is much better and 
should help keep things organized. You'll notice that class use the name structure: "CREATE" and functions
use the name structure "BUILD". This way we can distinguish from the two and keep actions seperate. 
"""

def buildDialog():
    """
    Building a dialog application requires windowns(interfaces) to point
    to an object. In this case, the object in win. So every function that 
    deals with an interface must be passed win. Tags are also important, 
    these are the decision makers for iterating through different interface.
    There must also be a tag where any interface is being used in order to 
    operate on that interface. 
    """
    locale.setlocale(locale.LC_ALL, '')
    win = Dialog(dialog='dialog')
    win.set_background_title('The Home Library')
    code, tag = win.menu('LIBRARY SET-UP SCREEN', title = 'SET-UP', 
    choices = [('SET-UP', 'SET-UP LIBRARY'), 
    ('LOGIN', 'LOGIN CREDENTIALS')])
    return code, tag, win 




def buildSetupMessage(win): 
    """
    Set up procedures for the first time users begin with creating dialog objects
    (*View buildDialog()*), creating setup message objects to talkwith users, and 
    creating a user and their credentials
    """
    setup = Message()
    setupMessage = setup.sendSetupMessage()
    win.msgbox(setupMessage, height = 60, width = 90)


def getUserFirstNameLastName(win):
    """
    win must be passed to create inputbox windows. Returned is the user's first 
    and last name. This function is used to build the user's userName for system.
    """
    code, firstName = win.inputbox('Enter First Name: ', height = None, width = None)
    code, lastName = win.inputbox('Enter Last Name: ', height = None, width = None)
    return firstName, lastName


def buildUserName(firstName, lastName):
    """
    To Build a username, this function must receive the user's first and last name
    See class implementation in User.py. 
    """
    newUser = User(firstName, lastName)
    newUserLogin = newUser.createUserName()
    newUserFullname = newUser.assembleUserFullName()
    return newUser


def showLoginCredentials(win, newUser):
    # This function utilizes User class methods to show the user's new credentials 
    win.msgbox('      Welcome ' + newUser.getUserFullName() + '!\n'
               '\n      User Name : ' + newUser.getUserName(), height = None, width = 40)

def buildPassword(win, newUser): 
    code, password = win.inputbox('Enter Password: ', height = None, width = None)
    finalPassword = newUser.createPassword(newUser, password)
    return finalPassword

# attempting to verify password in dialog is bugged. I think its from not passing the username
# currently right now I'm passing newuser
def verifyNewPassword(win, newUser, finalPassword): 
    code, tryPassword = win.inputbox('Verify Password: ', height = None, width = None)
    passwordAttempt = newUser.verifyPassword(newUser, tryPassword)
    if(passwordAttempt == 'Correct password'):
            return win.msgbox('Successful Set-up!')

    attempts = 2
    while(passwordAttempt != 'Correct password' and attempts <= 3):
        code, tryPassword = win.inputbox(f'Verify Password (attempt{attempts}):', height = None, width = 45)
        passwordAttempt = newUser.verifyPassword(newUser, tryPassword)
        attempts += 1
        if(passwordAttempt == 'Correct password'): 
            return win.msgbox('Successful Set-up!')
    return win.msgbox('Please try again in 1 minute')







    
    

