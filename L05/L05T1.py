def ensimmainen():
    print("Nyt olemme tulosta-aliohjelmassa")
    print("Tämä aliohjelma tulostaa vain tekstiä.")
    print("Tämä sopii hyvin valikon tulostamiseen.")

def toinen(luku):
    print("Aliohjelmassa parametrin arvo on {}".format(luku))
    nelio = luku * luku
    print("Aliohjelmassa parametrin arvo on neliöön korottamisen jälkeen {}".format(nelio))

def kolmas(etunimi, sukunimi):
    return etunimi + " " + sukunimi

def main():
    print("Ensimmäinen vaihe:")
    ensimmainen()
    print()

    print("Toinen vaihe:")
    luku = int(input("Anna luku: "))
    print("Päätasolla ennen aliohjelmaa luku on {}".format(luku))
    toinen(luku)
    print("Päätasolla aliohjelman jälkeen luku on {}".format(luku))
    print()

    print("Kolmas vaihe:")
    etunimi = input("Anna etunimi: ")
    sukunimi = input("Anna sukunimi: ")
    yhdistetty = kolmas(etunimi, sukunimi)
    print("Etunimi '{}' ja sukunimi '{}' muodostavat nimen '{}'.".format(etunimi, sukunimi, yhdistetty))

    print("Kiitos ohjelman käytöstä.")

main()