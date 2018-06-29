"""Cards module for playing poker."""

HIGH_CARD      = 1
PAIR           = 1 << 1
TWO_PAIR       = 1 << 2
THREE_OFA_KIND = 1 << 3
STRAIGHT       = 1 << 4
FLUSH          = 1 << 5
FULL_HOUSE     = 1 << 6
FOUR_OFA_KIND  = 1 << 7
STRAIGHT_FLUSH = 1 << 8


class Card(object):
    RANKS = dict(reversed(e) for e in enumerate(
                 '2 3 4 5 6 7 8 9 T J Q K A'.split()))
    def __init__(self, card_spec):
        rank, suit = card_spec
        self.rank = self.RANKS.get(rank, -1)
        self._raw_rank = rank
        self.suit = suit

    def __cmp__(self, other):
        return cmp(self.rank, other.rank)

    def __repr__(self):
        return '%s("%s%s")' % (self.__class__.__name__,
                               self._raw_rank,
                               self.suit)

def is_flush(cards):
    suit = None
    for card in cards:
        if suit is None:
            suit = card.suit
        elif card.suit != suit:
            return False
    return True


def is_straight(cards):
    if (cards and
        cards[4].rank == Card.RANKS['A'] and
        cards[0].rank == Card.RANKS['2'] and
        cards[1].rank == Card.RANKS['3'] and
        cards[2].rank == Card.RANKS['4'] and
        cards[3].rank == Card.RANKS['5']):
        return True

    last_rank = None
    for card in cards:
        if last_rank is None:
            last_rank = card.rank
        elif last_rank + 1 != card.rank:
            return False
        last_rank = card.rank
    return True


class PokerHand(object):
    """Base poker hand."""
    def __init__(self, card_specs=None):
        if card_specs is None:
            self.cards = []
        else:
            self.cards = list(sorted([Card(spec) for spec in card_specs]))

        _is_flush = is_flush(self.cards)
        _is_straight = is_straight(self.cards)

        if _is_flush and _is_straight:
            self.rank = STRAIGHT_FLUSH
        elif _is_flush:
            self.rank = FLUSH
        elif _is_straight:
            self.rank = STRAIGHT
        else:
            self.rank = HIGH_CARD

    def __cmp__(self, other):
        lhs = self.cards[-1] if self.cards else None
        rhs = other.cards[-1] if other.cards else None

        return cmp((self.rank, lhs), (other.rank, rhs))


class StraightFlush(PokerHand):
    def __init__(self, *args, **kwargs):
        PokerHand.__init__(self, *args, **kwargs)
        self.rank = STRAIGHT_FLUSH


class FourOfaKind(PokerHand):
    def __init__(self, *args, **kwargs):
        PokerHand.__init__(self, *args, **kwargs)
        self.rank = FOUR_OFA_KIND


class FullHouse(PokerHand):
    def __init__(self, *args, **kwargs):
        PokerHand.__init__(self, *args, **kwargs)
        self.rank = FULL_HOUSE


class Flush(PokerHand):
    def __init__(self, *args, **kwargs):
        PokerHand.__init__(self, *args, **kwargs)
        self.rank = FLUSH


class Straight(PokerHand):
    def __init__(self, *args, **kwargs):
        PokerHand.__init__(self, *args, **kwargs)
        self.rank = STRAIGHT


class ThreeOfaKind(PokerHand):
    def __init__(self, *args, **kwargs):
        PokerHand.__init__(self, *args, **kwargs)
        self.rank = THREE_OFA_KIND


class TwoPair(PokerHand):
    def __init__(self, *args, **kwargs):
        PokerHand.__init__(self, *args, **kwargs)
        self.rank = TWO_PAIR


class Pair(PokerHand):
    def __init__(self, *args, **kwargs):
        PokerHand.__init__(self, *args, **kwargs)
        self.rank = PAIR


class HighCard(PokerHand):
    def __init__(self, *args, **kwargs):
        PokerHand.__init__(self, *args, **kwargs)
        self.rank = HIGH_CARD


def hand(hand_spec):
    return PokerHand(hand_spec.split())
