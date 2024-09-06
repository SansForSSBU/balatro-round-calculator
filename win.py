from enum import Enum

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
    ALL_RANKS = list(_VALUES.keys())

    def __init__(self, rank):
        if rank not in self._VALUES.keys():
            raise Exception("Invalid rank")
        self.rank = rank

    def get_chips(self):
        return self._VALUES[self.rank]

class Suit(Enum):
    SPADES = 0
    DIAMONDS = 1
    CLUBS = 2
    HEARTS = 3
Suit.ALL_SUITS = [Suit(x) for x in range(4)] # TODO: can we get rid of this magic number?

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

deck = []
for suit in Suit.ALL_SUITS:
    for rank in Rank.ALL_RANKS:
        deck.append(Card(suit, rank))

print(len(deck))
print(deck)