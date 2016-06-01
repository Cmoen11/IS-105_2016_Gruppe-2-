

# Kort beskrivelse av poker og litt informasjon
Hovedfilen er poker.py<br />
Utrengningen av poeng ligger i pointcalc_poker.<br />
utregningen av vinner skjer i calculate winner.<br />
Testklasser kan du finne i PokerTestC.py<br />


Programmet er skrevet av gruppe 2  og er ett originalt prosjekt laget fra bunnen av. Vi ønsker å skrive så mye som mulig selv, for å å lære mest mulig om programmet vårt og lære python mest mulig. 

I dette programmet blir det laget objekter av "player" og "pokercards", men vi har i ettertid funnet ut at funksjoner er mest egnet, fordi å programmere til webapplikasjoner kan være problematisk med objekter. 

Poker.py
*GenerateCards* genererer alle kortene som trengs for å kunne gjennomføre et spill. <br />
*deal* oppretter spillere og deler ut kort.

pointcalc_poker.py
*calculatePoints* Kjører gjennom alle metodene fra royalflush og videre, og returnerer en poengsum for den hånden spillerne har. 

CalculateWinner.py
*CalculateWinner* Kalkulerer vinner basert på poengsummen hånden til spilleren har fått av pointcalc_poker.py.

## En mer detaljert beskrivelse

Nøkkelvariabler som er verdt å merke seg: 
Pokerhånd rangeres ved bruk av en poengskala. Disse poengene er ikke synlige for spillerne, men brukes av systemet til avgjøre hvilken hånd spilleren har og hvilken hånd som er best. Denne blir lagt til spillerobjektet når kortene blir utdelt. 

Først opprettes x antall decks/kortstokker på 52 kort i generateCards, hvert kort blir da et objekt av PokerCard. Hvert kort får 2 ulike variabler som bestemmer hva kortet er. Det ene er "Value", som måles fra 0 - 12, da 0 = 2 i kortsammenhenger (mer om dette kan man se i diagrammet under), den andre er "Symbol" som går fra 0 - 3(også definert under).

Deretter blir array'en sendt videre til "deal"-metoden, "deal"-metoden har som oppgave å dele ut kort til spillerne. Foreløpig blir spillerne også generert her. Dette vil på ett senere tidspunkt bli implementert i "deal", da spillerobjektene bør defineres tidligere når vi skal koble dette videre mot et virkelig spill senere i prosessen.<br />
I "deal" får hver spiller tildelt 5 kort hver fra kortstokken som ble generert i "generateCards", og blir dermed lagt inn i spillerobjektet til hver av spillerne. Her vil også "Pointcalc_Poker" tre inn. Denne metoden vil finne ut hvilken poengsum som finnes i hver tildelte hånd. Denne metoden vil kjøres på hver spiller og returnerer en poengsum basert på spillerens tildelte hånd. Denne poengsummen blir ikke synlig for spillerne, det er kun en poengskala som brukes av systemet for å kalkulere hvilken spiller som er vinner. <br />
Etter dette blir spillerne printet ut med sine kort og en vinner vil bli trukket basert på poengscoren spillerens hånd har fått. Dette gjøres gjøres på den måten at spillerprofilene blir sendt inn i "CalculateWinner.py" i metoden "CalculateWinner" der systemet samler spillerne i en liste og printer ut fra høy til lav poengsum, og returnerer spilleren med høyest score. <br />
Det er foreløpig ikke lagt opp til at flere spillere kan får samme score. Da den nå vil konkludere med at spilleren som havner på toppen av listen vil vinne. Dette vil bli endret i senere versjoner av spillet.

## Metode definisjoner / Klasser

<b> class Player </b> <br />
En beskrivelse av hvordan hver spiller skal fremstilles og hvilke variabler den skal inneholde. <br />
Hver spiller får hvert sitt objekt av "Player", som skal holde styr på hånden til spilleren og playerscore. Denne klassen inneholder også metoder som kan gi navn på en hånd i poker, som blir brukt til å presentere spillet til brukeren.
<br /><br />
<b> class PokerCard </b><br />
En beskrivelse av hvordan et kort skal fremstilles.<br />
Hvert kort krever 2 parametere for å kunne opprette et objekt. De to parameterene er "Value" og "Symbol": "value" står for hvilken verdi kortet har, mens "symbol" står for hvilken type kortet er. Under dette innlegget får du en bedre definisjon på bestemmelsene for dette. 
<br /><br />
<b> def generateCards </b><br />
Metoden genererer x antall kortstokker(deck), avhengig av hvilken informasjon som er gitt. Den vil lage 13 kort av hvert "symbol"(sjanger på kortet) per kortstokk og returnerer kortstokken som genereres. 
<br /><br />
<b> def deal</b><br />
Oppretter spillerobjektene og deler ut kort fra toppen av bunken til spillerene. <br />
Det er kun midlertidig at spillerobjektene blir opprettet fra denne metoden. Dette vil bli endret når det er faktiske spillere som blir med på "bordet". 
<br /><br />
<b> def calculatePoints</b><br />
Går igjennom alle muligheter for å finne ut hvilken hånd spilleren har fått og den returnerer rangeringen hånden har. <br />
I dette tilfellet har vi gitt det navnet poeng. Poeng vil ikke bli synlig for spilleren, men brukes for å indikere hvilken hånd som er best. Jo høyere poengsum, dess bedre er hånden. 
<br /><br />
<b> def checkIfAllCardsIsBlack</b><br />
Sjekker om alle kortene har enten symbol 0 (Spar) eller 1 (Kløver)
<br /><br />
<b> def checkIfAllCardsIsRed</b><br />
Sjekker om alle kortene har enten symbol 2 (Hjerter) eller 3 (Ruter)
<br /><br />
<b> def checkForSameType</b><br />
Sjekker om alle symbolene til kortene er like. f.eks at alle har 0 (Spar) som symbol.
<br /><br />
<b> def checkForSameType</b><br />
Sjekker om alle symbolene til kortene er like. f.eks at alle har 0 som symbol.
<br /><br />
<b> def sortList</b><br />
Returnerer listen tilbake, rangert lavest til høyest
<br /><br />
<b> Resten av check-metodene</b><br />
Sjekker om kortetene utgjør en godkjent hånd i poker, og returner en 'score' for dette.
<br /><br />
<b> def CalculateWinner</b><br />
Denne metoden er lokalisert i CalculateWinner.py, og sorterer listen etter høyest poengscore og returnerer da det vinnende spillerobjektet.
<br /><br />

### Value og symbol definisjoner: 
| Tall          | Value           | Symbol  |
| ------------- |:-------------:| -----:|
0 | 2 | ♠ Spar |
1 | 3 | ♣ Kløver |
2 | 4 | ♥ Hjerter |
3 | 5 | ♦ Ruter |
4 | 6 | ... |
5 | 7 | ... |
6 | 8 | ... |
7 | 9 | ... |
8 | 10 | ... |
9 | knekt | ... |
10 | Dronning | ... |
11|Konge | ... |
12|Ess (Ace) | ... |



Testing er blitt gjort i modulen PokerTestC.py
