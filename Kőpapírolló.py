prps = 0
arps = 0
prps = int(input("(Kő:1 Papír:2 Olló:3) Írd ide választásod:"))

if prps == 1:
    print ("Követ választottál")
if prps == 2:
    print ("Papírt választottál")
if prps == 3: 
    print ("Ollót választottál")
    
import random

arps = random.randrange(1, 3)

if arps == 1:
    print ("Kőt választott")
    
if arps == 2:
    print ("Papírt választott")
    
if arps == 3:
    print ("Ollót választott")
    
if arps == prps:
    print ("Döntetlen!")
    
if arps == 1 and prps == 3:
    print ("Vesztettél")
    
if arps == 2 and prps == 1:
    print ("Vesztettél")
    
if arps == 3 and prps == 2:
    print("Vesztettél")
    

if arps == 3 and prps == 1:
    print ("Nyertél")
    
if arps == 1 and prps == 2:
    print ("Nyertél")
    
if arps == 2 and prps == 3:
    print ("Nyertél")