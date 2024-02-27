pituus = int(input("Anna pituus (cm): "))
paino = int(input("Anna paino (kg): "))

indeksi = round(paino / (pituus/100)**2, 1)

if indeksi <= 17:
    print("Painoindeksi on {} (Vaarallinen aliravitsemus)".format(indeksi))
elif 17 < indeksi < 18.5:
    print("Painoindeksi on {} (Liiallinen laihuus)".format(indeksi))
elif 18.5 <= indeksi < 25:
    print("Painoindeksi on {} (Normaali paino)".format(indeksi))
elif 25 <= indeksi < 30:
    print("Painoindeksi on {} (Ylipaino eli lievä lihavuus)".format(indeksi))
elif 30 <= indeksi < 35:
    print("Painoindeksi on {} (Merkittävä lihavuus)".format(indeksi))
elif 35 <= indeksi < 40:
    print("Painoindeksi on {} (Vaikea lihavuus)".format(indeksi))
else:
    print("Painoindeksi on {} (Sairaalloinen lihavuus)".format(indeksi))

tavoite = float(input("Anna tavoiteindeksi: "))

if tavoite < indeksi:
    ero = paino - round(tavoite * (pituus/100)**2, 1)
    print("Tavoiteindeksi vastaa {} kg alhaisempaa painoa.".format(ero))
else:
    ero = round(tavoite * (pituus/100)**2, 1) - paino
    print("Tavoiteindeksi vastaa {} kg suurempaa painoa.".format(ero))

print("Kiitos ohjelman käytöstä.")