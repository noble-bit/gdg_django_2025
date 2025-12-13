class Library:
    def __init__(self):
        self.books = []  
    
    def add_book(self, book_title):
        self.books.append(book_title)
        print(f"Added: {book_title}")
    
    def show_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")


lib = Library()


lib.add_book("Book1")
lib.add_book("Book2")
lib.add_book("Book3")


print()  
lib.show_books()


print("\n--- Testing empty library ---")
empty_lib = Library()
empty_lib.show_books()