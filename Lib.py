"""
The Book Class is currently being replanned and reworked. It shouldn't take much 
to build a book, but currently going through all possible avenues of approach for
books. 
"""

class Book(object):

    def __init__(self, title, author, publisher, publishDate, isb):
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__publishDate = publishDate
        self.__isb = isb

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getPublisher(self):
        return self.publisher

    def getPublishDate(self):
        return self.publishDate

    def getIsb(self):
        return self.isb


    def __str__(self):
        return f'Title:{self.title}, Author:{self.author}, Publisher:{self.publisher}, \
                Publish date:{self.publishDate}, ISB#:{self.isb}'
