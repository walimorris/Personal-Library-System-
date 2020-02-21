"""
The Message Class is solely for the purpose of author communication. 
All messages are written to help user's understand the purpose and ideas 
behind the Personal Library Management System. Messages may also have a 
few methods to help user/author communication.
"""

class Message: 
    
    def __init__(self): 
        self.__message = ""

    def sendSetupMessage(self): 
        self.message = """
        Welcome to the Personal Library Management System. I'm glad you're here.
        After a few different approaches to building this Library, unfortunately,
        I don't think It'll ever be entirely complete. Since the beginning of my
        stunt as a programmer, I've since been interested in understanding the
        fundamentals of systems. How they work, how data is processed, shared and
        used. Unsurprisingly, during this time Open Source software has also been
        a huge factor in software development. You can search almost anything you
        can imagine on the World Wide Web and learn almost anything there is to
        learn, provided you take the time with diligence, perserverence and care.
        The Personal Library Management System is a collection of your personal
        hard copy books, that is, the books in your real world home collection.
        As the fourth industrial revolution is underway, many hardcopy books will
        soon be a thing of the past. As a college student, I've barely brought any
        hard copy book required of my classes. Most times, I open my laptop and
        read what's on the virtual screen. Although this might be the case in the
        near future, your hard copy books are anything but a heavy paperweight.
        I've read a good handful of Computer Science books before the first year
        into my programming career and I've learned many things. From an authoring
        point of view I've learned that many computer scientist and programmers
        have a charming and nearly poetic way with words. Whether they're more 
        inclined to mathematics, language, or a pragmaticists point of view. One
        thing is for certain, programmers are keen authors, learners and thinkers.
        Whether you're a programmer or advid reader, I hope this virtual library
        collection is useful to you, for whatever reason you find. Building this
        program has helped me learn many things about the intricacies of systems,
        simple as this one may be.
        
        Thanks,
        
        Wali Morris
        """

        return self.message

