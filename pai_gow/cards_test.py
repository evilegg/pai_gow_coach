import unittest


from cards import Card


class PokerCardTestCase(unittest.TestCase):
    def testRankComparisons(self):
        self.assertTrue(Card('As') > Card('Ks'))
        self.assertTrue(Card('Ks') > Card('Qs'))
        self.assertTrue(Card('Qs') > Card('Js'))
        self.assertTrue(Card('Js') > Card('Ts'))
        self.assertTrue(Card('Ts') > Card('9s'))
        self.assertTrue(Card('9s') > Card('8s'))
        self.assertTrue(Card('8s') > Card('7s'))
        self.assertTrue(Card('7s') > Card('6s'))
        self.assertTrue(Card('6s') > Card('5s'))
        self.assertTrue(Card('5s') > Card('4s'))
        self.assertTrue(Card('4s') > Card('3s'))
        self.assertTrue(Card('3s') > Card('2s'))

    def testRanksIgnoreSuits(self):
        self.assertTrue(Card('As') == Card('Ac') == Card('Ad') == Card('Ah') == Card('As'))
        self.assertTrue(Card('Ks') == Card('Kc') == Card('Kd') == Card('Kh') == Card('Ks'))
        self.assertTrue(Card('Qs') == Card('Qc') == Card('Qd') == Card('Qh') == Card('Qs'))
        self.assertTrue(Card('Js') == Card('Jc') == Card('Jd') == Card('Jh') == Card('Js'))
        self.assertTrue(Card('Ts') == Card('Tc') == Card('Td') == Card('Th') == Card('Ts'))
        self.assertTrue(Card('9s') == Card('9c') == Card('9d') == Card('9h') == Card('9s'))
        self.assertTrue(Card('8s') == Card('8c') == Card('8d') == Card('8h') == Card('8s'))
        self.assertTrue(Card('7s') == Card('7c') == Card('7d') == Card('7h') == Card('7s'))
        self.assertTrue(Card('6s') == Card('6c') == Card('6d') == Card('6h') == Card('6s'))
        self.assertTrue(Card('5s') == Card('5c') == Card('5d') == Card('5h') == Card('5s'))
        self.assertTrue(Card('4s') == Card('4c') == Card('4d') == Card('4h') == Card('4s'))
        self.assertTrue(Card('3s') == Card('3c') == Card('3d') == Card('3h') == Card('3s'))
        self.assertTrue(Card('2s') == Card('2c') == Card('2d') == Card('2h') == Card('2s'))


if '__main__' == __name__:
    unittest.main()
