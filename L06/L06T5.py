def Valikko():
    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut")
    print("2) Summa")
    print("3) Osamäärä")
    print("0) Lopeta")
    toiminto = int(input("Valitse toiminto (0-3): "))

    return toiminto

def AnnaLuku(tiedosto):
    luku1 = 0
    luku2 = 0
    
    rivi = tiedosto.readline().rstrip()
    if len(rivi) == 0:
        print("Luvut loppuivat, lopeta ohjelma.")
        luku1 = 0
    else:
        luku1 = int(rivi)
    
    rivi = tiedosto.readline().rstrip()
    if len(rivi) == 0:
        print("Luvut loppuivat, lopeta ohjelma.")
        luku2 = 0
    else:
        luku2 = int(rivi)
        
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
    tiedostoNimi = input("Anna luettavan tiedoston nimi: ")
    kirjoitettavaTiedosto = open("L06T5T1.txt", "w")
    tiedosto = open(tiedostoNimi, "r")
    toiminto = Valikko()
    luku1 = 0
    luku2 = 0

    while toiminto != 0:
        if toiminto == 1:
            luku1, luku2 = AnnaLuku(tiedosto)
            print("Luettiin luvut {} ja {}".format(luku1, luku2))
        elif toiminto == 2:
            merkkijono = Summa(luku1, luku2)
            print("Tulos tallennettu tiedostoon.")
            kirjoitettavaTiedosto.write(merkkijono + "\n")
        elif toiminto == 3:
            merkkijono = Osamaara(luku1, luku2)
            print("Tulos tallennettu tiedostoon.")
            kirjoitettavaTiedosto.write(merkkijono + "\n")
        toiminto = Valikko()

    print("Lopetetaan")
    print("Kiitos ohjelman käytöstä.")


main()