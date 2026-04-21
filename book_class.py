class Book:
    def __init__(
        self, title: str, author: str, isbn: str, isAvailable: bool = True
    ) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.isAvailable = isAvailable

    def borrow_book(self) -> bool:
        if self.isAvailable is False:
            return False
        else:
            self.isAvailable = False
            return True

    def return_book(self) -> bool:
        if self.isAvailable is True:
            return False
        else:
            self.isAvailable = True
            return True

    def display_info(self) -> None:
        common = f"{self.title} by {self.author} (ISBN: {self.isbn} - "
        if self.isAvailable is True:
            display = common + "Available"
            print(display)
        else:
            display = common + "Borrowed"
            print(display)


if __name__ == "__main__":
    book = Book("The Pragmatic Programmer", "David Thomas", "978-0135957059")
    book.display_info()

    success = book.borrow_book()
    print(f"Borrow successful: {str(success).lower()}")
    book.display_info()

    success = book.borrow_book()
    print(f"Borrow successful: {str(success).lower()}")

    book.return_book()
    book.display_info()
