class Book:
    def __init__(self,id ,title,author,quantity):
        self.id = id
        self.title = title
        self.author=author
        self.quantity = quantity

    def book_info(self):
        print("book info")
    
    def check_avalability(self):
        if self.quantity > 0:
            print("available")    
        else:
            print("not available")

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []   # empty list

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(f"{book.title} borrowed by {self.name}")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{book.title} returned by {self.name}")
        else:
            print("This book was not borrowed by this member.")

    def member_info(self):
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")
        print("Borrowed Books:")
        for book in self.borrowed_books:
            print("-", book.title)

class Library:
    def __init__(self):
        self.books = []        # stores Book objects
        self.members = []      # stores Member objects

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
              return book
        return None

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, book_id):
        book = self.find_book_by_id(book_id)
        member = self.find_member_by_id(member_id)

        if not book:
            print("Book not found")
            return

        if not member:
            print("Member not found")
            return

        if book.quantity > 0:
            book.quantity -= 1
            member.borrowed_books.append(book)
            print("Book borrowed successfully")
        else:
            print("Book out of stock")

    def return_book(self, member_id, book_id):
        book = self.find_book_by_id(book_id)
        member = self.find_member_by_id(member_id)

        if book and member and book in member.borrowed_books:
            book.quantity += 1
            member.borrowed_books.remove(book)
            print("Book returned successfully")
        else:
            print("Return failed")

        
if __name__ == "__main__":
    library = Library()

    # Create books
    book1 = Book(1, "Python Basics", "Ali", 3)
    book2 = Book(2, "OOP Guide", "Sara", 2)

    # Add books to library
    library.add_book(book1)
    library.add_book(book2)

    # Create member
    member1 = Member(101, "Ahmed")
    library.add_member(member1)

    # Borrow book
    library.borrow_book(101, 1)

    # Return book
    library.return_book(101, 1)

    Member.member_info()