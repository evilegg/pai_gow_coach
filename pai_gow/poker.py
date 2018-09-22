"""Cards module for playing poker."""


import collections


from cards import Card


class Ranks(object):
    """The various legal poker hands."""
    HIGH_CARD      = 1
    PAIR           = 1 << 1
    TWO_PAIR       = 1 << 2
    THREE_OFA_KIND = 1 << 3
    STRAIGHT       = 1 << 4
    STRAIGHT_WHEEL = STRAIGHT - 1
    FLUSH          = 1 << 5
    FULL_HOUSE     = 1 << 6
    FOUR_OFA_KIND  = 1 << 7
    STRAIGHT_FLUSH = 1 << 8
    STRAIGHT_FLUSH_WHEEL = STRAIGHT_FLUSH - 1


def is_flush(cards):
    suit = None
    for card in cards:
        if suit is None:
            suit = card.suit
        elif card.suit != suit:
            return False
    return True


def is_straight(cards):
    # catch the wheel which doesn't come in order when sorted
    if (cards and
        cards[0].rank == Card.RANKS['2'] and
        cards[1].rank == Card.RANKS['3'] and
        cards[2].rank == Card.RANKS['4'] and
        cards[3].rank == Card.RANKS['5'] and
        cards[4].rank == Card.RANKS['A']):
        return True

    last_rank = None
    for card in cards:
        if last_rank is None:
            last_rank = card.rank
        elif last_rank + 1 != card.rank:
            return False
        last_rank = card.rank
    return True


def _count_matches(cards):
    groupings = collections.Counter()
    for card in cards:
        groupings[card.rank] += 1
    return list(sorted(groupings.values()))


def _is_three_ofa_kind(cards):
    return [1, 1, 3] == _count_matches(cards)


def _is_four_ofa_kind(cards):
    return [1, 4] == _count_matches(cards)


def _is_full_house(cards):
    return [2, 3] == _count_matches(cards)


def _is_two_pair(cards):
    return [1, 2, 2] == _count_matches(cards)


def _is_pair(cards):
    return [1, 1, 1, 2] == _count_matches(cards)


def assign_rank(cards):
    """Assign the collection of cards a poker rank."""
    _is_flush = is_flush(cards)
    _is_straight = is_straight(cards)
    _is_wheel = (is_straight and 
                    cards and
                    cards[0].rank == Card.RANKS['2']
                    and cards[-1].rank == Card.RANKS['A'])

    if _is_flush and _is_straight:
        return Ranks.STRAIGHT_FLUSH_WHEEL if _is_wheel else Ranks.STRAIGHT_FLUSH
    elif _is_four_ofa_kind(cards):
        return Ranks.FOUR_OFA_KIND
    elif _is_full_house(cards):
        return Ranks.FULL_HOUSE
    elif _is_flush:
        return Ranks.FLUSH
    elif _is_straight:
        return Ranks.STRAIGHT_WHEEL if _is_wheel else Ranks.STRAIGHT
    elif _is_three_ofa_kind(cards):
        return Ranks.THREE_OFA_KIND
    elif _is_two_pair(cards):
        return Ranks.TWO_PAIR
    elif _is_pair(cards):
        return Ranks.PAIR
    else:
        return Ranks.HIGH_CARD


class Hand(object):
    """Base poker hand."""
    def __init__(self, card_specs=None):
        if card_specs is None:
            self.cards = []
            self.rank = None
        else:
            self.cards = list(sorted([Card(spec) for spec in card_specs.split()]))
            self.rank = assign_rank(self.cards)

    def __cmp__(self, other):
        return cmp(self.score(), other.score())

    def score(self):
        return (self.rank, self.order_cards())

    def order_cards(self):
        if not self.cards:
            return []

        counter = collections.Counter()
        for card in self.cards:
            counter[card.rank] += 1

        # sort cards by count then rank
        sorted_cards = sorted([(cnt, rank) for rank, cnt in counter.items()],
                              reverse=True)
        return sorted_cards


class StraightFlush(Hand):
    def __init__(self, *args, **kwargs):
        Hand.__init__(self, *args, **kwargs)
        self.rank = Ranks.STRAIGHT_FLUSH


class FourOfaKind(Hand):
    def __init__(self, *args, **kwargs):
        Hand.__init__(self, *args, **kwargs)
        self.rank = self.rank or Ranks.FOUR_OFA_KIND


class FullHouse(Hand):
    def __init__(self, *args, **kwargs):
        Hand.__init__(self, *args, **kwargs)
        self.rank = self.rank or Ranks.FULL_HOUSE


class Flush(Hand):
    def __init__(self, *args, **kwargs):
        Hand.__init__(self, *args, **kwargs)
        self.rank = self.rank or Ranks.FLUSH


class Straight(Hand):
    def __init__(self, *args, **kwargs):
        Hand.__init__(self, *args, **kwargs)
        self.rank = self.rank or Ranks.STRAIGHT


class ThreeOfaKind(Hand):
    def __init__(self, *args, **kwargs):
        Hand.__init__(self, *args, **kwargs)
        self.rank = self.rank or Ranks.THREE_OFA_KIND


class TwoPair(Hand):
    def __init__(self, *args, **kwargs):
        Hand.__init__(self, *args, **kwargs)
        self.rank = self.rank or Ranks.TWO_PAIR


class Pair(Hand):
    def __init__(self, *args, **kwargs):
        Hand.__init__(self, *args, **kwargs)
        self.rank = self.rank or Ranks.PAIR


class HighCard(Hand):
    def __init__(self, *args, **kwargs):
        Hand.__init__(self, *args, **kwargs)
        self.rank = self.rank or Ranks.HIGH_CARD

