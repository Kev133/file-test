
# nacteni dat
mojedata = open("data.txt", "r")
seznam_str = mojedata.read().splitlines()
pocet_radku = len(seznam_str)

# loop pro převedení str v seznamu na float, urcite jde i nějak lip
# funkce pro prevedeni dat ze souboru do seznamu rovnou v int, popř. float?
seznam_float = list(map(float, seznam_str))
#for i in range(0, pocet_radku):
#    cely_seznam[i] = float(cely_seznam[i])

mereni = seznam_float[13:]

# soucet a prumer mereni

delitel = pocet_radku-13
soucet = sum(mereni)
prumer=soucet/delitel
print("Součet všech měření je ", soucet)
print("Průměr měření je ", prumer)
# info mereni
datum = int(seznam_float[8])
print("Datum měření je ", datum, ", ve formátu ddmmr (den měsíc a rok)")
mojedata.close()

# ulozeni do souboru
novy_soubor = open("hodnoty z programu.txt", "w")
novy_soubor.write(str(prumer)+"\n")
novy_soubor.write(str(soucet)+"\n")
novy_soubor.write(str(datum))
novy_soubor.close()
# scipy optimize, co je optimalizace in general, github, konvoluce pochopit, pochopit rovnice, formatovani strings {}