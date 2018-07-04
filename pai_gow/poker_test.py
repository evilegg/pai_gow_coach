import unittest


from . import poker


class TestCase(unittest.TestCase):
    def assertPokerGreaterThan(self, lhs, rhs):
        """Assert that lhs is a higher poker hand than rhs."""
        self.assertTrue(poker.hand(lhs) > poker.hand(rhs))


class PokerEnumScoringTestCase(TestCase):
    def testStraightFlush(self):
        self.assertTrue(poker.Ranks.STRAIGHT_FLUSH > poker.Ranks.FOUR_OFA_KIND)

    def testFourOfaKind(self):
        self.assertTrue(poker.Ranks.FOUR_OFA_KIND > poker.Ranks.FULL_HOUSE)

    def testFullHouse(self):
        self.assertTrue(poker.Ranks.FULL_HOUSE > poker.Ranks.FLUSH)

    def testFlush(self):
        self.assertTrue(poker.Ranks.FLUSH > poker.Ranks.STRAIGHT)

    def testStraight(self):
        self.assertTrue(poker.Ranks.STRAIGHT > poker.Ranks.THREE_OFA_KIND)

    def testThreeOfaKind(self):
        self.assertTrue(poker.Ranks.THREE_OFA_KIND > poker.Ranks.TWO_PAIR)

    def testTwoPair(self):
        self.assertTrue(poker.Ranks.TWO_PAIR > poker.Ranks.PAIR)

    def testPair(self):
        self.assertTrue(poker.Ranks.PAIR > poker.Ranks.HIGH_CARD)


class PokerHandScoringTestCase(TestCase):
    def testStraightFlush(self):
        self.assertTrue(poker.StraightFlush() > poker.FourOfaKind())

    def testFourOfaKind(self):
        self.assertTrue(poker.FourOfaKind() > poker.FullHouse())

    def testFullHouse(self):
        self.assertTrue(poker.FullHouse() > poker.Flush())

    def testFlush(self):
        self.assertTrue(poker.Flush() > poker.Straight())

    def testStraight(self):
        self.assertTrue(poker.Straight() > poker.ThreeOfaKind())

    def testThreeOfaKind(self):
        self.assertTrue(poker.ThreeOfaKind() > poker.TwoPair())

    def testTwoPair(self):
        self.assertTrue(poker.TwoPair() > poker.Pair())

    def testPair(self):
        self.assertTrue(poker.Pair() > poker.HighCard())


class PokerHandIdentification(TestCase):
    def testStraightFlush(self):
        self.assertIsInstance(poker.hand('As 2s 3s 4s 5s'), poker.StraightFlush)
        self.assertIsInstance(poker.hand('3c 4c 5c 6c 7c'), poker.StraightFlush)

    def testFourOfaKind(self):
        self.assertIsInstance(poker.hand('As Ac Ad Ah 6s'), poker.FourOfaKind)

    def testFullHouse(self):
        self.assertIsInstance(poker.hand('As Ac 4s 4c 4d'), poker.FullHouse)

    def testFlush(self):
        self.assertIsInstance(poker.hand('As 3s 4s 5s 6s'), poker.Flush)

    def testStraight(self):
        self.assertIsInstance(poker.hand('As 2c 3s 4s 5s'), poker.Straight)

    def testThreeOfaKind(self):
        self.assertIsInstance(poker.hand('As Ac Ad 3s 5s'), poker.ThreeOfaKind)

    def testTwoPair(self):
        self.assertIsInstance(poker.hand('As Ac 3d 3s 5s'), poker.TwoPair)

    def testOnePair(self):
        self.assertIsInstance(poker.hand('As Ac 3d 4s 5s'), poker.Pair)

    def testHighCard(self):
        self.assertIsInstance(poker.hand('As Kc 3d 4s 5s'), poker.HighCard)


class PairTestCase(TestCase):
    def testHigherHandWins(self):
        self.assertPokerGreaterThan('As Ks Kc 3s 5s',
                                    'Qc Qs 2h 3h 4h')

    def testFirstKicker(self):
        self.assertPokerGreaterThan('As Ac 8s 6s 4s',
                                    'Ad Ah 7h 6h 4h')

    def testSecondKicker(self):
        self.assertPokerGreaterThan('As Ac 8s 6s 4s',
                                    'Ad Ah 8h 5h 4h')

    def testThirdKicker(self):
        self.assertPokerGreaterThan('As Ac 8s 6s 4s',
                                    'Ad Ah 8h 6h 3h')

class TwoPairTestCase(TestCase):
    def testHigherHandWins(self):
        self.assertPokerGreaterThan('As Ac 3d 3s 5s', 'Ks Kc 3d 5c 5d')

    def testMismatchedHigherHand(self):
        self.assertPokerGreaterThan('Ks Kc 3d 5c 5d', 'As 3d 3s 4d 4s')

    def testKicker(self):
        self.assertPokerGreaterThan('Ks Kc 3s 3c 5d', 'Kd Kh 3d 3c 4d')


class ThreeOfaKindTestCase(TestCase):
    def testHigherHandWins(self):
        self.assertPokerGreaterThan('As Ac Ad 3s 5s',
                                    'Ks Kc Ks 3d 5d')

    def testRankingHandIsntHighest(self):
        self.assertPokerGreaterThan('Qs 5s 5c 5d 3s',
                                    'Ac 2d 2s 2c 7d')


class StraightTestCase(TestCase):
    def testHigherHandWins(self):
        self.assertPokerGreaterThan('3c 4s 5s 6s 7s',
                                    '2c 3s 4s 5s 6s')

    def testWheelieHand(self):
        self.assertPokerGreaterThan('2c 3s 4s 5s 6s',
                                    'As 2c 3s 4s 5s')


class FlushTestCase(TestCase):
    def testHigherHandWins(self):
        self.assertPokerGreaterThan('As 3s 4s 5s 6s',
                                    'Ks 3s 4s 5s 6s')


class FourOfaKindTestCase(TestCase):
    def testHigherHandWins(self):
        self.assertPokerGreaterThan('As Ac Ad Ah 6s', 'Ts Tc Td Th 8s')


if '__main__' == __name__:
    unittest.main()
