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


def Valikko():
    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Testaa ValueError")
    print("2) Testaa IndexError")
    print("3) Testaa ZeroDivisionError")
    print("4) Testaa TypeError")
    print("0) Lopeta")

    try:
        toiminto = int(input("Valitse toiminto (0-3): "))
    except:
        print("Anna valinta kokonaislukuna.")
        return None
    else:
        return toiminto
    

def TestaaIndex():
    lista = [11, 22, 33, 44, 55]

    try:
        indeksi = int(input("Anna indeksi 0-4: "))    
        luku = lista[indeksi]
        return None
    except:
        print("Tuli IndexError, indeksi {}.".format(indeksi))
        return None


def TestaaNolla():
    try:
        luku = float(input("Anna jakaja: "))
        return None
    except:
        print("Tuli ZeroDivisionError, jakaja {}".format(luku))
        return None


def TestaaTyyppi():
    try:
        luku = int(input("Anna numero: "))
        return None
    except:
        print("Tuli TypeError, {}*{} merkkijonoilla ei onnistunut.".format(luku, luku))
        return None



def main():
    toiminto = Valikko()

    while toiminto != 0:
        if toiminto == 1:
            print("Valikko-ohjelma testaa ValueError'n.")
        elif toiminto == 2:
            TestaaIndex()
        elif toiminto == 3:
            TestaaNolla()
        elif toiminto == 4:
            TestaaTyyppi()

        toiminto = Valikko()

    print("Kiitos ohjelman käytöstä.")


main()