##ICA09 - Kommunikasjonsnettverk</br>
### River crossing spillet

**For å kjøre programmet: </br>**
#### Start serveren
1. Kjør filen server_launch.py - (Starter Client, kan være flere av denne)
1. Kjør filen Controlls.py

![Gif som demonstrerer bruk av programmet](https://i.gyazo.com/cd7066d9f10e0443f774723437c44a11.gif "Bilde av 2 klienter koblet til samme server")</br>
######Gif: 2 klienter som er koblet til samme server. 

Vårt program er laget med en server og to klienter.</br>
Serveren sin oppgave i programmet er å holde tilstanden systemet er i. Så lenge man ikke lukker serveren i programmet, vil klienten starte med programmet i den tilstanden som det ble avsluttet.</br> Klienten skal endre tilstand og holde seg oppdatert på tilstanden i programmet. Dette gjelder når det er flere klienter og en klient gjør en endring. Da må de andre klientene sørge for at de har informasjon om nåværende tilstand i programmet slik at de kan gjøre endringer basert på den tilstanden.</br>
I vår i kode er det vanskelig for nodene å skille tilstanden. Det vil si at når en klient gjør en endring, så vil de andre klientene oppdateres med tilstand fra server, som dermed setter klienten i gjeldende tilstand.
