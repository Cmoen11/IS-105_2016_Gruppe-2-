#Fillagringssystem:
Vi har brukt Array for å holde på alle blokkene. Arrayen inneholder 32 block spaces (linjer)<br/>
Hver block kan inneholde 8 bits (1 byte).<br/>
Selv om en fil kun inneholder 4 bits tar den i denne modellen hele block space på 8 bits. <br/>
![alt text](https://i.gyazo.com/fe389632d324034f4e7f85c8b8b5f039.png "Lite screenshot fra bash")

Dette er fordi man tilegner hver blokk metadata. Om man fyller halvfylte blokker med ny informasjon for å fylle blokken, vil da metadataen ikke fungere og man vil få problemer med å hente filen etterpå. 
##Mappestruktur: 
Blokker har ikke blitt tilegnet en mappe før de først er skrevet på. Det som kartlegger hvilken blokk som tilhører hvilken mappe er at de har metadata som head_dir. Head_dir oppgir da adressen (index) til mappeblokken, altså den mappen blokken tilhører. Mappen har også en metadata som sier hvilke blokker som den har kontroll over. Mappe blokker har igjen en metadata “head_dir”, som forteller hvilken mappe som kontrollerer den neste mappen. Denne head_dir fungerer som ett “directory-tre”. Som viser hvor i mappestrukturen man befinner seg.<br/>
##Sletting: 
Når man sletter en fil fra systemet, blir ikke filen fysisk fjernet. Men blokkenes availability blir satt fra False til True. Og fjerner blokk visability fra mappestrukturen, slik at filen ikke lenger blir synlig.<br/>
Dette gjør det mulig å overskrive innholdet i blokkene. Vi har ikke laget en gjenopprettingsfunksjon i dette systemet, da vi anser dette å være “ekspert” kunnskap.<br/>

##Skriving
Når man legger til en mappe eller filer, blir det skrevet inn til ledige blokker. Ledige blokker blir funnet bed at man benytter seg av get_available_block til å søke igjennom blokkene og lager da en array med adresser(indexer) som man kan skrive til. Dette blir regelmessig sjekket. <br>

Er det ikke plass på disken vil den ikke starte å skrive, den sjekker først om det er plass til å skrive, er det ikke plass vil den gi brukeren beskjed. 

##Bash(Commands.py):
Vi har laget en bash for systemet. <br/>
Dette fungerer nesten som “command prompt” i Windows, men med litt annerledes kommandoer. <br/>
Dette har vi gjort for å demonstrere hva som er mulig å gjøre med vårt filsystem.<br/>
I Bash kan man f.eks opprette filer og mapper, navigere rundt i mappehierarkiet, slette og flytter filer og mapper.<br/>
###Kommandoer i Bash:
**dir:** Liste opp alle filer og mapper i mappen man er i, pr nå lister den alle blokker i mappen, dette for å vise mer hvordan det blir lagret på hardisken.<br/>
**-a dir:** Lister opp alle blokkene på hele hardisken, uavhengig av hvilken mappe man er i.<br/>
**cd:** Gå inn i mapper fra posisjonen du er i nå. <br/>
**cd .. :** Gå tilbake i den mappen du var i.<br/>
**file create:** Skriv inn en ny fil til den posisjonen du er i.<br/>
**dir create:** Oppretter en mappe på den posisjonen du er i.<br/>
**dir delete:** Sletter en mappe på den posisjonen du er på.<br/>
**file delete:** Sletter en fil på den posisjonen du er på.<br/>
**file open:** Åpner en fil fra den posisjonen du er på. <br/>
**file move:** Flytter filen til en annen posisjon på disken (enda ikke implementert.)<br/>

##Metoder i Python programmet(harddrive.py): 
**add**<br/>
Legger til ny fil<br/>
**create_empty_blocks**<br/>
lager tomme blokker før de blir skrevet til<br/>
**get_available_block**<br/>
Gir oversikt over ledige blokker<br/>
**delete_file**<br/>
Sletter fil<br/>
**add_block**<br/>
Legger inn tomme blokker<br/>
**open_directory**<br/>
Viser hva som er i en mappe<br/>
**open_file**<br/>
Åpner en fil. Returnerer det som er inni filen.<br/>
**write**<br/>
Skriver ny informasjon til block<br/>
**create_dir**<br/>
Oppretter directory<br/>
**delete_dir**<br/>
Sletter directory<br/>
**del_block**<br/>
Sletter innhold i blokk. Setter “available” fra False til True. Gjør det mulig å overskrive innhold.<br/>
**clean_block**<br/>
Fjerner alt innhold i blokken. Utføres kun ved sletting av mapper<br/>
**go_inside_directory**<br/>
Går inn i directory. Men må følge stien. Kan ikke hoppe til annet directory.<br/>
**go_outside_directory**<br/>
Går tilbake på stien.<br/>
**move_file**<br/>
Flytter fil til annen plass.<br/>
