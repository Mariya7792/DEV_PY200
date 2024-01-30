class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Страницы {self.pages}. "
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        self.name = name
        self.author = author
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Длительность {self.duration}."
    def __repr__(self):
        return super().__repr__()


book1 = Book('OOO', 'Author')
book2 = PaperBook('FFF', 'Author_paper', 38)
book3 = AudioBook('ZZZ', 'Author-audio', 6)
print(book1.__str__())
print(book1.__repr__())
print(book2.__str__())
print(book2.__repr__())
print(book3.__str__())
print(book3.__repr__())