##ICA09 - Kommunikasjonsnettverk</br>
### River crossing spillet

For å kjøre programmet: 
1. Start serveren
2. Kjør filen server_launch.py
3. tart Client, kan være flere av denne
4. kjør filen Controlls.py

![Gif som demonstrerer bruk av programmet](https://i.gyazo.com/cd7066d9f10e0443f774723437c44a11.gif "Bilde av 2 klienter koblet til samme server")</br>
2 klienter som er koblet til samme server. 

Serveren sin oppgave i programmet er å holde tilstanden systemet er i. Klienten skal endre tilstand og holde seg oppdatert på tilstanden i programmet. Dette gjelder når det er flere klienter og en klient gjør en endring. Da må de andre klientene sørge for at de har informasjon om nåværende tilstand i programmet slik at de kan gjøre endringer basert på den tilstanden.
Dersom nodene (
