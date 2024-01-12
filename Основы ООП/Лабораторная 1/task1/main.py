# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Time:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.check(hours, minutes, seconds)
        self.give_more_minutes(minutes)
        """
        Класс, указывающий время (часы, минуты,секунды)
        
        :param hours: Указываем час
        :param minutes: Указываем количество минут
        :param hours: Указываем количество секунд

        """
        for i in [hours, minutes, seconds]:
            if not isinstance(i, int):
                raise ValueError
    def check(self, hours: int, minutes: int, seconds: int):
        if hours > 24:
            raise ValueError('В сутках не больше 24 часов!')
        if minutes > 59:
            raise ValueError('Можно указать только меньше 60 минут!')
        if seconds > 59:
            raise ValueError('Пожалуйста, укажите меньше 60 секунд')

    def give_more_minutes(self, minutes: int):
        minutes_to_add = int(input('Сколько минут добавить?'))
        self.minutes += minutes_to_add
        return minutes

class Giraffe:
    def __init__(self, height: int):

        if not isinstance(height, int):
            raise ValueError

        self.height = height
        self.count_neck_lenght(height)
    """
    Класс позволяет узнать длину шеи жирава по росту
    """
    def count_neck_lenght(self, height: int):
        neck_lenght = height // 3
        print(f'Рост жирафа:{height}, длина шеи: {neck_lenght}')

class Laptop:
    def __init__(self, price:int, color:str):
        self.price = price
        self.color = color
        self.check(price, color)
        self.possible_color(color)
        self.laptop_price(price)
    def check(self, price, color):
        if not isinstance(price, int):
            raise ValueError
        if not isinstance(color, str):
            raise ValueError
    def possible_color(self, color):
       self.list_color = ['черный', 'белый', 'синий', 'красный']
       if color in self.list_color:
          return color
       else:
          print('Выбирайте другой цвет')
    def laptop_price(self, price):
        if price <= 5000:
           price += 1000
           return price

a = Laptop(6000, 'black')
print(a.price())

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
