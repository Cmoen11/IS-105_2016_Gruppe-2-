'''
   1.2.4

   Poker!

'''
import random 

def deal() :
    


def generateCards():
    
    pokerCards = []
    
    i = 0                   # For loop
    x = 0                   # for loop
    symbole = 1             # deligere symbole
    value = 1               # Deligere value
    
    for x in range (0,4) :
        for i in range(0,13) :
            obj = PokerCard(symbole, value)
            pokerCards.append(obj)
            value += 1
        symbole += 1
        value = 1
    
    pokerCards = random.sample(pokerCards, len(pokerCards))     
    return pokerCards
               

'''

def cardDictionary () :
    cardsAvailable = {}
    i = 0
    
    for i in range(0,51) :
        cardsAvailable[i] = True


    return cardsAvailable
'''

class PokerCard:
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
    
    

    def __init__ (self, symbole, value) :
        '''
        Symbole er da hvilken type kort det er. 
        Value er da hvilken veri kortet har
        
        '''
        self.symbole = symbole
        self.value = value
        
            
    def getValue(self) :
        return self.value
    
    def getSymbole(self) :
        return self.symbole
    
    


class Player :
    def __init__ (self, cards) :
        '''
        Give the player random name
        '''
        
        names = ["Christian", "Erlend", "Ola", "Tommy Woa", "Merethe<3", "Benny", "Henrik aka ditcher"]
        self.cards = cards
        
        self.name = names[randint(0, 6)]
        
        
    def getName(self):
        return self.name
    def getCards(self):
        return self.cards
            
cards = generateCards()
  
print cards[1].getSymbole()
print cards[1].getValue()