######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Seppälä
# Opiskelijanumero: 002328748
# Päivämäärä: 13.3.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Tiettyjen metodien toimintoja on käyty hakemassa w3shcools sivuston materiaaleista
# Muuten kurssimateriaalin lisäksi on käytetty vain aikaisemmin oppimia asioita
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################


import datetime

def aikaOlio():
    teksti = input("Anna päivämäärä ja kello muodossa 'pp.kk.vvvv hh:mm': ")

    paivamaara = datetime.datetime.strptime(teksti, "%d.%m.%Y %H:%M")

    print("Annoit vuoden {}".format(paivamaara.year))
    print("Annoit kuukauden {}".format(paivamaara.month))
    print("Annoit päivän {}".format(paivamaara.day))
    print("Annoit tunnin {}".format(paivamaara.hour))
    print("Annoit minuutin {}".format(paivamaara.minute))
    
def ikaPaivina():
    teksti = input("Anna syntymäpäiväsi muodossa pp.kk.vvvv: ")
    paivamaara = datetime.datetime.strptime(teksti, "%d.%m.%Y")
    verrokkipvm = datetime.datetime(2000, 1, 1)

    tulos = verrokkipvm - paivamaara

    print("1.1.2000 sinä olit {} päivää vanha.".format(tulos.days))

def viikonpaivat():
    startDate = datetime.datetime(2024, 3, 4)


    for i in range(7):
        newDate = startDate + datetime.timedelta(days=i)
        print("{}".format(newDate.strftime("%A")))

def kuukaudet():
    for i in range(1, 13):
        month =  datetime.datetime(2024, 1*i, 1)
        print("{}".format(month.strftime("%b")))


def main():
    print("Tämä ohjelma käyttää datetime-kirjastoa tehtävien ratkaisemiseen.")
    print("Mitä haluat tehdä:")
    print("1) Tunnistaa aika-olion komponentit")
    print("2) Laskea iän päivinä")
    print("3) Tulostaa viikonpäivät")
    print("4) Tulostaa kuukaudet")
    print("0) Lopeta")
    toiminto = int(input("Valintasi: "))

    while toiminto != 0:
        if toiminto == 1:
            aikaOlio()
        elif toiminto == 2:
            ikaPaivina()
        elif toiminto == 3:
            viikonpaivat()
        elif toiminto == 4:
            kuukaudet()

        print()
        print("Mitä haluat tehdä:")
        print("1) Tunnistaa aika-olion komponentit")
        print("2) Laskea iän päivinä")
        print("3) Tulostaa viikonpäivät")
        print("4) Tulostaa kuukaudet")
        print("0) Lopeta")
        toiminto = int(input("Valintasi: "))

    print("Kiitos ohjelman käytöstä.")


main()