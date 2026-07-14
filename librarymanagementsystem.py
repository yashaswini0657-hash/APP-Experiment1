class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self):
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        self.books.append(book)

        print("Book Added Successfully!\n")

    def register_patron(self):
        patron_id = int(input("Enter Patron ID: "))
        name = input("Enter Patron Name: ")

        patron = Patron(patron_id, name)
        self.patrons.append(patron)

        print("Patron Registered Successfully!\n")

    def display_books(self):
        print("\nBook List")

        if len(self.books) == 0:
            print("No Books Available")
        else:
            for book in self.books:
                status = "Available" if book.available else "Borrowed"
                print(book.book_id, book.title, book.author, status)

    # Borrow Book
    def borrow_book(self):
        book_id = int(input("Enter Book ID to Borrow: "))

        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book Borrowed Successfully!\n")
                else:
                    print("Book is Already Borrowed!\n")
                return

        print("Book Not Found!\n")

    # Return Book
    def return_book(self):
        book_id = int(input("Enter Book ID to Return: "))

        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print("Book Returned Successfully!\n")
                else:
                    print("Book was not Borrowed!\n")
                return

        print("Book Not Found!\n")



library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Display Books")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        library.add_book()

    elif choice == 2:
        library.register_patron()

    elif choice == 3:
        library.display_books()

    elif choice == 4:
        library.borrow_book()

    elif choice == 5:
        library.return_book()

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")