class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __repr__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({status})"

class Member:
    MAX_BORROWED_BOOKS = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.MAX_BORROWED_BOOKS:
            raise MemberLimitExceededException(f"{self.name} has already borrowed the maximum number of books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title}' is already borrowed.")

        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)

    def __repr__(self):
        return f"Member: {self.name}, Borrowed Books: {[book.title for book in self.borrowed_books]}"

class Library:
    def __init__(self):
        self.books = [
            Book("Game of Thrones", "G.R.R.M"),
            Book("The Lord Of The Rings", "J.R.R. Tolkien"),
            Book("The Little Prince", "Antoine de Saint-Exupéry"),
            Book("Pride and Prejudice", "Jane Austen"),
            Book("Jane Eyre", "Emily Bronte")
        ]
        self.members = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def add_member(self, name):
        self.members.append(Member(name))

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found in the library.")

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        raise ValueError(f"Member '{name}' not found.")

    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.return_book(book)

    def display_books(self):
        for book in self.books:
            print(book)

    def display_members(self):
        for member in self.members:
            print(member)

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Display Members")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            library.add_book(input("Enter book title: "), input("Enter book author: "))
            print("Book added successfully.")

        elif choice == '2':
            library.add_member(input("Enter member name: "))
            print("Member added successfully.")

        elif choice == '3':
            member_name = input("Enter member name: ")
            print("Available books:")
            library.display_books()
            try:
                book_title = input("Enter the book title to borrow: ")
                library.borrow_book(member_name, book_title)
                print("Book borrowed successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '4':
            member_name = input("Enter member name: ")
            print("Available books:")
            library.display_books()
            try:
                book_title = input("Enter the book title to return: ")
                library.return_book(member_name, book_title)
                print("Book returned successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '5':
            library.display_books()

        elif choice == '6':
            library.display_members()

        elif choice == '7':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()