#!/usr/bin/env python 

import random

class Book(object):
    """ This class creates a book object that has in it the typical characteristics
    of a book. These attributes are hidden, but this is a fairly simple class with 
    a few short and simple methods to receive all the information a library owner
    should want to know about the books in their collection. The exception to this 
    is the createBookID() method that actually creates the books identification 
    number. This is important for library owners, who search for books by Id, as well 
    as record when a book is borrowed and returned. IDing the book allows for proficient
    tracking, recording, and printing of receipts. 
    
    """
    def __init__(self, title, author, publisher, publishDate, isb):
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__publishDate = publishDate
        self.__isb = isb

    def bookTitle(self):
        return self.__title

    def bookAuthor(self):
        return self.__author

    def bookPublisher(self):
        return self.__publisher

    def bookPublishDate(self):
        return self.__publishDate

    def bookIsb(self):
        return self.__isb
    
    def createBookId(self):
        bookIdNumber = 'HL' + str(random.randrange(1000,10000))
        return bookIdNumber

    def __str__(self):
        return f'Title:{self.__title}, Author:{self.__author}, Publisher:{self.__publisher}, \
                Publish date:{self.__publishDate}, ISB#:{self.__isb}'

def inputBookInfo1(title, author, publisher):
    """ This function allows the library owner to input information for one book.
    Returned will be all information relevant for sending to book object.

    """
    title = title
    author = author
    publisher = publisher
    return title, author, publisher

def inputBookInfo2(publishDate, isb):
    publishDate = publishDate
    isb = isb
    return publishDate, isb

def saveBook(libraryDictionary):
    """ This function is void and only acts to open the library file and append new
    books to the current library.

    """
    f = open("Library.txt", "a")
    f.write(str(libraryDictionary) + '\n')
    f.close()

def buildBook(book):
    """ Here, building the book means to take the attributes from the created book
    and format the book for storing.

    """
    title = book.bookTitle()
    auth = book.bookAuthor()
    pub = book.bookPublisher()
    pubDate = book.bookPublishDate()
    isb = book.bookIsb()
    return f'Title:{title}, Author:{auth}, Publisher:{pub}, Publish date:{pubDate}, ISB#:{isb}'

def addData(book, bookInfo):
    """ Adding the formatted bookbuild to the actual library dictionary and updating
    all new book entries.

    """
    libraryDictionary = {}
    bookId = book.createBookId()
    libraryDictionary.update({bookId:bookInfo})
    saveBook(libraryDictionary)

#Add search functions
def searchById(bookId):
    """ This option gives the ability for Library to search for books by the randomly generated
    Id numbers when the book is stored in the library. The library is search by matching the
    given book's indexed number(key). If the key is found, then the book will be returned.

    """
    book = {}
    f = open("Library.txt", "r")
    line = f.readline()
    while line != '':
        if line[2:8] == str(bookId):
            return line[1:-2]
            break
        line = f.readline()
    return 'Results Not Found'
    f.close()

def searchByTitle(bookTitle):
    """ This option gives the ability for Library to search for books by Title and this function 
    is simply passed a string containing the book title. If the title is matched to any book in 
    the Library, the results will be reported. For best results, the full title should be submitted.
    If multiple books contain the same word, then the results will report multiple books. This is okay
    for searching, as the menu allows for scroll and each book has a personal Id number.
    
    """
    book = {}
    f = open("Library.txt", "r")
    line = f.readline()
    while line != '':
        if bookTitle in line:
            return line[1:-2]
            break
        line = f.readline()
    return 'Results Not Found'
    f.close()

def searchByAuthor(bookAuthor):
    """

    """
    book = {}
    f = open("Library.txt", "r")
    line = f.readline()
    while line != '':
        if bookAuthor in line:
            return line[1:-2]
            break
        line = f.readline()
    return 'Results Not Found'
    f.close()

# deletion of books
def deleteBook(bookTitle):
    """

    """
    # There was a big, deleting all entries within the library: the bug was pretty simple. 
    # Rather than originally having lines = r.readlines(); it was line = r.readlines(). So, 
    # when this function was called, there was an error "lines was not defined". That was 
    # identified. Now, the new file isn't deleting the book entry. << *FIX* 
    r = open("Library.txt", "r")
    lines = r.readlines()
    w = open("Library.txt", "w")
    for line in lines:
        if line.rstrip('\n') != bookTitle:
            w.write(line)
    r.close()
    w.close()

			
