'''
   1.2.4

   Poker!

'''




def giveCards() :
    pass

def calculateWinner() :     
    pass

def generateCards() :
    pokerCards = []
    
    ruter = 13
    hjerter = 13
    spar = 13
    klover = 13
    
    
    i = 0
    x = 0
    symbole = 1
    value = 1
    for x in range (0,4) :
        
        for i in range(0,13) :
            pokerCards.append(PokerCards(symbole, value))
            value += 1
            
        symbole += 1
            
    return pokerCards
               


class PokerCards:
    '''
    Symbole definasjon: 
    1 = Ruter
    2 = Hjerter
    3 = Spar
    4 = kløver
    
    Value definasjon
    1.   2
    2.   3
    3.   4
    4.   5
    5.   6
    6.   7
    7.   8
    8.   9
    9.   10
    10.  Knekt
    11.  Dronning
    12.  Konge
    13.  Ess
    '''

    def __init__ (symbole, value) :
        '''
        Symbole er da hvilken type kort det er. 
        Value er da hvilken veri kortet har
        
        '''
        self.symbole = symbole
        self.value = value
        
        pokerCards.counter += 1
            
    def getValue(self) :
        return self.value
    
    def getSymbole(self) :
        return self.Symbole
    
    

generateCards()
