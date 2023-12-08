hatarertek = int(input("Kérem a hatzárértéket "))
leghosszabbSzekvencia = -1
leghosszabbSzekvSzam = -1
maximumVizsgaltszam = 0

for vizsgaltSzam in range(2, hatarertek):
    szam = vizsgaltSzam
    lepesek = 0

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
            print("Új leghosszabb szekvenciát találtam:", leghosszabbSzekvencia, "A hozzá tartozó szám:", leghosszabbSzekvSzam)

        if szam > maximumVizsgaltszam:
            maximumVizsgaltszam = szam
            print("Új legmagasabb számot találtam:", maximumVizsgaltszam, "a hozzá tartozó kiindulóérték:", vizsgaltSzam)

print("A leghosszabb sorozat:", leghosszabbSzekvencia, "a hozzá tartozó szam:", leghosszabbSzekvSzam)
print("A legmagasabb szám:", maximumVizsgaltszam, "A hozzátartozó kiindulóérték:", leghosszabbSzekvSzam)