from Codes.Biblioteca.Book import Book
from Codes.Biblioteca.User import User
from Codes.Biblioteca.Library import Library

age = 0
list_user = Library()


while age != -1:
    print("Ingrese nombre")
    name_user = str(input(""))
    print("Ingrese edad:")
    age = int(input(""))
    print("Ingrese calle:")
    address = str(input(""))
    user = User(name_user, age, address)
    list_user.clients_append(user.view_user())
    #list_book = Library()
print(list_user.view_users())

#list_book = Library()
#user_2 = User("Maria",23,"Los Suaces 2121")
#user_3 = User("Pablo",28,"Los Suaces 2121")
#user_4 = User("Juana",21,"Los Suaces 2121")
#user_5 = User("Valentina",19,"Los Suaces 2121")
#user_6 = User("Nicolas",20,"Los Suaces 2121")
#user_7 = User("Alexis", 20,"Los Suaces 2121")
#user_8 = User("Facundo",19,"Los Suaces 2121")

#book_1 = Book("El secreto de sus ojos","Juan Carlos","$1200")
#book_2 = Book("Python constructor","Juan Carlos","$1800")
#book_3 = Book("El Ethernauta","Juan Carlos","$2000")
#book_4 = Book("Shingeki no Kjoyin","Juan Carlos","$2500")
#book_5 = Book("Crear o morir","Juan Carlos","$1000")
#book_6 = Book("Yo robot","Juan Carlos","$900")
#book_7 = Book("Tormenta de espadas","Darin","$1200")
#book_8 = Book("Fuego y Sangre","George RR Martin","$6000")

#print(user_1.view_name())
#print(book_1.view_title())

#list_user.clients_append(user_1.view_name())
#list_user.clients_append(user_2.view_name())
#list_user.clients_append(user_3.view_name())
#list_user.clients_append(user_4.view_name())
#list_user.clients_append(user_5.view_name())
#list_user.clients_append(user_6.view_name())
#list_user.clients_append(user_7.view_name())
#list_user.clients_append(user_8.view_name())

#list_book.books_append(book_1.view_title())
#list_book.books_append(book_2.view_title())
#list_book.books_append(book_3.view_title())
#list_book.books_append(book_4.view_title())
#list_book.books_append(book_5.view_title())
#list_book.books_append(book_6.view_title())
#list_book.books_append(book_7.view_title())
#list_book.books_append(book_8.view_title())


#print(list_user.view_users())
#print(list_book.view_books())