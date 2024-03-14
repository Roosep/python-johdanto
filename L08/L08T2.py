import L08T2Kirjasto as muunnin

def main():
    print("Käytetään lämpötilamuunnoskirjaston versiota {}".format(muunnin.versio))
    print("Minkä lämpötilamuunnoksen haluat tehdä?")
    print("1) Celsius->Fahrenheit")
    print("2) Celsius->Kelvin")
    print("3) Fahrenheit->Kelvin")
    print("4) Fahrenheit->Celsius")
    print("5) Kelvin->Celsius")
    print("6) Kelvin->Fahrenheit")
    print("0) Lopeta")
    toiminto = int(input("Valintasi: "))
    
    while toiminto != 0:
        lampotila = int(input("Anna lähtölämpötila: "))
        if toiminto == 1:
            muunnettu = muunnin.CelToFah(lampotila)
            print("Lämpötila Fahrenheit asteina: {}".format(round(muunnettu, 2)))
        elif toiminto == 2:
            muunnettu = muunnin.CelToKel(lampotila)
            print("Lämpötila Kelvin asteina: {}".format(round(muunnettu, 2)))
        elif toiminto == 3:
            muunnettu = muunnin.FahToKel(lampotila)
            print("Lämpötila Kelvin asteina: {}".format(round(muunnettu, 2)))
        elif toiminto == 4:
            muunnettu = muunnin.FahToCel(lampotila)
            print("Lämpötila Celsius asteina: {}".format(round(muunnettu, 2)))
        elif toiminto == 5:
            muunnettu = muunnin.KelToCel(lampotila)
            print("Lämpötila Celsius asteina: {}".format(round(muunnettu, 2)))
        elif toiminto == 6:
            muunnettu = muunnin.KelToFah(lampotila)
            print("Lämpötila Fahrenheit asteina: {}".format(round(muunnettu, 2)))
        
        print()
        print("Minkä lämpötilamuunnoksen haluat tehdä?")
        print("1) Celsius->Fahrenheit")
        print("2) Celsius->Kelvin")
        print("3) Fahrenheit->Kelvin")
        print("4) Fahrenheit->Celsius")
        print("5) Kelvin->Celsius")
        print("6) Kelvin->Fahrenheit")
        print("0) Lopeta")
        toiminto = int(input("Valintasi: "))
    
    print("Kiitos ohjelman käytöstä.")


main()