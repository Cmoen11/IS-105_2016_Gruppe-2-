import unittest
import Poker
import Pointcalc_Poker

class TestRoyalFlush(unittest.TestCase):
    
    pokerCards = []
    def setUp(self):
        i = 0
        startCard = 8
        global pokerCards
        pokerCards = []
        for i in range(0,5) :
            obj = Poker.PokerCard(0, startCard)
            pokerCards.append(obj)
            print startCard
            startCard += 1
             
    def test_testCalculatePoints1(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.calculatePoints(pokerCards), 500000)



class TestStraightFlush(unittest.TestCase):
    pokerCards = []
    def setUp(self):
        i = 0
        startCard = 4
        global pokerCards
        pokerCards = []
        for i in range(0,5) :
            obj = Poker.PokerCard(0, startCard)
            pokerCards.append(obj)
            startCard += 1
             
    def test_testCalculatePoints2(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.calculatePoints(pokerCards), 480000)
        
        
class TestFourOfaKind(unittest.TestCase):
    pokerCards = []
    cards = []
    def setUp(self):
        i = 0
        global pokerCards
        global cards
        pokerCards = []
        cards = []
        for i in range(0,5) :
            obj = Poker.PokerCard(0,0)
            pokerCards.append(obj)
            
        for i in range(0,5) :
            obj = Poker.PokerCard(0,i)
            cards.append(obj)
            
            
    # A test where cards are four of a kind.         
    def test_testCalculatePoints3(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.calculatePoints(pokerCards), 460000)
    
    # A test where no cards are four of a kind.    
    def test_testCalculatePoints3(self):
        global cards
        self.assertEqual(Pointcalc_Poker.calculatePoints(cards), 0)    
        

class TestPair(unittest.TestCase):
    pokerCards = []
    def setUp(self):
        global pokerCards
        pokerCards = []
        
        # this is a pair of twos
        pokerCards.append(Poker.PokerCard(0,2))
        pokerCards.append(Poker.PokerCard(1,2))
        
        # the three remaining cards
        i = 5
        for i in range (5,8) :
            obj = Poker.PokerCard(0,i)
            pokerCards.append(obj)            
                

    def test_testCalculatePoints4(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.calculatePoints(pokerCards), 104)
        

class TestFullHouse(unittest.TestCase):
    pass
    
class TestFlush(unittest.TestCase): #Merthe
    pass

class TestStraight(unittest.TestCase):
    pass

class TestThreeOfaKind(unittest.TestCase):
    pokerCards = []
    cards = []
    def setUp(self):
        i = 0
        global pokerCards
        pokerCards = []
        pokerCards.append(Poker.PokerCard(0,2))
        pokerCards.append(Poker.PokerCard(0,3))
        pokerCards.append(Poker.PokerCard(0,2))
        pokerCards.append(Poker.PokerCard(0,3))
        pokerCards.append(Poker.PokerCard(0,2))
        
    def test_testCalculatePoints8(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.checkThreeOfaKind(pokerCards), 80000)
        
        

    
if __name__ == '__main__':
    unittest.main()
    
    
    