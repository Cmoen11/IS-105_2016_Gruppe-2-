##ICA09 - Kommunikasjonsnettverk</br>
### River crossing spillet

**For å kjøre programmet: </br>**
1. Kjør filen server_launch.py
1. Kjør filen Controlls.py (Starter klient, kan være flere av denne)

![Gif som demonstrerer bruk av programmet](https://i.gyazo.com/cd7066d9f10e0443f774723437c44a11.gif "Bilde av 2 klienter koblet til samme server")</br>
######Gif: 2 klienter som er koblet til samme server. 

Vårt program er laget med en server og kan betjene forespørsler fra flere klienter.</br>
Serveren sin oppgave er å holde tilstanden systemet er i. Så lenge man ikke lukker serveren i programmet, vil klienten starte med programmet i den tilstanden som det ble avsluttet i.</br> Klienten endrer tilstand og holde seg oppdatert på tilstanden i programmet. At klienten er oppdatert på tilstanden viktig når det er flere klienter og en klient gjør en endring. Da må de andre klientene sørge for at de har informasjon om nåværende tilstand i programmet slik at de kan gjøre endringer basert på den.</br>
I vår i kode er det vanskelig for nodene å skille tilstanden. Det vil si at når en klient gjør en endring, så vil de andre klientene oppdateres med tilstand fra server, som dermed setter klienten i gjeldende tilstand. Det er derfor liten sannsynlighet for kollisjoner når tilstanden endres.

![Gif som viser serveren som opprettholder tilstanden til clientene](https://i.gyazo.com/25c25f3de9e73e72733a1c30f7fed326.gif "Bilde av 2 klienter koblet til samme server")</br>
######Gif som viser serveren som opprettholder tilstanden til klientene

Serveren ser ikke ut til å kunne håndtere mer enn fem klienter samtidig. Responstiden fra serveren ble betydelig dårligere allerede når flere enn 2 klienter var involvert. Vi kjørte programmet med 6 klienter på en av våre maskiner, og da klarte ikke den ene klienten å oppdatere seg til riktig tilstand. 

