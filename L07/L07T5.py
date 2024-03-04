######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Seppälä
# Opiskelijanumero: 002328748
# Päivämäärä: 4.3.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Tiettyjen metodien toimintoja on käyty hakemassa w3shcools sivuston materiaaleista
# Muuten kurssimateriaalin lisäksi on käytetty vain aikaisemmin oppimia asioita
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################


def Valikko():
    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut")
    print("2) Summa")
    print("3) Osamäärä")
    print("0) Lopeta")
    toiminto = int(input("Valitse toiminto (0-3): "))

    return toiminto

def AnnaLuku(lista1: list):
    luku1 = 0
    luku2 = 0
    
    if len(lista1) == 0:
        print("Luvut loppuivat, lopeta ohjelma.")
        return luku1, luku2
    else:
        luku1 = lista1[0]
        lista1.pop(0)
        luku2 = lista1[0]
        lista1.pop(0)
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

def tallennaTulos(tiedosto, lista2):
    for rivi in lista2:
        tiedosto.write(rivi + "\n") 
    

def main():
    luettavaNimi = input("Anna luettavan tiedoston nimi: ")
    kirjoitettavaNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    kirjoitettavaTiedosto = open(kirjoitettavaNimi, "w")
    luettavaTiedosto = open(luettavaNimi, "r")
    toiminto = Valikko()
    luku1 = 0
    luku2 = 0
    lista1 = []
    lista2 = []

    while True:
        rivi = luettavaTiedosto.readline().rstrip()
        if len(rivi) == 0:
            break
        else:
            lista1.append(int(rivi))
    
    print("Luettu tiedosto '{}'.".format(luettavaNimi))
    luettavaTiedosto.close()

    while toiminto != 0:
        if toiminto == 1:
            luku1, luku2 = AnnaLuku(lista1)
            if luku1 != 0:
                print("Luettiin luvut {} ja {}".format(luku1, luku2))
        elif toiminto == 2:
            merkkijono = Summa(luku1, luku2)
            lista2.append(merkkijono)
            print("Tulos lisätty listaan.")
        elif toiminto == 3:
            merkkijono = Osamaara(luku1, luku2)
            print("Tulos lisätty listaan.")
            lista2.append(merkkijono)
        toiminto = Valikko()

    tallennaTulos(kirjoitettavaTiedosto, lista2)
    

    print("Lopetetaan")
    print("Kiitos ohjelman käytöstä.")


main()