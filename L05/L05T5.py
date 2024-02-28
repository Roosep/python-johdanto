def Valikko():
    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut")
    print("2) Summa")
    print("3) Osamäärä")
    print("0) Lopeta")
    toiminto = int(input("Valitse toiminto (0-3): "))

    return toiminto

def AnnaLuku(ohje1, ohje2):
    luku1 = int(input(ohje1))
    luku2 = int(input(ohje2))

    return luku1, luku2

def Summa(luku1, luku2):
    summa = luku1 + luku2
    merkkijono = "Summa {} + {} = {}".format(luku1, luku2, summa)
    return merkkijono

def Osamaara(luku1, luku2):
    if luku2 == 0:
        merkkijono = "Nollalla ei voi jakaa."
    else:
        osamaara = round(luku1 / luku2, 2)
        merkkijono = "Osamäärä {} / {} = {}".format(luku1, luku2, osamaara)
    return merkkijono

def main():
    toiminto = Valikko()
    ohje1 = "Anna ensimmäinen luku: "
    ohje2 = "Anna toinen luku: "
    luku1 = 0
    luku2 = 0

    while toiminto != 0:
        if toiminto == 1:
            luku1, luku2 = AnnaLuku(ohje1, ohje2)
            print("Annoit luvut {} ja {}".format(luku1, luku2))
        elif toiminto == 2:
            print(Summa(luku1, luku2))
        elif toiminto == 3:
            print(Osamaara(luku1, luku2))
        toiminto = Valikko()

    print("Lopetetaan")
    print("Kiitos ohjelman käytöstä.")


main()