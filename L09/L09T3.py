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
    
    return lista


def AnalysoiTiedot(lista: list):
    viimeMerkki = ""
    analysoidut = []

    for merkki in lista:
        if merkki != viimeMerkki:
            analysoidut.append(merkki)

    return analysoidut

def TallennaTiedot(lista: list, kirjoitettavaNimi):
    print("Tiedostossa oli {} eri merkkiä.".format(len(lista)))
    for merkki in lista:
        print(merkki)
    tiedosto = open(kirjoitettavaNimi, "w")
    for merkki in lista:
        tiedosto.write(merkki + "\n")
    tiedosto.close


def main():
    luettavaNimi = input("Anna luettavan tiedoston nimi: ")
    kirjoitettavaNimi = input("Anna kiejoitettavan tiedoston nimi: ")
    lista = []

    lista = LueTiedosto(lista, luettavaNimi)

    if len(lista) != 0:
        lista = AnalysoiTiedot(lista)
        TallennaTiedot(lista, kirjoitettavaNimi)
    
    print("Kiitos ohjelman käytöstä.")

main()