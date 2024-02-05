# Task Nr.1:

# Create a class called Product that takes a name and price as parameters and has __str__ and __repr__ methods defined.

# The __str__ method should return a string in the format "Product: name, Price: price"
# The __repr__ method should return a string in the format "Product('name', price)"


# class Product:
#     def __init__(self, name: str, price: float) -> None:
#         self.name = name
#         self.price = price

#     def __str__(self) -> str:
#         return f"Product: {self.name}, Price: {self.price}"

#     def __repr__(self) -> str:
#         return f"Product('{self.name}', {self.price})"


# product = Product("Apple", 0.49)

# print(product)
# print(repr(product))


# Task Nr.2:

# Create a class called MyQueue that has __bool__, __repr__ and __len__ methods defined.

# The __bool__ method should return True if the queue has any items and False if it is empty.
# The __repr__ method should return a string in the format MyQueue(items) where items is the list of items in the queue.
# The __len__ method should return the number of items in the queue.


# class MyQueue:
#     def __init__(self, items) -> None:
#         self.items = items

#     def __bool__(self):
#         return bool(self.items)

#     def __repr__(self) -> str:
#         return f"MyQueue({self.items})"

#     def __len__(self) -> int:
#         return len(self.items)


# item = MyQueue([1, 2, 3])

# print(bool(item))
# print(item)
# print(len(item))


# Task Nr.3:

# Create a class called Book that takes title, author, and ISBN as parameters. The class should have __bool__, __repr__, __len__, __str__, __eq__, __add__, and __getitem__ methods defined.

# The __bool__ method should return True if the book has a title, False otherwise.
# The __repr__ method should return a string in the format "Book(title, author, ISBN)" where title, author and ISBN are the respective attributes of the class
# The __len__ method should return the number of pages of the book
# The __str__ method should return a string in the format "title by author (ISBN)"
# The __eq__ method should compare two books and return True if both ISBN are the same and False otherwise.
# The __add__ method should add two books and return a new book object that contains the contents of both books concatenated and the title of the new book should be the title of the first book
# The __getitem__ method should return the title of the book if the index passed is 0, and the author of the book if the index passed is 1.


class Book:
    def __init__(
        self, title: str, author: str, isbn: str, content: str, pages: int
    ) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.content = content
        self.pages = pages

    def __bool__(self):
        return bool(self.title)

    def __repr__(self) -> str:
        return f"Book({self.title}, {self.author}, {self.isbn})"

    def __len__(self: int) -> int:
        x = []
        for _ in range(self.pages):
            x.append(1)
        return len(x)

    def __str__(self) -> str:
        return f"{self.title} by {self.author} ({self.isbn})"

    def __eq__(self, other: "Book") -> bool:
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return False

    def __add__(self, other: "Book") -> "Book":
        if isinstance(other, Book):
            return Book(self.content + other.content, self.title)
        raise TypeError(
            "unsupported operand type(s) for +: 'Book' and '{}'".format(
                type(other).__name__
            )
        )

    def __getitem__(self, index) -> None:
        if index == 0:
            return self.title
        elif index == 1:
            return self.author
        else:
            "Index should be 0 or 1"


book1 = Book(
    title="Don Quixote",
    author="Miguel de Cervantes",
    isbn="5464 6465 6467 1387",
    content="ladijgeoigjhgoijwhoi",
    pages=465,
)

book2 = Book(
    title="The Alchemist",
    author="Paulo Coelho",
    isbn="5324 6456 4267 7915",
    content="ladtrhwhethheheeer",
    pages=418,
)

print(bool(book1))
print(repr(book1))
print(len((book1)))
print(book1)
print(book1 == book2)
# book3 = book1 + book2
print(book1[1])
