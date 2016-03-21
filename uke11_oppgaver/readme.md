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
Når man legger til en mappe eller filer, blir det skrevet inn til ledige blokker. Ledige blokker blir funnet ved at man benytter seg av get_available_block til å søke igjennom blokkene og lager da en array med adresser(indexer) som man kan skrive til. Dette blir regelmessig sjekket. <br> Når en fil er skrevet, vil mappeindexen bli lagret som en metadata i blokken(e) som filen er lagret i. Samtidig vil modermappen også få adressene(indexene) lagt til. <br>

Er det ikke plass på disken vil den ikke starte å skrive, den sjekker først om det er plass til å skrive, er det ikke plass vil den gi brukeren beskjed. 

##Bash(Commands.py):
Vi har laget en bash for systemet. <br/>
Dette fungerer nesten som “command prompt” i Windows, men med litt annerledes kommandoer. <br/>
Dette har vi gjort for å demonstrere hva som er mulig å gjøre med vårt filsystem.<br/>
I Bash kan man f.eks opprette filer og mapper, navigere rundt i mappehierarkiet, slette og flytter filer og mapper.<br/>
###Kommandoer i Bash:
| Kommando          | Beskrivelse     |
| ------------- |:-------------:|
|dir | Liste opp alle filer og mapper i mappen man er i, pr nå lister den alle blokker i mappen, dette for å vise mer hvordan det blir lagret på hardisken.|
|-a dir|Lister opp alle blokkene på hele hardisken, uavhengig av hvilken mappe man er i.|
|cd|Gå inn i mapper fra posisjonen du er i nå.|
|cd ..|Gå tilbake i den mappen du var i.|
|file create|Skriv inn en ny fil til den posisjonen du er i.|
|dir create|Oppretter en mappe på den posisjonen du er i.|
|dir delete|Sletter en mappe på den posisjonen du er på.|
|file delete|Sletter en fil på den posisjonen du er på.|
|file open|Åpner en fil fra den posisjonen du er på.|
|file move|Åpner en fil fra den posisjonen du er på.|
|file rename|Endrer filnavnet på oppgitt fil.|
|dir rename| Endrer navnet på mappen|


##Metoder i Python programmet(harddrive.py): 
| metodenavn          | Beskrivelse     |
| ------------- |:-------------:|
|add|Legger til ny fil|
|create_empty_blocks|lager tomme blokker før de blir skrevet til|
|get_available_block|Gir oversikt over ledige blokker som programmet bruker til å skrive nye blokker til|
|delete_file|Sletter fil fra systemet dvs. setter blokken til ledig, slik at den kan bli skrevet over igjen.|
|add_block|Legger inn tomme blokker, altså - slik at programmet har noen blokker å skrive til.|
|open_directory| Gir en oversikt over alle blokker som mappen du er inni i har kontroll over|
|open_file|Åpner en fil. Returnerer det som er inni filen.|
|write|Skriver ny informasjon til block|
|create_dir| Oppretter en ny mappe i den mappen du er i.|
|delete_dir| Sletter en mappe som ligger i samme mappe du er i|
|del_block| Sletter innhold i blokk. Setter “available” fra False til True. Gjør det mulig å overskrive innhold.|
|clean_block|Fjerner alt innhold i blokken. Utføres kun ved sletting av mapper, dette fordi metadataen er forksjellig fra filer til mapper|
|go_inside_directory|Går inn i directory. Men må følge stien. Kan ikke hoppe til annet directory.|
|go_outside_directory| Går tilbake på stien.|
|move_file|Flytter fil til annen plass.|
|rename_file|Endrer navnet på filen. |
|rename_dir| endrer navnet på mappen.|

