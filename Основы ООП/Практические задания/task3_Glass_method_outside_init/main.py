from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        self.check(capacity_volume, occupied_volume)
        self.capacity(capacity_volume, occupied_volume)

    def check(self, capacity_volume, occupied_volume):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
    def capacity(self, capacity_volume, occupied_volume):
        if self.capacity_volume <= occupied_volume:
            raise ValueError

if __name__ == "__main__":
    glass1 = Glass(500, 600)

    print(glass1.capacity_volume)  # TODO распечатать атрибут capacity_volume
    print(glass1.occupied_volume)  # TODO распечатать атрибут occupied_volume
