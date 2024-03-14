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

import L08T4Kirjasto as laskin


def Valikko():
    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut")
    print("2) Summa")
    print("3) Osamäärä")
    print("0) Lopeta")
    toiminto = int(input("Valitse toiminto (0-3): "))

    return toiminto    

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
            luku1, luku2 = laskin.AnnaLuku(lista1)
            if luku1 != 0:
                print("Luettiin luvut {} ja {}".format(luku1, luku2))
        elif toiminto == 2:
            merkkijono = laskin.Summa(luku1, luku2)
            lista2.append(merkkijono)
            print("Tulos lisätty listaan.")
        elif toiminto == 3:
            merkkijono = laskin.Osamaara(luku1, luku2)
            print("Tulos lisätty listaan.")
            lista2.append(merkkijono)
        toiminto = Valikko()

    laskin.tallennaTulos(kirjoitettavaTiedosto, lista2)
    

    print("Tallennettu tiedosto '{}'.".format(kirjoitettavaNimi))
    print("Kiitos ohjelman käytöstä.")


main()