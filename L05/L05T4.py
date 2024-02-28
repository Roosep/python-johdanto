def kysy():
    sana = input("Anna merkkijono, 5-15 merkkiä: ")
    return sana

def testaa(sana):
    pituus = 0

    for kirjain in sana:
        pituus += 1

    return pituus

def main():
    sana = kysy()
    pituus = testaa(sana)

    while pituus < 5 or pituus > 15:
        if pituus < 5:
            print("Liian lyhyt, {} merkkiä, anna uusi.".format(pituus))
        else:
            print("Liian pitkä, {} merkkiä, anna uusi.".format(pituus))

        sana = kysy()
        pituus = testaa(sana)

    print("Annoit sopivan merkkijonon, {} merkkiä.".format(pituus))
    print("Kiitos ohjelman käytöstä.")

main()