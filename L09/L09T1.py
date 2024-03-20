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

import sys

def LueTiedosto(lista: list, luettavaNimi: str):
    try:
        tiedosto = open(luettavaNimi, "r")

        while True:
            rivi = tiedosto.readline().rstrip()
            if len(rivi) == 0:
                break
            else:
                lista.append(rivi)
        tiedosto.close()
    except:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(luettavaNimi))
        sys.exit(0)
    else:
        print("Tiedoston '{}' lukeminen onnistui, {} riviä.".format(luettavaNimi, len(lista)))
        return lista

def KirjoitaTiedosto(lista: list, kirjoitettavaNimi: str):
    try:
        tiedosto = open(kirjoitettavaNimi, "w")

        for luku in lista:
            tiedosto.write(luku + "\n")
        
        tiedosto.close()
    except:
        print("Tiedosto '{}' käsittelyss' virhe, lopetetaan.".format(kirjoitettavaNimi))
        sys.exit(0)
    else:
        print("Tiedoston '{}' kirjoittaminen onnistui.".format(kirjoitettavaNimi))

def main():
    luettavaNimi = input("Anna luettavan tiedoston nimi: ")
    lista = []

    lista = LueTiedosto(lista, luettavaNimi)

    kirjoitettavaNimi = input("Anna kirjoitettavan tiedoston nimi: ")

    KirjoitaTiedosto(lista, kirjoitettavaNimi)

    print("Kiitos ohjelman käytöstä.")

main()