import unittest


import poker


class PokerEnumScoringTestCase(unittest.TestCase):

    def testFiveOfaKind(self):
        self.assertTrue(poker.FIVE_OFA_KIND > poker.STRAIGHT_FLUSH)

    def testStraightFlush(self):
        self.assertTrue(poker.STRAIGHT_FLUSH > poker.FOUR_OFA_KIND)

    def testFourOfaKind(self):
        self.assertTrue(poker.FOUR_OFA_KIND > poker.FULL_HOUSE)

    def testFullHouse(self):
        self.assertTrue(poker.FULL_HOUSE > poker.FLUSH)

    def testFlush(self):
        self.assertTrue(poker.FLUSH > poker.STRAIGHT)

    def testStraight(self):
        self.assertTrue(poker.STRAIGHT > poker.THREE_OFA_KIND)

    def testThreeOfaKind(self):
        self.assertTrue(poker.THREE_OFA_KIND > poker.TWO_PAIR)

    def testTwoPair(self):
        self.assertTrue(poker.TWO_PAIR > poker.PAIR)

    def testPair(self):
        self.assertTrue(poker.PAIR > poker.HIGH_CARD)


class PokerHandScoringTestCase(unittest.TestCase):

    def testFiveOfaKind(self):
        self.assertTrue(poker.FiveOfaKind() > poker.StraightFlush())

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


if '__main__' == __name__:
    unittest.main()
