def tulostus(teksti):
    print(teksti)

def main():
    teksti = input("Anna teksti: ")
    
    while teksti != "lopeta":
        maara = int(input("Anna luku: "))
        for i in range(maara):
            tulostus(teksti)
        print("")
        teksti = input("Anna teksti: ")
    
    print("Lopetetaan.")
    print("Kiitos ohjelman käytöstä.")


main()