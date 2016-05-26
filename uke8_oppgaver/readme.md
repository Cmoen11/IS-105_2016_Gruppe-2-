# Beskrivelse

![En skjermdump av grafen vi fikk når vi kjørte Ica_05.py](https://i.gyazo.com/0881897bcf4aafa71670a754753dbd98.png "En skjermdump av grafen vi fikk når vi kjørte Ica_05.py")


######Ica_05.py
Kjører needle plassering test, og viser da en graf over de ulke testene som ble gått. Når needle plasseringen er like stor som filen. Kan man se en forskjell uansett. Men dette er fordi man aldri vil få en helt gjevn fordeling, altså en rett strek fordi det vil alltid være litt tid som skiller dem begge. Det er derfor så og si tilfeldig hvilken av dem som bruker mer tid. 
######Search.py
Denne inneholder en superklasse til EachLetter og EachWord fra Ica_05.py, dette er for å forbedre litt modulariasjon.
######Test.py
Denne inneholder en test. Her vil den generere en temp fil og sjekke om tidene faktisk er bedre på fast enn fra slow. Her kan man også generere så stor fil som man ønsker. Den vil også putte needle en random posisjon fra 1, 150. 
######File.py
Denne generere filer og legger inn tekst inni dem samt en needle som programmet søker etter. Denne blir foreløbig kun brukt av testklassen. 
