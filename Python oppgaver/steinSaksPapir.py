import random

#!/usr/bin/env python
# -*- coding: utf-8 -*-

spiller = raw_input ("stein,saks,papir:")

data = random.random()

if data <=0.33:
    data = "stein"
    
elif data <=0.66:
    data = "papir"
    
else:
    data = "saks"
    

def spill(valgEn,valgTo):
    if valgEn == valgTo:
        print "Du valgte", valgEn
        print "Dataen valgte", valgTo
        print "Det ble likt"
        
    elif valgEn == "stein":
        if valgTo == "saks":
            print "Du valgt", valgEn
            print "Dataen valgte", valgTo
            print "Du vant! Gratulerer"
        
        else:
            print "Du valgt", valgEn
            print "Dataen valgte", valgTo
            print "Du tapte, bedre lykke neste gang!"
            
    
    elif valgEn == "papir":
        if valgTo == "stein":
            print "Du valgt", valgEn
            print "Dataen valgte", valgTo
            print "Du vant! Gratulerer!"
                    
        else:
            print "Du valgt", valgEn
            print "Dataen valgte", valgTo
            print "Du tapte, bedre lykke neste gang!"    
        
        
    elif valgEn == "saks":
        if valgTo == "papir":
            print "Du valgt", valgEn
            print "Dataen valgte", valgTo
            print "Du vant! Gratulerer!"
                    
        else:
            print "Du valgt", valgEn
            print "Dataen valgte", valgTo
            print "Du tapte, bedre lykke neste gang!"    
    
spill(spiller, data)

    
#Håper dette er noe som kan brukes videre folkens!! :D GLHF 

# Jeg tok vekk det ola skreiv, og la inn en variant som regner ut ifra desimal 0-0.33 = Stein, 0.34-0.66 = saks og 0.67-1 = Papir. 
# Nå funker programmet, kanskje ikke optimalt, da det papir har litt ekstra sjans for å bli trukket, men det jeg fikk til. Med litt hjelp fra internett selvfølgelig.