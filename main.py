
# nacteni dat
mojedata = open("data.txt", "r")
cely_seznam = mojedata.read().splitlines()
pocet_radku = len(cely_seznam)

# loop pro převedení str v seznamu na float, urcite jde i nějak lip
# funkce pro prevedeni dat ze souboru do seznamu rovnou v int, popř. float?
pokus = list(map(float, cely_seznam))
print(pokus)
for i in range(0, pocet_radku):
    cely_seznam[i] = float(cely_seznam[i])

mereni = cely_seznam[13:]
print(mereni)

# soucet a prumer mereni

delitel = pocet_radku-13
soucet = sum(mereni)
prumer=soucet/delitel
print("Součet všech měření je ", soucet)
print("Průměr měření je ", prumer)
# info mereni
datum = int(cely_seznam[8])
print("Datum měření je ", datum, ", ve formátu ddmmr (den měsíc a rok)")
mojedata.close()

# ulozeni do souboru
novy_soubor = open("hodnoty z programu.txt", "w")
novy_soubor.write(str(prumer)+"\n")
novy_soubor.write(str(soucet)+"\n")
novy_soubor.write(str(datum))
novy_soubor.close()
