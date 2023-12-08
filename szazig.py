felsohatar = 0
alsohatar = 0
osszeg = 0

alsohatar = int(input("Kérem a sororzat alsó határát: "))
felsohatar = int(input("Kérem a sororzat felső határát: "))

szamossag = felsohatar - alsohatar

osszeg = ((alsohatar + felsohatar)* szamossag) / 2

print ("A sorozat elemeinek összege: ", osszeg)