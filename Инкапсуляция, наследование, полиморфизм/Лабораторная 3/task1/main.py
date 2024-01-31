class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError('Введите верное название книги')
        if not isinstance(author, str):
            raise TypeError('Введите верное имя автора')

        self._name = name
        self._author = author
    @property
    def name(self):
        return self._name
    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise ValueError('Пожалуйста, укажите число')
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int):
            raise TypeError('Введите количество страниц')
        if self.pages <= 0:
            raise ValueError('Количество страниц больше 0')
        self._pages = pages

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Страницы {self._pages}. "

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook(Book):

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise ValueError('Пожалуйста, укажите число с точкой')
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, float):
            raise TypeError('Введите длительность')
        if duration <= 0:
            raise ValueError('Длительность книги больше 0')
        self._duration = duration

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Длительность {self._duration}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"


book1 = Book('1', 'Author')
book2 = PaperBook('2', 'Author_paper', 38)
book3 = AudioBook('3', 'Author_audio', 6.5)
print(book2.author)
print(book1.__str__())
print(book1.__repr__())
print(book2.__str__())
print(book2.__repr__())
print(book3.__str__())
print(book3.__repr__())

