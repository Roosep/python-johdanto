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

class VARASTO:
    merkki = ""
    maara = 0

def Tiedot(auto):
    autoMerkki = input("Anna automerkki: ")
    autojenMaara = int(input("Anna automerkin lukumäärä varastossa: "))

    auto.merkki = autoMerkki
    auto.maara = autojenMaara

    return auto

def Tulostus(auto):
    print("Varastossa on nyt {}-merkkisiä autoja {} kpl.".format(auto.merkki, auto.maara))

def main():
    auto = VARASTO()

    Tiedot(auto)

    Tulostus(auto)

    print("Kiitos ohjelman käytöstä.")

main()