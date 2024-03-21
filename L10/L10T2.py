def main():
    luettavaNimi = input("Anna luettavan tiedoston nimi: ")
    tiedosto = open(luettavaNimi, "r", encoding= "UTF-8")

    sanakirja = {}

    tiedosto.readline()

    while True:
        rivi = tiedosto.readline().rstrip()
        if len(rivi) == 0:
            break
        else:
            osat = rivi.split(";")
            pvm = osat[1]
            vuosi = pvm[:3]

            if vuosi in sanakirja:
                sanakirja[vuosi] += 1
            else:
                sanakirja[vuosi] = 1
    
    summa = 0

    for vuosi in sanakirja:
        print("{}: {}".format(vuosi, sanakirja[vuosi]))

        summa += int(sanakirja[vuosi])

    print("Yhteensä {} autoa.")

    print("Kiitos ohjelman käytöstä.")


main()