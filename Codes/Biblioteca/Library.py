class Library:
    #user = User()
    #book = Book()
    def __init__(self):
        self.book_list = []
        self.user_list = []

    def books_append(self,book):
        self.book_list.append(str(book))

    def clients_append(self,user):
        self.user_list.append(str(user))

    def view_books(self):
        return self.book_list


    def view_users(self):
        return self.user_list