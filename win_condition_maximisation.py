import enum

class Rank():
    _VALUES = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 11
    }
    _POSSIBILITIES = list(_VALUES.keys())
    def get_possibilities(self):
        return self._VALUES

    def __init__(self, rank):
        self.rank = rank

    def get_chips(self):
        return self._VALUES[self.rank]
    
class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

Rank.get_possibilities()

print("Hello")