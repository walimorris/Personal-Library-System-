#!/usr/bin/env python3

import locale 
from dialog import Dialog 
from Lib import * 
import sys 

def main(): 

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
        win.msgbox('Thank you for using The Home Library!')
        sys.exit(0)
    #submit new book
    elif tag == 'Submit Book':
        
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
    #search for book info 
    elif tag == 'Search Book':
        code, tag = win.menu('                 Search Library', 
                            choices = [('Search by Book Id #', '#####'), 
                                       ('Search by Title', 'Book title'), 
                                       ('Search by Author', 'Book Author')])
        if code == win.CANCEL: 
            win.msgbox('Thank you for using the home Library')
            sys.exit(0)
        if tag == 'Search by Book Id #': 
            code, bookId = win.inputbox('Enter Book Id #', height=None, width=None)
            results = searchById(bookId)
            win.msgbox(results, height=None, width=60)


if __name__ == '__main__': 
    main() 




        


    






