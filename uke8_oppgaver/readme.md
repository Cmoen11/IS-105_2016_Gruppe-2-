# Beskrivelse

![En skjermdump av grafen vi fikk når vi kjørte Ica_05.py](https://i.gyazo.com/0881897bcf4aafa71670a754753dbd98.png "En skjermdump av grafen vi fikk når vi kjørte Ica_05.py")
En skjermdump av grafen vi fikk når vi kjørte igjennom Ica_05.py, vi kan se her at fast er raskere enn slow på 'nesten' alle punkter. Utifra koden, slow. Må man kjøre igjennom hele løkka før man vet om needlen er i listen. Men i fast metoden, så vil den stoppe når den har funnet needlen. Det ser på digrammet også. Her ser vi at om needlen er plassert på et punkt i lista, så tar denne mindre tid enn slow metoden.

Vi ser også at om needlen er plassert helt på slutten, vil man bruke så og si samme tid, fordi da er begge metodene nødt til å søke igjennom hele listen for å finne needlen. 

```python
# Search fast method
 def search_fast(self):
        for item in self.prepare:                               # Go trough every symbol in the list
            if item == self.needle:                             # check if the symbol match the needle
                return True                                     # Return true if the needle is founded
        return False                                            # Return false if the needle is not found

#search slow method    
def search_slow(self):
        return_value = False                                    # If results is found
        for item in self.prepare:                               # go trough every symbol in prepare
            if item == self.needle:                             # check if the symbol match the needle
                return_value = True                             # set the boolean to true if found
        return return_value                                     # return the boolean
```


######Ica_05.py
Kjører needle plassering test, og viser da en graf over de ulke testene som ble gått. Når needle plasseringen er like stor som filen. Kan man se en forskjell uansett. Men dette er fordi man aldri vil få en helt gjevn fordeling, altså en rett strek fordi det vil alltid være litt tid som skiller dem begge. Det er derfor så og si tilfeldig hvilken av dem som bruker mer tid. 
######Search.py
Denne inneholder en superklasse til EachLetter og EachWord fra Ica_05.py, dette er for å forbedre litt modulariasjon.
######Test.py
Denne inneholder en test. Her vil den generere en temp fil og sjekke om tidene faktisk er bedre på fast enn fra slow. Her kan man også generere så stor fil som man ønsker. Den vil også putte needle en random posisjon fra 1, 150. 
######File.py
Denne generere filer og legger inn tekst inni dem samt en needle som programmet søker etter. Denne blir foreløbig kun brukt av testklassen. 
