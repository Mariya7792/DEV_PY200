from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass1 = Glass(1, 5)
    glass2 = Glass(3, 6)
    print(glass1.occupied_volume)
    glass3 = Glass('ggsg', 2)
    print(glass3.capacity_volume)
    # TODO попробовать инициализировать не корректные объекты
