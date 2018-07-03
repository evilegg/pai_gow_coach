import unittest


from . import cards


class PokerCardTestCase(unittest.TestCase):
    def testRankComparisons(self):
        self.assertTrue(cards.Card('As') > cards.Card('Ks'))
        self.assertTrue(cards.Card('Ks') > cards.Card('Qs'))
        self.assertTrue(cards.Card('Qs') > cards.Card('Js'))
        self.assertTrue(cards.Card('Js') > cards.Card('Ts'))
        self.assertTrue(cards.Card('Ts') > cards.Card('9s'))
        self.assertTrue(cards.Card('9s') > cards.Card('8s'))
        self.assertTrue(cards.Card('8s') > cards.Card('7s'))
        self.assertTrue(cards.Card('7s') > cards.Card('6s'))
        self.assertTrue(cards.Card('6s') > cards.Card('5s'))
        self.assertTrue(cards.Card('5s') > cards.Card('4s'))
        self.assertTrue(cards.Card('4s') > cards.Card('3s'))
        self.assertTrue(cards.Card('3s') > cards.Card('2s'))

    def testRanksIgnoreSuits(self):
        self.assertTrue(cards.Card('As') == cards.Card('Ac')
                                         == cards.Card('Ad')
                                         == cards.Card('Ah'))
        self.assertTrue(cards.Card('Ks') == cards.Card('Kc')
                                         == cards.Card('Kd')
                                         == cards.Card('Kh'))
        self.assertTrue(cards.Card('Qs') == cards.Card('Qc')
                                         == cards.Card('Qd')
                                         == cards.Card('Qh'))
        self.assertTrue(cards.Card('Js') == cards.Card('Jc')
                                         == cards.Card('Jd')
                                         == cards.Card('Jh'))
        self.assertTrue(cards.Card('Ts') == cards.Card('Tc')
                                         == cards.Card('Td')
                                         == cards.Card('Th'))
        self.assertTrue(cards.Card('9s') == cards.Card('9c')
                                         == cards.Card('9d')
                                         == cards.Card('9h'))
        self.assertTrue(cards.Card('8s') == cards.Card('8c')
                                         == cards.Card('8d')
                                         == cards.Card('8h'))
        self.assertTrue(cards.Card('7s') == cards.Card('7c')
                                         == cards.Card('7d')
                                         == cards.Card('7h'))
        self.assertTrue(cards.Card('6s') == cards.Card('6c')
                                         == cards.Card('6d')
                                         == cards.Card('6h'))
        self.assertTrue(cards.Card('5s') == cards.Card('5c')
                                         == cards.Card('5d')
                                         == cards.Card('5h'))
        self.assertTrue(cards.Card('4s') == cards.Card('4c')
                                         == cards.Card('4d')
                                         == cards.Card('4h'))
        self.assertTrue(cards.Card('3s') == cards.Card('3c')
                                         == cards.Card('3d')
                                         == cards.Card('3h'))
        self.assertTrue(cards.Card('2s') == cards.Card('2c')
                                         == cards.Card('2d')
                                         == cards.Card('2h'))


if '__main__' == __name__:
    unittest.main()
