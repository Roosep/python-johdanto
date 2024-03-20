######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Seppälä
# Opiskelijanumero: 002328748
# Päivämäärä: 17.3.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Tiettyjen metodien toimintoja on käyty hakemassa w3shcools sivuston materiaaleista
# Muuten kurssimateriaalin lisäksi on käytetty vain aikaisemmin oppimia asioita
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################


import L09T4Kirjasto as laskin
import sys


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
    toiminto = Valikko()
    luku1 = 0
    luku2 = 0
    lista1 = []
    lista2 = []

    try:
        luettavaTiedosto = open(luettavaNimi, "r")
        while True:
            rivi = luettavaTiedosto.readline().rstrip()
            if len(rivi) == 0:
                break
            else:
                lista1.append(int(rivi))
    except:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(luettavaNimi))
        sys.exit(0)

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

    if len(lista2) > 0:
        laskin.tallennaTulos(kirjoitettavaTiedosto, lista2)
        print("Tallennettu tiedosto '{}'.".format(kirjoitettavaNimi))
    else:
        print("Ei tallenettavia tietoja, tiedostoa ei tallennettu.")
    

    print("Kiitos ohjelman käytöstä.")


main()