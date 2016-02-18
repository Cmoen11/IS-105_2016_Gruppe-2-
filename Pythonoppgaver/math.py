#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 
tall1 = raw_input("Skriv inn første tall: ")
tall2 = raw_input("Skriv inn andre tall: ")


tall1 = int(tall1)
tall2 = int(tall2)

# Pluss 
def pluss(tall1,tall2) :
    return tall1 + tall2

# Minus
def minus(tall1,tall2) :
    result = tall1 - tall2
    return result 

# Gange
def gange(tall1,tall2) :
    result = tall1 * tall2
    return result 

# Dele 
def dele(tall1,tall2) : 
    result = tall1 / tall2
    return result 
    
# Prosent av ett tall
def prosent(tall1,tall2) :
    result = tall1 / tall2 * 100
    return result 

# print ut alle resultatene
def printResultat() : 
    pluss()
    minus()
    gange()
    dele()
    prosent()
    
printResultat()    
