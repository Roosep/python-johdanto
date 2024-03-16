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



def CelToFah(lampotila):
    fah = lampotila * 1,8 + 32
    return fah

def CelToKel(lampotila):
    kel = lampotila + 273,15
    return kel

def KelToFah(lampotila):
    fah = lampotila * 1,8 - 459,67
    return fah

def KelToCel(lampotila):
    cel = lampotila - 273,15
    return cel

def FahToKel(lampotila):
    kel = (lampotila + 459,67) / 1,8 
    return kel

def FahToCel(lampotila):
    cel = (lampotila - 32) / 1,8
    return cel

versio = 1.0