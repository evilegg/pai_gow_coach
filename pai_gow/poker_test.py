import unittest


from . import poker


class PokerEnumScoringTestCase(unittest.TestCase):

    def testStraightFlush(self):
        self.assertTrue(poker.Ranks.STRAIGHT_FLUSH >
                        poker.Ranks.FOUR_OFA_KIND)

    def testFourOfaKind(self):
        self.assertTrue(poker.Ranks.FOUR_OFA_KIND >
                        poker.Ranks.FULL_HOUSE)

    def testFullHouse(self):
        self.assertTrue(poker.Ranks.FULL_HOUSE >
                        poker.Ranks.FLUSH)

    def testFlush(self):
        self.assertTrue(poker.Ranks.FLUSH >
                        poker.Ranks.STRAIGHT)

    def testStraight(self):
        self.assertTrue(poker.Ranks.STRAIGHT >
                        poker.Ranks.THREE_OFA_KIND)

    def testThreeOfaKind(self):
        self.assertTrue(poker.Ranks.THREE_OFA_KIND >
                        poker.Ranks.TWO_PAIR)

    def testTwoPair(self):
        self.assertTrue(poker.Ranks.TWO_PAIR >
                        poker.Ranks.PAIR)

    def testPair(self):
        self.assertTrue(poker.Ranks.PAIR >
                        poker.Ranks.HIGH_CARD)


class PokerHandScoringTestCase(unittest.TestCase):

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


class PokerHandIdentification(unittest.TestCase):
    def testStraightFlush(self):
        self.assertEquals(poker.hand('As 2s 3s 4s 5s').rank,
                          poker.Ranks.STRAIGHT_FLUSH)

        self.assertEquals(poker.hand('3c 4c 5c 6c 7c').rank,
                          poker.Ranks.STRAIGHT_FLUSH)

    def testFourOfaKind(self):
        self.assertEquals(poker.hand('As Ac Ad Ah 6s').rank,
                          poker.Ranks.FOUR_OFA_KIND)

    def testFullHouse(self):
        self.assertEquals(poker.hand('As Ac 4s 4c 4d').rank,
                          poker.Ranks.FULL_HOUSE)

    def testFlush(self):
        self.assertEquals(poker.hand('As 3s 4s 5s 6s').rank,
                          poker.Ranks.FLUSH)

    def testStraight(self):
        self.assertEquals(poker.hand('As 2c 3s 4s 5s').rank,
                          poker.Ranks.STRAIGHT)

    def testThreeOfaKind(self):
        self.assertEquals(poker.hand('As Ac Ad 3s 5s').rank,
                          poker.Ranks.THREE_OFA_KIND)

    def testTwoPair(self):
        self.assertEquals(poker.hand('As Ac 3d 3s 5s').rank,
                          poker.Ranks.TWO_PAIR)

    def testOnePair(self):
        self.assertEquals(poker.hand('As Ac 3d 4s 5s').rank,
                          poker.Ranks.PAIR)

    def testHighCard(self):
        self.assertEquals(poker.hand('As Kc 3d 4s 5s').rank,
                          poker.Ranks.HIGH_CARD)


class TwoPairTestCase(unittest.TestCase):
    def testHigherHandWins(self):
        self.assertTrue(poker.hand('As Ac 3d 3s 5s') >
                        poker.hand('Ks Kc 3d 5c 5d'))

    @unittest.expectedFailure
    def testMismatchedHigherHand(self):
        self.assertTrue(poker.hand('As 3d 3s 4d 4s') <
                        poker.hand('Ks Kc 3d 5c 5d'))

class ThreeOfaKindTestCase(unittest.TestCase):
    def testHigherHandWins(self):
        self.assertTrue(poker.hand('As Ac Ad 3s 5s') >
                        poker.hand('Ks Kc Ks 3d 5d'))


class StraightTestCase(unittest.TestCase):
    def testHigherStraightWins(self):
        self.assertTrue(poker.hand('As 2c 3s 4s 5s') >
                        poker.hand('2c 3s 4s 5s 6s'))


class FlushTestCase(unittest.TestCase):
    def testHigherFlushWins(self):
        self.assertTrue(poker.hand('As 3s 4s 5s 6s') >
                        poker.hand('Ks 3s 4s 5s 6s'))


class FourOfaKindTestCase(unittest.TestCase):
    def testHigherHandWins(self):
        self.assertTrue(poker.hand('As Ac Ad Ah 6s') >
                        poker.hand('Ts Tc Td Th 8s'))


if '__main__' == __name__:
    unittest.main()
