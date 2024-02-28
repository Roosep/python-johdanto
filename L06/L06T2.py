import math

def TiedostoLue(tiedostoNimi):
    tiedosto = open(tiedostoNimi, "r", encoding="UTF-8")
    rivit = []
    while True:
        rivi = tiedosto.readline()
        if len(rivi) == 0:
            break
        rivit.append(rivi)
    tiedosto.close()

    rivienMaara = len(rivit)
    merkkienMaara = 0
    for nimi in rivit:
        for kirjain in nimi:
            merkkienMaara += 1

    return rivienMaara, merkkienMaara


def main():
    tiedostoNimi = input("Anna luettavan tiedoston nimi: ")

    rivit, merkit = TiedostoLue(tiedostoNimi)

    print("Tiedostossa oli {} nimeä ja {} merkkiä.".format(rivit, merkit))

    print("Keskimääräinen nimen pituus oli {}".format(merkit/rivit))

main()