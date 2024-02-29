def TiedostoLue(tiedostoNimi):
    tiedosto = open(tiedostoNimi, "r", encoding="UTF-8")
    rivit = []
    rivitClean = []
    while True:
        rivi = tiedosto.readline()
        riviClean = rivi.rstrip()
        if len(rivi) == 0:
            break
        rivit.append(rivi)
        rivitClean.append(riviClean)
    tiedosto.close()

    rivienMaara = len(rivit)
    merkkienMaara = 0
    kirjaimet = 0
    for nimi in rivit:
        for kirjain in nimi:
            merkkienMaara += 1

    for nimi in rivitClean:
        for kirjain in nimi:
            kirjaimet += 1

    return rivienMaara, merkkienMaara, kirjaimet


def main():
    tiedostoNimi = input("Anna luettavan tiedoston nimi: ")

    rivit, merkit, kirjaimet = TiedostoLue(tiedostoNimi)

    print("Tiedostossa oli {} nimeä ja {} merkkiä.".format(rivit, merkit))

    print("Keskimääräinen nimen pituus oli {} merkkiä.".format(round(kirjaimet/rivit)))

    print("Kiitos ohjelman käytöstä.")


main()