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


class FlushTestCase(unittest.TestCase):
    def testFlushIsIdentified(self):
        self.assertIsInstance(poker.hand('As 3s 4s 5s 6s'), poker.Flush)

    def testHigherFlushWins(self):
        self.assertTrue(poker.hand('As 3s 4s 5s 6s') >
                        poker.hand('Ks 3s 4s 5s 6s'))


class PokerCardTestCase(unittest.TestCase):
    def testRankComparisons(self):
        self.assertTrue(poker.Card('As') > poker.Card('Ks'))
        self.assertTrue(poker.Card('Ks') > poker.Card('Qs'))
        self.assertTrue(poker.Card('Qs') > poker.Card('Js'))
        self.assertTrue(poker.Card('Js') > poker.Card('Ts'))
        self.assertTrue(poker.Card('Ts') > poker.Card('9s'))
        self.assertTrue(poker.Card('9s') > poker.Card('8s'))
        self.assertTrue(poker.Card('8s') > poker.Card('7s'))
        self.assertTrue(poker.Card('7s') > poker.Card('6s'))
        self.assertTrue(poker.Card('6s') > poker.Card('5s'))
        self.assertTrue(poker.Card('5s') > poker.Card('4s'))
        self.assertTrue(poker.Card('4s') > poker.Card('3s'))
        self.assertTrue(poker.Card('3s') > poker.Card('2s'))

    def testRanksIgnoreSuits(self):
        self.assertTrue(poker.Card('As') == poker.Card('Ac')
                                         == poker.Card('Ad')
                                         == poker.Card('Ah'))
        self.assertTrue(poker.Card('Ks') == poker.Card('Kc')
                                         == poker.Card('Kd')
                                         == poker.Card('Kh'))
        self.assertTrue(poker.Card('Qs') == poker.Card('Qc')
                                         == poker.Card('Qd')
                                         == poker.Card('Qh'))
        self.assertTrue(poker.Card('Js') == poker.Card('Jc')
                                         == poker.Card('Jd')
                                         == poker.Card('Jh'))
        self.assertTrue(poker.Card('Ts') == poker.Card('Tc')
                                         == poker.Card('Td')
                                         == poker.Card('Th'))
        self.assertTrue(poker.Card('9s') == poker.Card('9c')
                                         == poker.Card('9d')
                                         == poker.Card('9h'))
        self.assertTrue(poker.Card('8s') == poker.Card('8c')
                                         == poker.Card('8d')
                                         == poker.Card('8h'))
        self.assertTrue(poker.Card('7s') == poker.Card('7c')
                                         == poker.Card('7d')
                                         == poker.Card('7h'))
        self.assertTrue(poker.Card('6s') == poker.Card('6c')
                                         == poker.Card('6d')
                                         == poker.Card('6h'))
        self.assertTrue(poker.Card('5s') == poker.Card('5c')
                                         == poker.Card('5d')
                                         == poker.Card('5h'))
        self.assertTrue(poker.Card('4s') == poker.Card('4c')
                                         == poker.Card('4d')
                                         == poker.Card('4h'))
        self.assertTrue(poker.Card('3s') == poker.Card('3c')
                                         == poker.Card('3d')
                                         == poker.Card('3h'))
        self.assertTrue(poker.Card('2s') == poker.Card('2c')
                                         == poker.Card('2d')
                                         == poker.Card('2h'))


if '__main__' == __name__:
    unittest.main()
