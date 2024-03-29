from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана

        if self.validate_occupied_volume(occupied_volume):
            self.occupied_volume = occupied_volume  # объем жидкости в стакане

    def validate_occupied_volume(self, occupied_volume):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        return True


if __name__ == "__main__":
    glass1 = Glass(200, -100)  # экземпляр класса
    print(glass1.capacity_volume, glass1.occupied_volume)

    glass2 = Glass(800, 500)
    print(glass2.capacity_volume, glass2.occupied_volume)

    print("Доливаем воды в первый стакан...")
    glass2.occupied_volume += 200
    print(glass1.capacity_volume, glass1.occupied_volume)
    print(glass2.capacity_volume, glass2.occupied_volume)
    print(id(glass1))
    print(id(glass2))
    #  TODO сравнить id объектов
