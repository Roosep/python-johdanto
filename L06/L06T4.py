def pieninmaara(luettavaNimi, kirjoitettavaNimi):
    luettavaTiedosto = open(luettavaNimi, "r")
    kirjoitettavaTiedosto = open(kirjoitettavaNimi, "w", encoding="UTF-8")

    pienin = 0

    while True:
        rivi = luettavaTiedosto.readline().rstrip()
        if len(rivi) == 0:
            break
        if int(rivi) < pienin or pienin == 0:
            pienin = int(rivi)

    kirjoitettavaTiedosto.write("Pienin askelmäärä oli {} askelta.\n".format(pienin))

    print("Pienin askelmäärä oli {} askelta.".format(pienin))

def suurinmaara(luettavaNimi, kirjoitettavaNimi):
    luettavaTiedosto = open(luettavaNimi, "r")
    kirjoitettavaTiedosto = open(kirjoitettavaNimi, "a", encoding="UTF-8")

    suurin = 0

    while True:
        rivi = luettavaTiedosto.readline().rstrip()
        if len(rivi) == 0:
            break
        if int(rivi) > suurin:
            suurin = int(rivi)

    kirjoitettavaTiedosto.write("Suurin askelmäärä oli {} askelta.\n".format(suurin))

    print("Suurin askelmäärä oli {} askelta.".format(suurin))



def yhteismaara(luettavaNimi, kirjoitettavaNimi):
    luettavaTiedosto = open(luettavaNimi, "r")
    kirjoitettavaTiedosto = open(kirjoitettavaNimi, "a", encoding="UTF-8")

    summa = 0

    while True:
        rivi = luettavaTiedosto.readline().rstrip()
        if len(rivi) == 0:
            break
        summa += int(rivi)

    kirjoitettavaTiedosto.write("Yhteensä askelia oli {} askelta.\n".format(summa))

    print("Yhteensä askelia oli {} askelta.".format(summa))


def main():
    luettavaNimi = input("Anna tiedot sisältävän tiedoston nimi: ")
    kirjoitettavaNimi = input("Anna tallennettavan tiedoston nimi: ")

    pieninmaara(luettavaNimi, kirjoitettavaNimi)
    suurinmaara(luettavaNimi, kirjoitettavaNimi)
    yhteismaara(luettavaNimi, kirjoitettavaNimi)

    print("Kiitos ohjelman käytöstä.")

main()