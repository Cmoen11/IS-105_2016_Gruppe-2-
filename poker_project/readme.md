

## Synopsis
::Poker:: 
Hovedfilen er poker.py
Utrengningen av poeng ligger i pointcalc_poker
utregningen av vinner skjer i calculate winner.
Testklasser kan du finne i PokerTestC.py


Programmet er skrevet 100% av gruppe 2 og vi prøver å holde det på den måten for å lære mest mulig om programmet vårt og lære python mest mulig. 

I dette programmet blir det laget objekter av player og pokercards, men isenere tidpunkt funnet ut at funksjoner er mest egnet, fordi akkurat med det å programmere til webapplikasjoner kan være problematisk med objekter. 
# Det med store datamengder ^.

Poker.py
*GenerateCards* tar i utgangspunkt å generere alle kortene som trengs for å kunne gjennomføre et spill. 
*deal* oppretter spillere og deler ut kortene til spillerene

pointcalc_poker.py
*calculatePoints* Vil kjøre igjennom alle metodene fra stigende rekkefølge(altså fra royalflush og nedover), og returnere poengsummen for den hånden vedkommende har. 

CalculateWinner.py
*CalculateWinner* Vil kalkulere vinnerne bassert på hvilken poengsum hånden til spilleren har fått av pointcalc_poker.py.

## En mer detaljert beskrivelse


## Tests

Describe and show how to run the tests with code examples.
