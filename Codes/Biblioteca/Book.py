
class Book:

    def __init__(self,title = '',author = '',price = ''):
        self.title = title
        self.author = author
        self.price = price

    #Formato

    def __str__(self):
        return f"Title:{self.title} - Author:{self.author} - Price:{self.price}"

    def view_book(self):
        return f"Title:{self.title} - Author:{self.author} - Price:{self.price}"

    def view_title(self):
        return f"{self.title}"
