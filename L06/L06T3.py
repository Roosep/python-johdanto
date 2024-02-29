def main():
    luettavaNimi = input("Anna luettavan tiedoston nimi: ")
    kirjoitettavaNimi = "L06T3T1.txt"

    luettavaTiedosto = open(luettavaNimi, "r", encoding="UTF-8")
    kirjoitettavaTiedosto = open(kirjoitettavaNimi, "w")

    while True:
        rivi = luettavaTiedosto.readline().rstrip()
        if len(rivi) == 0:
            break
        if rivi.isdigit():
            print("Rivi '{}' on numerorivi.".format(rivi))
        elif rivi == rivi[::-1]:
            print("Rivi '{}' on palindromi.".format(rivi))
            kirjoitettavaTiedosto.write(rivi + "\n")
        else:
            print("Rivi '{}' ei ole palindromi.".format(rivi))

    print("Kiitos ohjelman käytöstä.")


main()