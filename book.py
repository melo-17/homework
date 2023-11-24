class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year of Publication: {self.year}, Number of Pages: {self.pages}"

    def change_pages(self, new_pages):
        self.pages = new_pages

    def __str__(self):
        return self.display_info()


book1 = Book("The hound of the Baskervilles", "Sir Arthur Conan Doyle", 1902, 200)
book2 = Book("1984", "George Orwell", 1949, 328)


print(book1.display_info())
print(book2.display_info())

book1.change_pages(282)
print(book1.display_info())


