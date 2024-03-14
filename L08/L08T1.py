import math
import random

def pintaAla():
    sade = int(input("Anna ympyrän säde kokonaislukuna: "))
    pa = math.pi * math.pow(sade,2)
    print("Säteellä {} ympyrän pinta-ala on {}.".format(sade, round(pa,2)))

def arvaaLuku():
    print("Arvaa ohjelman arpoma kokonaisluku.")
    random.seed(1)
    luku = random.randint(0,1000)
    arvaus = int(input("Anna kokonaisluku väliltä 0-1000: "))
    arvaustenMaara = 1

    while arvaus != luku:
        if arvaus > luku:
            print("Haettu luku on pienempi.")
        elif arvaus < luku:
            print("Haettu luku on suurempi.")
        arvaus = int(input("Anna kokonaisluku väliltä 0-1000: "))
        arvaustenMaara += 1
    
    print("Oikein! Käytit arvaamiseen {} kierrosta.".format(arvaustenMaara))


def main():
    print("Mitä haluat tehdä:")
    print("1) Laskea ympyrän pinta-alan")
    print("2) Arvata luvun")
    print("0) Lopeta")
    toiminto = int(input("Valintasi: "))

    while toiminto != 0:
        if toiminto == 1:
            pintaAla()
        elif toiminto == 2:
            arvaaLuku()
        toiminto = int(input("Valintasi: "))
    
    print("Kiitos ohjelman käytöstä.")

main()