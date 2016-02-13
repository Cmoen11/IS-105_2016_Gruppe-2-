## ICA uke 6<br />
**Oppgave** 1.2.1

**a)**
Table 1 = A, Table 2 = B, Table 3 = C

|Motatt | String Table | Dekodet |
|-------|:----------:|--------:|
|2  |Table 2 |B |
|3 |Table 4 [bc] |C |
|3 |Table 5 [cc] |C |
|1 |Table 6 [ca] |A |
|3 |Table 7 [ac] |C |
|4 |Table 8 [cb] |BC |
|5 |Table 9 [bcc] |CC |
|10 |Table 10 [ccc] | CCC |
|11 |Table 11 [cccc] |CCCC |
|6 |Table 12 [ccccc] |CA |
|10 |Table 13 [accc] |CCC |
|1 |Table 1 |A |

**Koden blir da**: B C C A C B C C C C C C C C C C C C A C C C A

Noen ASCII tabeller gir uttrykk for at hvert symbol består av 7 bits, mens i teksten fra uke 5 står det at det er 8 bits. Vi tar derfor utgangspunkt i at det er 8 bits. 
Dette gir oss da – 168 bits når hvert symbol 8 bits.

**b)** Se github, oppgave 1,2,1.py (øverste del av koden)

**c)** Vi klarte å endre på koden før vi husket å skrive ned komprimeringsgraden, og på grunn av stort tidforbruk valgte vi derfor å ikke besvare denne oppgaven. Men vi har beregnet komprimeringsgrad i de andre oppgavene. Så det bør vise at vi kan det.<br />
Se oppgave f).

**d)** Huffman kode: <br />
B C C A C B C C C C C C C C C C C A C C C A<br />
A forekommer 3 ganger, B forekommer 2 ganger og C forekommer 17 ganger<br />
Det gir en sannynlighet på:<br />
C = 0.77, A = 0.13, B = 0.1

![alt text](https://github.com/Cmoen11/IS-105_2016_Gruppe-2-.git/IS-105_2016_Gruppe-2-/Bilderfiler/Huffman_tre.png "Huffman_kode")
C = 0, A = 10, B = 11<br />
Koden blir da: 110010011000000000001000010 = 27 bits<br />
Original melding var på 168 bits, og vi har med Huffman koding fått en komprimeringsgrad ca 84%<br />

**e)** Koden vi brukte til å oversette oppgave b) har blitt endret til å utføre koding av Hamlet / Shakespear. <br />
Denne koden kan foreløpig bare kode og ikke dekode. Se fil i "uke6_oppgaver"<br />

**f)** Resultater av komprimering: <br />
Hamlet original størrelse = 180kb<br />
Hamlet dekoda uten (4095 plasser i tabellen før den ble satt til 0) = 183kb<br />
Hamlet dekoda med (4095 plasser i tabellen før den ble satt til 0) = 219kb<br />
Hamlet dekoda med (6095 plasser i tabellen før den ble satt til 0) = 209kb<br />
Hamlet dekoda med (10095 plasser i tabellen før den ble satt til 0) = 198kb<br />
Hamlet dekoda med (15095 plasser i tabellen før den ble satt til 0) = 194kb<br />
Shakespeare original størrelse = 2080kb<br />
Shakespeare dekodas størrelse med (4095 plasser i tabellen før den ble satt til 0) = 2448kb<br />
Shakespeare dekoda størrelse med (1024 plasser i tabellen før den ble satt til 0) = 2891kb<br />


**Komprimeringsgraden ble:**<br />
Hamlet ble + 101,02% (1,02% større)<br />
Shakespeare ble 101,8% (1,8% større)<br />
Vi valgte og ikke kjøre Shakespeare uten noe resetting av listen, fordi dette ville tatt for lang tid, hadde vi gjort dette, så ville mest sannsynlig filen blitt mindre en originalen. 
<br />
Dess større fila er, jo flere entries vil man få i tabellen. Og komprimeringen vil dermed bli mer effektiv grunnet programmets mulighet for å hente ut ord i tabellen. 
Med hensyn til oppgave c) - her er teksten så liten at LZW metoden vil være ineffektiv.
