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

splitsearch = """
for line in text.splitlines():
    if 'hello' in line:
        break
"""

presplitsearch = """
for line in lines:
    if 'hello' in line:
        break
"""

#Leter etter et definert ord i teksten og retunerer dette tiden pcen brukte på å finne dette ordet. 
benchmark = timeit.Timer(longsearch, prepare)
print "Finne første ord derfinert i kode:", benchmark.timeit(1000), "seconds"

#
benchmark = timeit.Timer(splitsearch, prepare)
print "IN on splitted string takes:", benchmark.timeit(1000), "seconds"


benchmark = timeit.Timer(presplitsearch, presplit_prepare)
print "IN on pre-splitted string takes:", benchmark.timeit(1000), "seconds"