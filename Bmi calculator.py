Magassag = float(input("Adja meg a magasságát (cm) "))
Tomeg = float(input("Adja meg a tömegét (kg) "))
MeterMagassag = Magassag / 100

BMI = Tomeg / (MeterMagassag * MeterMagassag)

print (BMI, "kg/m^2 vagy, ami:")

if BMI < 0:
    print ("Ön nem valódi")
elif BMI > 0 and BMI < 18.5 :
    print ("Túl vékony vagy")
elif BMI >= 18.5 and BMI < 24.9:
    print ("Ön ideális")
elif BMI > 24.9 and BMI <= 34.9:
    print ("Ön túlsúlyos")
elif BMI > 34.9 and BMI <= 39.9:
    print ("Ön súlyosan elhízott")
elif BMI >= 40 and BMI < 205:
    print ("Ön Morbidan elhízott")


if BMI > 205:
    print ("Ön nem ember")

print ("Ez csak iránymutatás, nem sértés, és az izmot nem számítja bele")