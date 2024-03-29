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



def AnnaLuku(lista1: list):
    luku1 = 0
    luku2 = 0
    
    if len(lista1) == 0:
        print("Luvut loppuivat, lopeta ohjelma.")
        return luku1, luku2
    else:
        luku1 = lista1[0]
        lista1.pop(0)
        luku2 = lista1[0]
        lista1.pop(0)
        return luku1, luku2        
        
def Summa(luku1, luku2):
    summa = luku1 + luku2
    merkkijono = "Summa {} + {} = {}".format(luku1, luku2, summa)
    return merkkijono

def Osamaara(luku1, luku2):
    if luku2 == 0:
        merkkijono = "Nollalla ei voi jakaa."
    else:
        osamaara = round(luku1 / luku2, 2)
        merkkijono = "Osamäärä {} / {} = {}".format(luku1, luku2, osamaara)
    return merkkijono

def tallennaTulos(tiedosto, lista2):
    for rivi in lista2:
        tiedosto.write(rivi + "\n") 