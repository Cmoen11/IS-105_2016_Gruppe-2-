# Beskrivelse

![En skjermdump av grafen vi fikk når vi kjørte Ica_05.py](https://i.gyazo.com/0881897bcf4aafa71670a754753dbd98.png "En skjermdump av grafen vi fikk når vi kjørte Ica_05.py")
En skjermdump av grafen vi fikk når vi kjørte igjennom Ica_05.py. </br>
Grafen viser at "fast" er raskere enn "slow" på nesten alle punkter. Når needlen er plassert midt i listen tar det lenger tid å kjøre "slow" enn "fast" metoden. Dette fordi "slow" kjører gjennom hele løkka før den fortelle om needlen er i listen. Mens fast metoden stopper når den har funnet den. </br>
Vi ser også at dersom needlen er plassert helt på slutten i listen, vil man bruke så og si samme tid, fordi begge metodene vil måtte  søke igjennom hele listen for å finne needlen. 

```python
# Search fast method
 def search_fast(self):
        for item in self.prepare:                               # Go trough every symbol in the list
            if item == self.needle:                             # check if the symbol match the needle
                return True                                     # Return true if the needle is founded
        return False                                            # Return false if the needle is not found
```
Koden viser at vi returnere funn med en gang programmet finner needlen.

```python
#search slow method    
def search_slow(self):
        return_value = False                                    # If results is found
        for item in self.prepare:                               # go trough every symbol in prepare
            if item == self.needle:                             # check if the symbol match the needle
                return_value = True                             # set the boolean to true if found
        return return_value                                     # return the boolean
```
Her returneres resultatet når programmet har kjørt gjennom hele listen. 

######Ica_05.py
Kjører needle-plasserings test og viser en graf over de ulike testene som ble gjennomført.</br> Når needle plasseringen er like stor som filen kan man se en forskjell uansett. Men dette er fordi man aldri vil få en helt jevn fordeling, altså en rett strek fordi det vil alltid være litt tid som skiller dem begge. Det er derfor så og si tilfeldig hvilken av metodene som bruker mest tid. 
######Search.py
Inneholder en superklasse for EachLetter og EachWord fra Ica_05.py, dette er for å forbedre modularisering.
######Test.py
Inneholder en test. Her vil den generere en temp fil og sjekke om tidene faktisk er bedre på fast enn fra slow. Her kan man også generere så stor fil som man ønsker. Den vil også putte needle en random posisjon fra 1, 150. 
######File.py
Denne generere filer og legger inn tekst inni dem samt en needle som programmet søker etter. Denne blir foreløbig kun brukt av testklassen. 
