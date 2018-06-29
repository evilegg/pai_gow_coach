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


class Card(object):
    RANKS = dict(reversed(e) for e in enumerate(
                 '2 3 4 5 6 7 8 9 T J Q K A'.split()))
    def __init__(self, card_spec):
        rank, suit = card_spec
        self.rank = self.RANKS.get(rank, -1)
        self.suit = suit

    def __cmp__(self, other):
        return cmp(self.rank, other.rank)


class PokerHand(object):
    """Base poker hand."""
    RANK = None
    def __init__(self, card_specs=None):
        if card_specs is None:
            self.cards = []
        else:
            self.cards = [Card(spec) for spec in card_specs]

    def __cmp__(self, other):
        lhs = self.cards[0] if self.cards else None
        rhs = other.cards[0] if other.cards else None

        return cmp((self.RANK, lhs), (other.RANK, rhs))


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


def is_flush(cards):
    suit = None
    for card in cards:
        if suit is None:
            suit = card.suit
        elif card.suit != suit:
            return False
    return True


def hand(card_spec):
    cards = sorted(Card(card) for card in card_spec.split())
    if is_flush(cards):
        return Flush(card_spec.split())
