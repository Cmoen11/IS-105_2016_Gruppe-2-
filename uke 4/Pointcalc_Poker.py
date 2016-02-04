def calculatePoints(cards) :
    '''
    this method will return back a 'score' of the selected score, in order to find the winner.
    '''
    #Score given:
    points = 0;
    
    '''
    Run trought every "hand" you can get, from the highest to the lowest. Stop when you've reached the higest hand
    and return the points
    '''
    # Royal flush check
    points = checkRoyalFlush(cards)          # Value given if found is 500 000
    if (points > 0 ) :
        return points
     
    #Straight Flush check
    points = checkStraightFlush(cards)          # Value given if found is 480 000
    if (points > 0 ) :
        return points    
        
    #Four like check
    points = checkFourLike(cards)           # Depends on value of the cards.. 
    if (points > 0 ) :                      
        return points       

    #Full house check 
    points = checkFullHouse(cards)          # Depends on value of the cards.. 
    if (points > 0 ) :  
        return points
    
    #Flush check
    points = checkFlush(cards)              # Value given if found is 120 000
    if (points > 0):
        return points
    
    #Sraight check
    points = checkStraight(cards)           # Value given if found is 100 000
    if (points > 0):
        return points
    
    #three like check
    points = checkThreeLike(cards)          # Value given if found is 80 000
    if (points > 0):
        return points    
    
    # pair of 2's check 
    points = checkPair(cards)               # Depends on value of the cards.. 
    if (points > 0) :
        return points
    
    else :
        return 0                            # Player has not got any hand of value
    
    
def checkStraightFlush (cards):
    #Sort the cards
    cards = sorted(cards)
    
    #Check the colour of the card
    color = checkIfAllCardsIsBlack(cards) # if all the cards colour is black
    
    if (color is False) :   # If the colour is not black, check if all is red 
        color = checkIfAllCardsIsRed(cards)
    
    # Check if is a straight flush  
    if (cards[0].getValue() == 4) \
       and (cards[1].getValue() == 5) \
       and (cards[2].getValue() == 6) \
       and (cards[3].getValue() == 7) \
       and (cards[4].getValue() == 8) :
        return 480000
    return 0
def checkFourLike(cards) :
    i = 0
    ekstraPoint = 0
    # Go trough each card value and see if any of them are alike. Add also 20 exstra points for each run, so higher card values give higher score
    for i in range(0,12):
        if (cards[0].getValue() == i) and (cards[1].getValue() == i) and (cards[2].getValue() == i) and (cards[3].getValue() == i) and (cards[4].getValue() == i):
            return 460000 + ekstraPoint
        else:
            ekstraPoint += 20
            
    return 0
def checkFullHouse(cards) : 
    return 0
def checkFlush(cards) :
    return 0
def checkStraight(cards) :
    return 0
def checkThreeLike(cards) :
    return 0
def checkRoyalFlush (cards) :
    
    #Sort the cards
    cards = sorted(cards)
    
    #Check the colour of the card
    color = checkIfAllCardsIsBlack(cards) # if all the cards colour is black
    
    if (color is False) :   # If the colour is not black, check if all is red 
        color = checkIfAllCardsIsRed(cards)
    
    
    if (color) : # if either all of the cards is red or black
        #Check if is royal flush

        if (cards[0].getValue() == 8) \
            and (cards[1].getValue() == 9) \
            and (cards[2].getValue() == 10) \
            and (cards[3].getValue() == 11) \
            and (cards[4].getValue() == 12):            
            print "Hey!"
            return 500000
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