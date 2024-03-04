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

def main():
    tiedostoNimi = input("Anna tiedoston nimi: ")

    tiedosto = open(tiedostoNimi, "r")

    tiedosto.readline()

    while True:
        rivi = tiedosto.readline().rstrip()
        if len(rivi) == 0:
            break

        osat = rivi.split(";")

        print("Kello oli {}, kun punnittiin marjoja {}.".format(osat[2], osat[0]))
    
    print("Kiitos ohjelman käytöstä.")

main()