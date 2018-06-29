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
FIVE_OFA_KIND  = 1 << 9


class PokerHand(object):
    """Base poker hand."""
    RANK = None
    def __cmp__(self, other):
        return cmp(self.RANK, other.RANK)


class FiveOfaKind(PokerHand):
    RANK = FIVE_OFA_KIND


class StraightFlush(PokerHand):
    RANK = STRAIGHT_FLUSH


class FourOfaKind(PokerHand):
    RANK = FOUR_OFA_KIND


class FullHouse(PokerHand):
    RANK = FULL_HOUSE


class Flush(PokerHand):
    RANK = FLUSH


class Straight(PokerHand):
    RANK = STRAIGHT


class ThreeOfaKind(PokerHand):
    RANK = THREE_OFA_KIND


class TwoPair(PokerHand):
    RANK = TWO_PAIR


class Pair(PokerHand):
    RANK = PAIR


class HighCard(PokerHand):
    RANK = HIGH_CARD
