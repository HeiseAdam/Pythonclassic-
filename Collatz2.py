szam = 0
lepesek = 0
hatarertek = int(input("Kérem a hatzárértéket "))
leghosszabbSzekvencia = -1
leghosszabbSzekvSzam = -1
vizsgaltSzam = 0
legmagasabbSzam = 0
maximumVizsgaltszam = 0
szamlalo = 0

for szamlalo in range (2, hatarertek) :
    while szam > 1:
        if szam % 2 == 0:
            szam = int(szam / 2)
            lepesek = lepesek + 1
        else:
            szam = int((3 * szam) + 1)
            lepesek = lepesek + 1
        
        if lepesek > leghosszabbSzekvencia:
            leghosszabbSzekvencia = lepesek
            leghosszabbSzekvSzam = vizsgaltSzam
            print("Új leghosszabb szekvenciát találtam:", leghosszabbSzekvencia, "A hozzá tartozo szám:", leghosszabbSzekvSzam)
            
        if szam > legmagasabbSzam:
            legmagasabbSzam = szam
            maximumVizsgaltszam = szam
            print ("Új legmagasabb számot találtam:", legmagasabbSzam, "a hozzá tartozó kiindulóérték:", maximumVizsgaltszam)
            
        lepesek = 0
        
print("A leghosszabb sorozat:", leghosszabbSzekvencia, "a hozzá tartozó szam:", leghosszabbSzekvSzam)
print ("A legmagasabb szám:", legmagasabbSzam, "A hozzátartozó kiindulóérték:", maximumVizsgaltszam)