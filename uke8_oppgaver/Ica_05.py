# kilde: http://stackoverflow.com/questions/6963236/python-string-search-efficiency 

# -*- coding: utf-8 -*-

import timeit

prepare = """
with open('shakespare.txt') as fh:
    text = fh.read()
"""

presplit_prepare = """
with open('shakespare.txt') as fh:
    text = fh.read()
lines = text.splitlines()
"""

longsearch = """
'hello' in text
"""

search_slow = """
for line in text.splitlines():
    if 'hello' in line:
        break
"""

search_fast = """
for line in lines:
    if 'hello' in line:
        break
"""




#Leter etter et definert ord i teksten og retunerer dette tiden pcen brukte på å finne dette ordet. 
benchmark = timeit.Timer(longsearch, prepare)
print "Finne første ord derfinert i kode:", benchmark.timeit(1000), "seconds"

# Splitter hvert ord opp, hvis ordet er 'hello' så stopper den. 
benchmark = timeit.Timer(search_slow, prepare)
print "Search-slow :", benchmark.timeit(1000), "seconds"

# Splitter alt opp før den begynner å se etter ordet 'hello'. 
benchmark = timeit.Timer(search_fast, presplit_prepare)
print "Search-fast :", benchmark.timeit(1000), "seconds"