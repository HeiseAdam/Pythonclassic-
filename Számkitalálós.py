szamkitalalo = 0

import random

szamkitalalo = random.randrange(1, 100)

teszamod = int(input("Add meg a te szamod (1-100): "))

tipp = szamkitalalo

while szamkitalalo != teszamod:
    if szamkitalalo != teszamod:
        print ("Nem talatam ki :(")
    teszamod = int(input("Add meg újra (1-100): "))
    if tipp < teszamod:
        print ("A gondolt szam KISEBB") 
    if tipp > teszamod:
        print ("A gondolt szam NAGYOBB") 

if szamkitalalo == teszamod:
    print("Kitaláltam :D")