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


def TeeValinta():
    print("Voit valita alla olevista toiminnoista:")
    print("1) Lisää")
    print("2) Poista")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))
    return valinta

def main():
    lista = []

    print(lista)
    valinta = TeeValinta()

    while valinta != 0:
        if valinta == 1:
            lisattavaTuote = input("Anna lisättävä tuote: ")
            lista.append(lisattavaTuote)
        elif valinta == 2:
            print("Ostoslistassasi on {} tuotetta.".format(len(lista)))
            poistettavaTuote = int(input("Anna poistettavan tuotteen järjestysnumero: "))
            lista.pop(poistettavaTuote)
        else:
            print("Tunnistamaton valita.")

        print()

        print("Ostoslistasi sisältää seuraavat tuotteet:")
        print(lista)
        valinta = TeeValinta()

    print("Sinulta jäi ostamatta seuraavat tuotteet:")
    print(lista)
    print("Kiitos ohjelman käytöstä.")

main()