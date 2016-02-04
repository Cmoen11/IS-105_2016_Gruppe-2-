def calculatePoints(cards) :
    '''
    this method will return back a 'score' of the selected score, in order to find the winner.
    '''
    
    
    #Score given:
    points = 0;
    
    # for et pair + ekstra like kort
    pair_point = 2
    
    '''
    PAIR of 2's give 2 points + 2 for every exstra card /// + 1 point for every number higher than this.
    
    
    '''
    
    checkPair()
    
    
                    
    
    return points;





def checkPair() :
    i = 0
    # For each card
    for i in range(0,5):
        x = 0
            
        # Check each card
        for x in range(0, 5):
            #ekstra points
            ekstraPoint = 0;
                
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
         
                    points += pair_point + ekstraPoint;    