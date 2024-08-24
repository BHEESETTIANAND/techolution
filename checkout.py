class CheckoutManager:
    def __init__(self, book_manager, user_manager):
        self.checkouts = []
        self.book_manager = book_manager
        self.user_manager = user_manager

    def checkout_book(self, user_id, isbn):
        user = self.user_manager.find_user_by_id(user_id)
        book = self.book_manager.find_book_by_isbn(isbn)
        
        if not user:
            print("User not found.")
            return
        
        if not book:
            print("Book not found.")
            return
        
        if not book.available:
            print("Book is already checked out.")
            return
        
        book.available = False
        self.checkouts.append({"user_id": user_id, "isbn": isbn})
        print(f"Book '{book.title}' checked out by {user.name}.")

    def return_book(self, isbn):
        book = self.book_manager.find_book_by_isbn(isbn)
        if not book:
            print("Book not found.")
            return
        
        if book.available:
            print("Book is not checked out.")
            return

        book.available = True
        print(f"Book '{book.title}' returned.")
