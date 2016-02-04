def calculatePoints(cards) :
    '''
    this method will return back a 'score' of the selected score, in order to find the winner.
    '''
    #Score given:
    points = 0;
    
    
    '''
    Royalflush == 200k points
    
    PAIR of 2's give 2 points + 2 for every exstra card /// + 1 point for every number higher than this.
    
    
    '''
    points = checkRoyalFush(cards)
    if (points > 0 ) :
        return points

    points = checkPair(cards)
    if (points > 0) :
        return points
    
    else :
        return 0
    
    
def  checkStraightFlush (cards):
    pass
def checkFourLike(cards) :
    pass
def checkFullHouse(cards) :
    pass
def checkFlush(cards) :
    pass
def checkStraight(cards) :
    pass
def checkThreeLike(cards) :
    pass
def checkRoyalFush (cards) :
    cards = sorted(cards)
    
    color = checkIfAllCardsIsBlack(cards)
    
    if (color is False) :
        color = checkIfAllCardsIsRed(cards)
    
    
    if (color) :
        print "alle sorte kort!"
        if (cards[0].getValue() == 8) and (cards[1].getValue() == 9) and (cards[2].getValue() == 10) and (cards[3].getValue() == 11) and (cards[4].getValue() == 12) :
            return 200000

    return 0

def checkIfAllCardsIsBlack(cards) :
    
    cardsBlack = 0
    
    i = 0 
    for i in cards :
        if (i.getSymbol() == 0) or (i.getSymbol() == 1) :
            cardsBlack += 1
        
    if (cardsBlack == 5) :
        return True
    return False
 
def checkIfAllCardsIsRed(cards) :
    
    cardsBlack = 0
    
    i = 0 
    for i in cards :
        if (i.getSymbol() == 3) or (i.getSymbol() == 4) :
            cardsBlack += 1
        
    if (cardsBlack == 5) :
        return True
    return False            
            
def checkPair(cards) :
    i = 0
    # For each card
    for i in range(0,5):
        
        # for et pair + ekstra like kort
        pair_point = 2 
        
        # Check each card
        x = 0
        for x in range(0, 5):
            #ekstra points
            ekstraPoint = 0
            
            # Jump over current card 
            if (x is not i) :
                if (cards[i].getValue() == cards[x].getValue()) :
                    #print "match found!"
                    
                    # Check if the pair is higher than 0 (pair in 2's)
                    if (cards[i].getValue() > 0) : 
                        
                        y = 0    
                        
                        for y in range (0,14) :
                            if (cards[i].getValue() == y) :
                                break
                            else :
                                # Add exstra point
                                ekstraPoint += 1
                    
                    # Add points            
                    return pair_point + ekstraPoint + 100   