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

# Dette er Tommy sin versjon. Var ikke sikker på om vi alle skulle jobbe på det sammen eller ikke.
# Ville stått "import random" på toppen. 

dataValg = random.randint (1,3)
spillerVelger = True

if dataValg == 1:
    dataValg = "Stein"
elif dataValg == 2:
    dataValg = "Saks"
elif dataValg == 3:
    dataValg = "Papir"

while spillerVelger == True:
    print("Stein! Saks! Papir! Hva velger du?")
    spillerValg input()
    if spillerValg == "Stein":
        print("Du har valgt stein!")
        spillerValg = "Stein"
        spillerVelger = False
    elif spillerValg == "Saks":
        print("Du har valgt saks!")
        spillerValg= "Saks"
        spillerVelger = False
    elif spillerValg == "Papir":
        print("Du har valgt papir!")
        spillerValg = "Papir"
        spillerVelger = False
    else:
        print("Det er ikke et valg!")
        spillerVelger = True

input()

print ("Din motstander valgte " +dataValg+ "!")

input()

if spillerValg == "Stein" and dataValg == "Papir":
    print("Du tapte!")
elif spillerValg == "Saks" and dataValg == "Stein":
    print("Du tapte!")
elif spillerValg == "Papir" and dataValg == "Saks":
    print("Du tapte!")
elif spillerValg == "Stein" and dataValg == "Saks":
    print("Du vant!")
elif spillerValg == "Saks" and dataValg == "Papir":
    print("Du vant!")
elif spillerValg == "Papir" and dataValg == "Stein":
    print("Du vant!")
elif spillerValg == "Stein" and dataValg == "Stein":
    print("Uavgjort!")
elif spillerValg == "Saks" and dataValg == "Saks":
    print("Uavgjort!")
elif spillerValg == "Papir" and dataValg == "Papir":
    print("Uavgjort!")
    
    