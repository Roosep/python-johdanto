def TiedostoLue(tiedostonimi):
    print("Tiedostoon '{}' on tallennettu seuraavat nimet: ".format(tiedostonimi))
    tiedosto = open(tiedostonimi, "r")
    while True:
        rivi = tiedosto.readline()
        if len(rivi) == 0:
            break
        print(rivi, end="")
    tiedosto.close()



def TiedostoKirjoita(tiedostonimi):
    tiedosto = open(tiedostonimi, "w").close()
    tiedosto = open(tiedostonimi, "w")
    nimi = input("Anna tiedostoon tallennettava nimi (0 lopettaa): ")
    while nimi != "0":
        tiedosto.write(nimi + "\n")
        nimi = input("Anna tiedostoon tallennettava nimi (0 lopettaa): ")
    tiedosto.close()

    
def main():
    tiedostonNimi = input("Anna tallennettavan tiedoston nimi: ")
    TiedostoKirjoita(tiedostonNimi)
    TiedostoLue(tiedostonNimi)

    print("Kiitos ohjelman käytöstä.")

main()