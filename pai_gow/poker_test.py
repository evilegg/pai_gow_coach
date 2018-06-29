import unittest


import poker


class PokerScoringTestCase(unittest.TestCase):

    def testFiveOfAKind(self):
        self.assertTrue(poker.FIVE_OFA_KIND > poker.STRAIGHT_FLUSH)
        self.assertTrue(poker.FIVE_OFA_KIND > poker.FOUR_OFA_KIND)
        self.assertTrue(poker.FIVE_OFA_KIND > poker.FULL_HOUSE)
        self.assertTrue(poker.FIVE_OFA_KIND > poker.FLUSH)
        self.assertTrue(poker.FIVE_OFA_KIND > poker.STRAIGHT)
        self.assertTrue(poker.FIVE_OFA_KIND > poker.THREE_OFA_KIND)
        self.assertTrue(poker.FIVE_OFA_KIND > poker.TWO_PAIR)
        self.assertTrue(poker.FIVE_OFA_KIND > poker.PAIR)
        self.assertTrue(poker.FIVE_OFA_KIND > poker.HIGH_CARD)

    def testStraightFlush(self):
        self.assertTrue(poker.STRAIGHT_FLUSH > poker.FOUR_OFA_KIND)
        self.assertTrue(poker.STRAIGHT_FLUSH > poker.FULL_HOUSE)
        self.assertTrue(poker.STRAIGHT_FLUSH > poker.FLUSH)
        self.assertTrue(poker.STRAIGHT_FLUSH > poker.STRAIGHT)
        self.assertTrue(poker.STRAIGHT_FLUSH > poker.THREE_OFA_KIND)
        self.assertTrue(poker.STRAIGHT_FLUSH > poker.TWO_PAIR)
        self.assertTrue(poker.STRAIGHT_FLUSH > poker.PAIR)
        self.assertTrue(poker.STRAIGHT_FLUSH > poker.HIGH_CARD)


if '__main__' == __name__:
    unittest.main()
