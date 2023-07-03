"""Representation of poker cards."""


class Card(object):
    RANKS = dict(reversed(e) for e in enumerate(
                 '2 3 4 5 6 7 8 9 T J Q K A'.split()))
    RANKS = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
    }
    SUITS = set('scdh')

    def __init__(self, card_spec):
        rank, suit = card_spec
        assert rank in self.RANKS
        assert suit in self.SUITS
        self.rank = rank
        self.suit = suit

    def score(self):
        return self.RANKS[self.rank]

    def __eq__(self, other_card):
        return (self.score() == other_card.score())

    def __lt__(self, other_card):
        return (self.score() < other_card.score())

    def __repr__(self):
        return '%s("%s%s")' % (self.__class__.__name__, self.rank, self.suit)

