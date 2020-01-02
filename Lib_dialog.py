#!/usr/bin/env python3

import locale
from dialog import Dialog
from Lib import *
import sys

def main():

    while True:
        locale.setlocale(locale.LC_ALL, '')
        win = Dialog(dialog='dialog')
        win.set_background_title("The Home Library")

        """ In a dialog menu setting, there may be mutilple "action" options. For instance, 
        in a yesno window object, if a user selects yes this is equivalent to win.OK or 'ok' 
        which allows for carry on actions to a new window or series of action windows after. 
        Selecting Cancel is equivalent to win.CANCEL which cancels an action all together. 
        This is used to build a dialog setting, creating a series of dialog boxes to complete
        a single program. 
    
        """
        code, tag = win.menu('      Welcome to your personalized Library',
                            title='The Home Library',
                            choices=[('Submit Book', 'Add to Library'),
                                     ('Search Book', 'Enter book information'),
                                     ('Delete Book', 'Delete book from Library')])

        """ It should be noted that the variable 'code' above references the dialog action to 
        for the menu window within the program, which shows that this feature allows for 
        event based programming, creating a series of windows dependent on user interaction. 

        """
        if code == win.CANCEL:
            win.msgbox("  ****Thank You for using the Home Library System****\n"
                       "\nThis software is free to use for anyone willing to build their "
                       "very own home library. This product was built with Python3, dialog, "
                       "and Ubuntu 18.04. The Home Library can be changed or modified and is "
                       "completely open source. The Home Library is solely for "
                       "individual safe keeping. We understand the importance of knowledge and "
                       "passing it on, books are a significant form of knowledge and this knowledge "
                       "should be stored and easily retrievable. The Home Library is an on-going personal "
                       "project by Wali Morris, who hopes to make a small impact through technology."
                       , height=30, width=60)
            sys.exit(0)

        # Submit new book option
        while tag == 'Submit Book':

            """ Written responses to input boxes can be passed to functions. Please see Lib.py for 
            function definitions. Submitting a book requires the user to input the book information, 
            which is broken up into two different functions but still creates the information for one 
            complete book object passed to the Book class. The book data is then created and stored 
            within the Library collection. The Library is stored in a single file called Library.txt. 
            This file should not be deleted, and more protection is given to this file to stop any 
            accidental deletion. The user will be asked to continue submitting books until canceled. 
            When auto widget is disabled, the default size (None) for input and msg boxes are height=10,
            width=30. If a larger text box is required you should assign their values.  
        
            """
            code, title = win.inputbox('Enter Title', height=None, width=None)
            code, author = win.inputbox('Enter Author', height=None, width=None)
            code, publisher = win.inputbox('Enter Publisher', height=None, width=None)
            code, publishDate = win.inputbox('Enter Publish date', height=None, width=None)
            code, isb = win.inputbox('Enter ISB #', height=None, width=None)
            title, author, publisher = inputBookInfo1(title,author,publisher)
            publishDate, isb = inputBookInfo2(publishDate, isb)
            book = Book(title, author, publisher, publishDate, isb)
            bookInfo = buildBook(book)
            addData(book, bookInfo)
            # Is there another book to submit?
            submitMore = win.yesno('Submit another book?', height=None, width=None)
            if submitMore == win.CANCEL:
                break
            else:
                tag = 'Submit Book'

        # Search for book option 
        while tag == 'Search Book':

            """ There are currently three ways to search for a book: By its personal Identification 
            number, title and author. Identification numbers are auto generated when a user submits 
            a new book to the overall library collection. ID numbers start with HL(Home Library). 
            Using the identification number is the most proficient and all other options will be 
            continually upgraded for the best proficiency, although they are all viable options. 
            
            """
            code, tag = win.menu('                 Search Library',
                                choices = [('Search by Book Id #', '#####'),
                                           ('Search by Title', 'Book title'),
                                           ('Search by Author', 'Book Author')])

            if tag == 'Search by Book Id #':
                code, bookId = win.inputbox('Enter Book Id #', height=None, width=None)
                results = searchById(bookId)
                win.msgbox(results, height=None, width=60)
            if tag == 'Search by Title':
                code, bookTitle = win.inputbox('Enter Book Title', height=None, width=None)
                results = searchByTitle(bookTitle)
                win.msgbox(results, height=None, width=60)
            if tag == 'Search by Author':
                code, bookAuthor = win.inputbox('Enter Book Author', height=None, width=None)
                results = searchByAuthor(bookAuthor)
                win.msgbox(results, height=None, width=60)
            # is there another book to search?
            searchMore = win.yesno('Search another book?', height=None, width=None)
            if searchMore == win.CANCEL:
                break
            else:
                tag = 'Search Book'

        #delete a book
        while tag == 'Delete Book':
            
            """ Deleting a book from the library collection is a pretty serious action. Once a book is 
            deleted, you can not undue this. A book can be resubmitted into the library, but it's 
            gone forever until then. Confirmation boxes are initiated well before any permanent action 
            is taken. Deleting books are also done by submitting its personal ID number, this way there's 
            no confusion to which book should be deleted. 

            """
            code, tag = win.menu('             Delete a Book from Library',
                                choices = [('Delete by ID', 'Enter book ID#')])

            #if code is cancelled from Delete Menu
            if code == win.CANCEL:
                break
            if tag == 'Delete by ID':
                code, bookId = win.inputbox('Enter book ID#', height=None, width=None)
                if code == win.CANCEL:
                    break
                confirm = searchById(bookId)
            if confirm == 'Results Not Found':
                win.msgbox(confirm, height=None, width=None)
            else:
                code = win.yesno('Are you sure you want to delete:' + '\n' + confirm, height=None, width=60)
                if code == win.OK:
                    deleteBook(confirm)
                    win.msgbox('DELETED!' + '\n' + confirm, height=None, width=None)
                else:
                    win.msgbox("Book Retained!", height=None, width=None)

            deleteAnother = win.yesno('Delete another book?', height=None, width=None)
            if deleteAnother == win.CANCEL:
                break
            else:
                tag = 'Delete Book'

if __name__ == '__main__':
    main()





        


    






