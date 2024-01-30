import math


class Figure:
    """ Базовый класс. """

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None


class Rectangle(Figure):
    """ Производный класс. Прямоугольник. """
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        S = self.a * self.b
        print(f"Вызван метод класса {self.__class__.__name__}")

class Circle(Figure):
    """ Производный класс. Круг. """

    def __init__(self, a):
        self.a = a

    def area(self):
        S = self.a * 3.14
        print(f"Вызван метод класса {self.__class__.__name__}")


if __name__ == "__main__":
    fig = Figure()
    fig.area()

    rect = Rectangle(5, 10)
    rect.area()

    circle = Circle(5)
    circle.area()
