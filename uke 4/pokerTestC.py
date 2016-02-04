import unittest
import Poker
import Pointcalc_Poker

class TestCalculatePoints(unittest.TestCase):
    pokerCards = []
    def setUp(self):
        i = 0
        startCard = 8
        global pokerCards
        pokerCards = []
        for i in range(0,5) :
            obj = Poker.PokerCard(0, startCard)
            print startCard
            pokerCards.append(obj)
            startCard += 1
             
    def test_testCalculatePoints(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.checkRoyalFush(pokerCards), 500000)



if __name__ == '__main__':
    unittest.main()
    
    
    