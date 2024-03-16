######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Seppälä
# Opiskelijanumero: 002328748
# Päivämäärä: 13.3.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Tiettyjen metodien toimintoja on käyty hakemassa w3shcools sivuston materiaaleista
# Muuten kurssimateriaalin lisäksi on käytetty vain aikaisemmin oppimia asioita
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################



class TUOTE:
    tunniste = ""
    maara = 0
    hinta = 0.00

def LueTiedosto(lista: list, luettavaNimi: str):
    tiedosto = open(luettavaNimi, "r")

    while True:
        rivi = tiedosto.readline().rstrip()
        if len(rivi) == 0:
            break
        else:
            tuote = TUOTE()
            riviOsissa = rivi.split(";")
            tuote.tunniste = riviOsissa[0]
            tuote.maara = riviOsissa[1]
            tuote.hinta = riviOsissa[2]
            lista.append(tuote)

    print("Tiedosto '{}' luettu, {} riviä.".format(luettavaNimi, len(lista)))

    tiedosto.close()

    return lista

def AnalysoiTiedosto(luetut: list, analysoidut: list):
    summa = 0.0
    for tuote in luetut:
        yhteisHinta = round(int(tuote.maara) * float(tuote.hinta), 2)
        analysoidut.append("{:.2f}".format(yhteisHinta))
        summa += yhteisHinta
    
    print("Tiedot analysoitu, varaston arvo on {} EUR.".format(round(summa, 2)))

    return analysoidut

def TallennaTulokset(kirjoitettavaNimi: str, analysoidyt: list):
    tiedosto = open(kirjoitettavaNimi, "w")

    for tuote in analysoidyt:
        tiedosto.write(str(tuote) + "\n")
    
    tiedosto.close()

    print("Tulokset tallennettu tiedostoon '{}'.".format(kirjoitettavaNimi))



def main():
    luettavaNimi = input("Anna luettavan tiedoston nimi: ")
    kirjoitettavaNimi = input("Anna kirjoitettavan tiedoston nimi: ")

    luetut = []
    analysoidut = []

    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi tiedot")
    print("3) Tallenna Tulokset")
    print("0) Lopeta")
    
    toiminto = int(input("Valintasi: "))

    while toiminto != 0:
        if toiminto == 1:
            luetut = LueTiedosto(luetut, luettavaNimi)
        elif toiminto == 2:
            analysoidut = AnalysoiTiedosto(luetut, analysoidut)
        elif toiminto == 3:
            TallennaTulokset(kirjoitettavaNimi, analysoidut)
        
        print()
        
        print("Mitä haluat tehdä:")
        print("1) Lue tiedosto")
        print("2) Analysoi tiedosto")
        print("3) Tallenna Tulokset")
        print("0) Lopeta")
        
        toiminto = int(input("Valintasi: "))
    
    print("Kiitos ohjelman käytöstä.")

main()