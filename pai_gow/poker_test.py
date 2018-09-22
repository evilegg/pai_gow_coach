import unittest


import poker


class PokerEnumScoringTestCase(unittest.TestCase):
    def testStraightFlush(self):
        self.assertGreater(poker.Ranks.STRAIGHT_FLUSH, poker.Ranks.FOUR_OFA_KIND)

    def testFourOfaKind(self):
        self.assertGreater(poker.Ranks.FOUR_OFA_KIND, poker.Ranks.FULL_HOUSE)

    def testFullHouse(self):
        self.assertGreater(poker.Ranks.FULL_HOUSE, poker.Ranks.FLUSH)

    def testFlush(self):
        self.assertGreater(poker.Ranks.FLUSH, poker.Ranks.STRAIGHT)

    def testStraight(self):
        self.assertGreater(poker.Ranks.STRAIGHT, poker.Ranks.THREE_OFA_KIND)

    def testThreeOfaKind(self):
        self.assertGreater(poker.Ranks.THREE_OFA_KIND, poker.Ranks.TWO_PAIR)

    def testTwoPair(self):
        self.assertGreater(poker.Ranks.TWO_PAIR, poker.Ranks.PAIR)

    def testPair(self):
        self.assertGreater(poker.Ranks.PAIR, poker.Ranks.HIGH_CARD)


class PokerHandScoringTestCase(unittest.TestCase):
    def testStraightFlush(self):
        self.assertGreater(poker.StraightFlush(), poker.FourOfaKind())

    def testFourOfaKind(self):
        self.assertGreater(poker.FourOfaKind(), poker.FullHouse())

    def testFullHouse(self):
        self.assertGreater(poker.FullHouse(), poker.Flush())

    def testFlush(self):
        self.assertGreater(poker.Flush(), poker.Straight())

    def testStraight(self):
        self.assertGreater(poker.Straight(), poker.ThreeOfaKind())

    def testThreeOfaKind(self):
        self.assertGreater(poker.ThreeOfaKind(), poker.TwoPair())

    def testTwoPair(self):
        self.assertGreater(poker.TwoPair(), poker.Pair())

    def testPair(self):
        self.assertGreater(poker.Pair(), poker.HighCard())


class PokerHandIdentification(unittest.TestCase):
    def testStraightFlush(self):
        self.assertEqual(poker.hand('As 2s 3s 4s 5s').rank, poker.Ranks.STRAIGHT_FLUSH_WHEEL)
        self.assertEqual(poker.hand('3c 4c 5c 6c 7c').rank, poker.Ranks.STRAIGHT_FLUSH)

    def testFourOfaKind(self):
        self.assertEqual(poker.hand('As Ac Ad Ah 6s').rank, poker.Ranks.FOUR_OFA_KIND)

    def testFullHouse(self):
        self.assertEqual(poker.hand('As Ac 4s 4c 4d').rank, poker.Ranks.FULL_HOUSE)

    def testFlush(self):
        self.assertEqual(poker.hand('As 3s 4s 5s 6s').rank, poker.Ranks.FLUSH)

    def testStraight(self):
        self.assertEqual(poker.hand('As 2c 3s 4s 5s').rank, poker.Ranks.STRAIGHT_WHEEL)
        self.assertEqual(poker.hand('2c 3s 4s 5s 6c').rank, poker.Ranks.STRAIGHT)

    def testThreeOfaKind(self):
        self.assertEqual(poker.hand('As Ac Ad 3s 5s').rank, poker.Ranks.THREE_OFA_KIND)

    def testTwoPair(self):
        self.assertEqual(poker.hand('As Ac 3d 3s 5s').rank, poker.Ranks.TWO_PAIR)

    def testOnePair(self):
        self.assertEqual(poker.hand('As Ac 3d 4s 5s').rank, poker.Ranks.PAIR)

    def testHighCard(self):
        self.assertEqual(poker.hand('As Kc 3d 4s 5s').rank, poker.Ranks.HIGH_CARD)


class PairTestCase(unittest.TestCase):
    def testHigherHandWins(self):
        self.assertGreater(poker.hand('As Ks Kc 3s 5s'),
                           poker.hand('Qc Qs 2h 3h 4h'))

    def testFirstKicker(self):
        self.assertGreater(poker.hand('As Ac 8s 6s 4s'),
                           poker.hand('Ad Ah 7h 6h 4h'))

    def testSecondKicker(self):
        self.assertGreater(poker.hand('As Ac 8s 6s 4s'),
                           poker.hand('Ad Ah 8h 5h 4h'))

    def testThirdKicker(self):
        self.assertGreater(poker.hand('As Ac 8s 6s 4s'),
                           poker.hand('Ad Ah 8h 6h 3h'))

class TwoPairTestCase(unittest.TestCase):
    def testHigherHandWins(self):
        self.assertGreater(poker.hand('As Ac 3d 3s 5s'),
                           poker.hand('Ks Kc 3d 5c 5d'))

    def testMismatchedHigherHand(self):
        self.assertGreater(poker.hand('Ks Kc 3d 5c 5d'),
                           poker.hand('As 3d 3s 4d 4s'))

    def testKicker(self):
        self.assertGreater(poker.hand('Ks Kc 3s 3c 5d'),
                           poker.hand('Kd Kh 3d 3c 4d'))


class ThreeOfaKindTestCase(unittest.TestCase):
    def testHigherHandWins(self):
        self.assertGreater(poker.hand('As Ac Ad 3s 5s'),
                           poker.hand('Ks Kc Ks 3d 5d'))

    def testRankingHandIsntHighest(self):
        self.assertGreater(poker.hand('Qs 5s 5c 5d 3s'),
                           poker.hand('Ac 2d 2s 2c 7d'))


class StraightTestCase(unittest.TestCase):
    def testHigherHandWins(self):
        self.assertGreater(poker.hand('3c 4s 5s 6s 7s'),
                           poker.hand('2c 3s 4s 5s 6s'))

    def testWheelieHand(self):
        self.assertGreater(poker.hand('2c 3s 4s 5s 6s'),
                           poker.hand('As 2c 3s 4s 5s'))


class FlushTestCase(unittest.TestCase):
    def testHigherHandWins(self):
        self.assertGreater(poker.hand('As 3s 4s 5s 6s'),
                           poker.hand('Ks 3s 4s 5s 6s'))


class FourOfaKindTestCase(unittest.TestCase):
    def testHigherHandWins(self):
        self.assertGreater(poker.hand('As Ac Ad Ah 6s'),
                           poker.hand('Ts Tc Td Th 8s'))


if '__main__' == __name__:
    unittest.main()
