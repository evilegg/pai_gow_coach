"""Cards module for playing poker."""


import collections
import enum


from cards import Card


Ranks = enum.IntEnum(
    'Ranks',
    'HIGH_CARD'
    ' PAIR'
    ' TWO_PAIR'
    ' THREE_OFA_KIND'
    ' STRAIGHT_WHEEL'
    ' STRAIGHT'
    ' FLUSH'
    ' FULL_HOUSE'
    ' FOUR_OFA_KIND'
    ' STRAIGHT_FLUSH_WHEEL'
    ' STRAIGHT_FLUSH')


def is_flush(cards):
    return all(e.suit == cards[0].suit for e in cards)


def is_straight(cards):
    if len(cards) != 5:
        return False

    # catch the wheel which doesn't come in order when sorted
    if (cards[0].score() == Card.RANKS['2'] and
        cards[1].score() == Card.RANKS['3'] and
        cards[2].score() == Card.RANKS['4'] and
        cards[3].score() == Card.RANKS['5'] and
        cards[4].score() == Card.RANKS['A']):
        return True

    last_card = cards[0]
    for card in cards[1:]:
        if card.score() != last_card.score() + 1:
            return False
        last_card = card

    return True


def is_wheel(cards):
    if len(cards) != 5:
        return False

    # catch the wheel which doesn't come in order when sorted
    if (cards[0].score() == Card.RANKS['2'] and
        cards[1].score() == Card.RANKS['3'] and
        cards[2].score() == Card.RANKS['4'] and
        cards[3].score() == Card.RANKS['5'] and
        cards[4].score() == Card.RANKS['A']):
        return True

    return False


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

# TODO: store cards highest rank to lowest rank to simplify straight/wheel scoring

def assign_rank(cards):
    """Assign the collection of cards a poker rank."""
    _is_flush = is_flush(cards)
    _is_straight = is_straight(cards)
    _is_wheel = is_wheel(cards)

    # pylint: disable=E1101
    if _is_flush and _is_wheel:
        return Ranks.STRAIGHT_FLUSH_WHEEL
    if _is_flush and _is_straight:
        return Ranks.STRAIGHT_FLUSH
    elif _is_four_ofa_kind(cards):
        return Ranks.FOUR_OFA_KIND
    elif _is_full_house(cards):
        return Ranks.FULL_HOUSE
    elif _is_flush:
        return Ranks.FLUSH
    elif _is_wheel:
        return Ranks.STRAIGHT_WHEEL
    elif _is_straight:
        return Ranks.STRAIGHT
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

    def __eq__(self, other_hand):
        return self.score() == other_hand.score()
    
    def __lt__(self, other_hand):
        return self.score() < other_hand.score()

    def __repr__(self):
        cards = [''.join([c.rank, c.suit]) for c in self.cards]
        return str(' '.join(cards))
    
    def score(self):
        return (self.rank,) + tuple(self.order_cards())

    def order_cards(self):
        if not self.cards:
            return []

        counter = collections.Counter()
        for card in self.cards:
            counter[card.score()] += 1

        # sort cards by count then rank
        sorted_cards = sorted([(cnt, rank) for rank, cnt in counter.items()], reverse=True)
        return sorted_cards


class StraightFlush(Hand):
    def __init__(self, *args, **kwargs):
        Hand.__init__(self, *args, **kwargs)
        # pylint: disable=E1101
        self.rank = Ranks.STRAIGHT_FLUSH


class FourOfaKind(Hand):
    def __init__(self, *args, **kwargs):
        Hand.__init__(self, *args, **kwargs)
        # pylint: disable=E1101
        self.rank = self.rank or Ranks.FOUR_OFA_KIND


class FullHouse(Hand):
    def __init__(self, *args, **kwargs):
        Hand.__init__(self, *args, **kwargs)
        # pylint: disable=E1101
        self.rank = self.rank or Ranks.FULL_HOUSE


class Flush(Hand):
    def __init__(self, *args, **kwargs):
        Hand.__init__(self, *args, **kwargs)
        # pylint: disable=E1101
        self.rank = self.rank or Ranks.FLUSH


class Straight(Hand):
    def __init__(self, *args, **kwargs):
        Hand.__init__(self, *args, **kwargs)
        # pylint: disable=E1101
        self.rank = self.rank or Ranks.STRAIGHT


class ThreeOfaKind(Hand):
    def __init__(self, *args, **kwargs):
        Hand.__init__(self, *args, **kwargs)
        # pylint: disable=E1101
        self.rank = self.rank or Ranks.THREE_OFA_KIND


class TwoPair(Hand):
    def __init__(self, *args, **kwargs):
        Hand.__init__(self, *args, **kwargs)
        # pylint: disable=E1101
        self.rank = self.rank or Ranks.TWO_PAIR


class Pair(Hand):
    def __init__(self, *args, **kwargs):
        Hand.__init__(self, *args, **kwargs)
        # pylint: disable=E1101
        self.rank = self.rank or Ranks.PAIR


class HighCard(Hand):
    def __init__(self, *args, **kwargs):
        Hand.__init__(self, *args, **kwargs)
        # pylint: disable=E1101
        self.rank = self.rank or Ranks.HIGH_CARD


if '__main__' == __name__:
    assert Hand('As 3s 4s 5s 6s').rank == Ranks.FLUSH
    print(Hand('As 2s 3s 4s 5s'))