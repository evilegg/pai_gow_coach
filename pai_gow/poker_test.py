import unittest


import poker


class PokerScoringTestCase(unittest.TestCase):

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


if '__main__' == __name__:
    unittest.main()
