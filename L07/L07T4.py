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


class AUTO:
    merkki = ""
    hinta = 0

def Valikko():
    print("Käytettävissä olevat toiminnot:")
    print("1) Anna auton tiedot")
    print("2) Tulosta autojen tiedot")
    print("0) Lopeta")
    toiminta = int(input("Valintasi: "))

    return toiminta

def lisaaAuto(lista: list):
    autoMerkki = input("Anna auton merkki: ")
    autoHinta = int(input("Anna auton hinta: "))

    olio = "auto" + str(len(lista)+1)

    olio = AUTO()

    olio.merkki = autoMerkki
    olio.hinta = autoHinta

    lista.append(olio)

    return lista

def tulostaAutot(lista: list):
    print("Listalta löytyy seuraavat automerkit ja hinnat:")
    for i in range(len(lista)):
        print("{} {}".format(lista[i].merkki, lista[i].hinta))
    

def main():
    lista = []
    print("Tämä ohjelma lisää autojen tietoja listaan ja tulostaa ne.")

    toiminta = Valikko()

    while toiminta != 0:
        if toiminta == 1:
            lisaaAuto(lista)
        elif toiminta == 2:
            tulostaAutot(lista)
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        
        print()
        toiminta = Valikko()

    lista.clear()
    print("Kiitos ohjelman käytöstä.")

main()