import hashlib
import os 

""" 
This file contains the User class, meant for building a user in the Library Management 
System. User's will have a distinct user name and protected password. Users can only 
have one account, although many users can be associated with one or many libraries.

"""

class User(object): 
    
    def __init__(self, firstName, lastName):
        """
        Creating a user involves receiving the user's first name and last name. 
        Passwords and accounts will be created there after
        """
        self.__firstName = firstName
        self.__lastName = lastName

    def assembleUserFullName(self):
        """
        This mutator method assembles a string of the user's fullname which will 
        be useful in many situations addressing the user. 
        """
        self.fullName = self.__firstName.capitalize() + " " + self.__lastName.capitalize()

    def getUserFullName(self): 
        """ 
        A accessor method to return the user's fullname
        """
        return f'{self.fullName}'
         

    def createUser(self): 
        """
        Creating a username is fast and easy. Generally a user name is first five
        letters of user's lastname plus users first initial. 
        """
        self.userName = self.__lastName[0:6].lower() + self.__firstName[0].upper()

    def getUserName(self): 
        """ 
        An accessor method to return the created username. This will come in 
        use for the administrator class and applying user's to various libraries
        """
        return f'{self.userName}'

    def createPassword(self, userName, password): 
        """
        passwords should be secure and only available for administrator purposes. 
        Changing passwords and recovering passwords etc. 
        """
        self.users = {} # hold users
        self.userName = userName
        # Dialog will provide an input box for creating a password, Field 1: Creating new password for user  
        self.password = password
        self.salt = os.urandom(32) # A new salt for this user
        self.key = hashlib.pbkdf2_hmac('sha256', self.password.encode('utf-8'), self.salt, 100000)
        self.users[self.userName] = {'salt': self.salt, 'key': self.key}

    def verifyPassword(self, userName, verifiedPassword): 
        """
        Passwords should be verified by Dialog before allowing a user to create a new 
        password as well as logging into an account. This is a action, so a response 
        is do. If password matches "correct password" will be returned. If password
        does not match "incorrect password" will be returned
        """
        self.userName = userName # ensure user is this user

        # get the user's password which contains salt and key 
        password = self.password 
        self.verifiedPassword = verifiedPassword
        salt = self.users[self.userName]['salt'] # get the salt 
        key = self.users[self.userName]['key'] # get the correct key
        new_key = hashlib.pbkdf2_hmac('sha256', self.verifiedPassword.encode('utf-8'), self.salt, 100000) # get attempted password key 
        if(key == new_key): 
            self.verifiedPassword = self.password # if keys match, password is a match
            match = 'Correct password'
            return f'{match}' # return match 
        else: 
            incorrect = 'Incorrect password' 
            return f'{incorrect}' # if passwords don't match inform the user 






        




