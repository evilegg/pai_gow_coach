"""Representation of poker cards."""


class Card(object):
    RANKS = dict(reversed(e) for e in enumerate(
                 '2 3 4 5 6 7 8 9 T J Q K A'.split()))

    def __init__(self, card_spec):
        rank, suit = card_spec
        assert rank in self.RANKS
        self.rank = self.RANKS[rank]
        self.suit = suit
        self._raw_rank = rank

    def __cmp__(self, other):
        return cmp(self.rank, other.rank)

    def __repr__(self):
        return '%s("%s%s")' % (self.__class__.__name__,
                               self._raw_rank,
                               self.suit)

