import random

kihuzottSzamok = []
lottoGomb = []
tipp = []

for i in range(0, 5):
    szam = int(input("Kérek egy 1 és 90 közötti számot: "))
    tipp.append(szam)

for i in range(1, 91):
    lottoGomb.append(i)

print("Az összes szám a lottó golyók között:", lottoGomb)
print("****************************************************************")

random.shuffle(lottoGomb)
print("Összekevert lottó golyók:", lottoGomb)

for i in range(0, 5):
    kihuzottSzamok.append(lottoGomb[i])

print("A kihúzott számok:", kihuzottSzamok)
print("****************************************************************")

print("Az ön tippje:", tipp)
print("A kihúzott számok:", kihuzottSzamok)