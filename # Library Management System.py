# Library Management System
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn   # private attribute
        self.available = True

    # Getter and Setter for ISBN
    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn

    def display_info(self):
        status = "Available" if self.available else "Not Available"
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.__isbn}, Status: {status}")


class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.__membership_id = membership_id   # private attribute
        self.borrowed_books = []

    # Getter and Setter for membership_id
    def get_membership_id(self):
        return self.__membership_id

    def set_membership_id(self, new_id):
        self.__membership_id = new_id

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")


class StaffMember(Member):
    def __init__(self, name, membership_id, staff_id):
        super().__init__(name, membership_id)
        self.staff_id = staff_id

    def add_book(self, library, book):
        library.books.append(book)
        print(f"Staff {self.name} added '{book.title}' to the library.")


class Library:
    def __init__(self):
        self.books = []

    def display_all_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                book.display_info()


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    # Create Library
    library = Library()

    # Create some Books
    b1 = Book("1984", "George Orwell", "12345")
    b2 = Book("To Kill a Mockingbird", "Harper Lee", "67890")

    # Create Members
    m1 = Member("John", "M001")
    s1 = StaffMember("Emily", "S001", "STF01")

    # Staff adds books to the library
    s1.add_book(library, b1)
    s1.add_book(library, b2)

    print("\n📚 All Books in Library:")
    library.display_all_books()

    print("\n🔹 Borrow & Return Example:")
    m1.borrow_book(b1)
    m1.borrow_book(b1)  # Try to borrow same book again
    m1.return_book(b1)

    print("\n📚 After Transactions:")
    library.display_all_books()