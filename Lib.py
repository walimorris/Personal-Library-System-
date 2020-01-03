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
    """ Continuation of the information needed to create a book, broken up over two 
    two functions. 
    
    """
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
    """ This option allows for the most proficient identification search for each book in 
    the library. This search matches a books identification number by taking the exact 
    index from a given book entry in the library. If the key is found then the book will 
    be returned.

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

def delSearchById(bookId):
    """ This function is essentially the same as the searchById() function, except this option 
    only searches for an individual book's identification number and matches it to the book 
    that's searched for deletion, without the more efficient indexing.

    """
    f = open("Library.txt", "r")
    line = f.readline()
    while line != '':
        if bookId in line:
            return line
            break
        line = f.readline()
    return 'Results Not Found'
    f.close()
	
def searchByTitle(bookTitle):
    """ Searching by title can be specific, but is mainly used to inquire a list of books that 
    may possibly be the book that's being searched. If for some reason, the full book title is 
    not known, a user can search what they know and receive a list of possible books they are 
    searching for. 
    
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
    """ Searching by Author is used when needing to know all books currently in
    collection from one specific author. By creating an empty dictionary, list 
    and string we can open the library and search specific words which will return 
    every line in our dictionary with that word. Be careful, searching for John can 
    return books by John Zelle, John Jacobs and John Adams. That's the nature of a 
    search. Those results will be appended to our searched Books list and then added
    to the results string that can be viewed from dialog. 

    """
    book = {}
    searchBooks = []
    searchResults = ''
    f = open("Library.txt", "r")
    line = f.readline()
    while line != '':
        if bookAuthor in line:
            searchBooks.append(line)
        line = f.readline()
    if searchBooks == []:
        return '{:*^55}'.format('Results Not Found')
    for i in range(len(searchBooks)):
        # Line below is a format line, searchBooks[i] is a long string so indexing 
        # here is allowed and let's us strip the dictionary '{}' braces. 
        searchResults += searchBooks[i][1:-2] + '\n'
    return searchResults
    f.close()

# deletion of books
def deleteBook(bookId):
    """ Deletion of books are triggered by recognition of each books personal identification 
    number. Recognizing a books four digit identification number is best due to this number 
    being one of a kind, there is no other number in the library like it. It seems to be 
    more proficient to open/read/close the library before opening the library again to update
    and delete the book of choice. 

    """
    d = open("Library.txt", "r")
    lines = d.readlines()
    d.close()
    f = open("Library.txt", "w")
    for line in lines:
        if not bookId in line:
            f.write(line)
    f.close()
