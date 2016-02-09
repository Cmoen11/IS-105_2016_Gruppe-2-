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
    cards = []
    pokerCards = []
    def setUp(self) :
        global cards
        global pokerCards
        cards = [
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,2),

            ]            
        pokerCards = [
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,2),

            ]          
            
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
    pokerCards = []
    cards = []
    def setUp(self):
        i = 0
        global pokerCards
        global cards
        pokerCards = []
        cards = []

        cards = [
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,3),
            Poker.PokerCard(2,3),

            ]       
        
    def test_testCalculatePoints8(self):
            global cards
            self.assertEqual(Pointcalc_Poker.checkFourOfaKind(cards), 140040)        
  
class TestFlush(unittest.TestCase): 
    pokerCards = []
    pokerCards2 = []
    def setUp(self):
        global pokerCards
        global pokerCards2
        pokerCards = [
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,3),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,1),
      
        ]
        pokerCards2 = [
            Poker.PokerCard(1,9),
            Poker.PokerCard(2,4),
            Poker.PokerCard(2,3),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,12),
      
        ]        

    def test_testCalculatePoints_flush(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.calculatePoints(pokerCards), 120000)
    def test_testCalculatePoints_flush2(self):
        global pokerCards2
        self.assertEqual(Pointcalc_Poker.calculatePoints(pokerCards2), 30)    

class TestStraight(unittest.TestCase):
    pokerCards = []
    cards = []
    def setUp(self):
        i = 0 
        global pokerCards
        pokerCards[
             Poker.PokerCard(1,1),
             Poker.PokerCard(3,2),
             Poker.PokerCard(2,3),
             Poker.PokerCard(2,4),
             Poker.PokerCard(0,5),

        ]
        
    def test_testCalcualtePoints7(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.checkStraight(pokerCards), 100000)
    

class TestThreeOfaKind(unittest.TestCase):
    pokerCards = []
    cards = []
    def setUp(self):
        i = 0
        global pokerCards
        pokerCards = [
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,3),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,1),
      
        ]
        
        
    def test_testCalculatePoints8(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.checkThreeOfaKind(pokerCards), 80040)
        
        

    
if __name__ == '__main__':
    unittest.main()
    
    
