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

        """ In a dialog menu setting, there are two options of 'OK' and 'Cancel'. Here the 
        variable 'code' acts as the response to the instance of menu window. If a user 
        selects ok or cancel you can dictate what comes next. Tag is the choices given 
        with in the menu window. If a user presses enter on a tag, show in the menu window,
        you can further initiate decisions and what comes next.
    
        """
        code, tag = win.menu('      Welcome to your personalized Library',
                            title='The Home Library',
                            choices=[('Submit Book', 'Add to Library'),
                                     ('Search Book', 'Enter book information'),
                                     ('tag 3------', 'Item text-------------')])
        if code == win.CANCEL:
            win.msgbox("The software is free to use for anyone willing to build their "
                       "very own home library. This product was built with Python3, dialog, "
                       "and Ubuntu 18.04. The Home Library can be changed or modified and is "
                       "completely open source, given proper annoucement of its original author "
                       "and purpose.The goal with The Home Library is solely for individual safe "
                       "keeping. We understand the importance of knowledge and passing it on, "
                       "books are a significant form of knowledge and this knowledge should be "
                       "stored and easily retrievable. The Home Library is an on-going personal "
                       "project by Wali Morris, who hopes to make a small impact on the world, "
                       "especially to those less fortunate, by making Knowledge easily accessible "
                       "to families. The open source community and spirit keeps this idea alive, "
                       "which helped this author learn a very small portion of technology. It is "
                       "in hopes, even as an individual, that The Home Library can be useful to you "
                       "and your families, to collect, retrieve, and pass on knowledge to future "
                       "generations. Thank you to the open source community and to you for passing "
                       "on this sweet sweet knowledge!", height=30, width=60)
            sys.exit(0)
        #submit new book
        while tag == 'Submit Book':

            """ The written responses in input boxes can be passed to functions, as you see here
            title, author, publisher, publishDate, isb is being passed to the InputBookInfo()
            functions which carries over to the creation of the book object. When auto widget 
            is disabled, the default size (None) for input and msg boxes are height=10, width=30.
            
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
            #Is there another book to submit?
            code = win.yesno('Submit another book?', height=None, width=None)
            if code == win.CANCEL:
                break
        #search for book info 
        while tag == 'Search Book':
            code, tag = win.menu('                 Search Library',
                                choices = [('Search by Book Id #', '#####'),
                                           ('Search by Title', 'Book title'),
                                           ('Search by Author', 'Book Author')])

            # If code is cancelled from Search Win                    
            if code == win.CANCEL:
                break
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
            code = win.yesno('Search another book?', height=None, width=None)
            if code == win.CANCEL:
                break
        #delete a book
        while tag == 'Delete Book':
            code, tag = win.menu('             Delete a Book from Library',
                                choices = [('Delete by Title', 'Enter book title')])

            #if code is cancelled from Delete win
            if code == win.CANCEL:
                break
            if tag == 'Delete by Title':
                code, bookTitle = win.inputbox('Enter book title', height=None, width=None)
                confirm = searchByTitle(bookTitle)
                code = win.yesno('Are you sure you want to delete:' + '\n' + confirm, height=None, width=60)
                if code == win.OK:
                    deleteBook(confirm)
                    win.msgbox('DELETED!' + '\n' + confirm, height=None, width=None)
                else:
                    win.msgbox('Book retained...', height=None, width=None)
            code = win.yesno('Delete another book?', height=None, width=None)
            if code == win.CANCEL:
                break


if __name__ == '__main__':
    main()




        


    






