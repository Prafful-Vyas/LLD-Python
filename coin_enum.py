from enum import Enum


class Coin(Enum):
    PENNY = 1
    NICKEL = 5
    DIME = 10
    QUARTER = 25

    def __init__(self, value):
        self.coin_value = value

    def get_value(self):
        return self.coin_value


if __name__ == "__main__":
    total = Coin.DIME.get_value() + Coin.QUARTER.get_value()
