class Book:
    def __init__(self, name):
        self.name = name
        self.status = "Available"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, name):
        self.books.append(Book(name))
        print(name, "added")

    def borrow_book(self, name):
        for book in self.books:
            if book.name == name and book.status == "Available":
                book.status = "Borrowed"
                print(name, "borrowed")
                return
        print("Book not available")

    def return_book(self, name):
        for book in self.books:
            if book.name == name:
                book.status = "Available"
                print(name, "returned")
                return


library = Library()

library.add_book("Python")
library.add_book("Java")

library.borrow_book("Python")
library.return_book("Python")
