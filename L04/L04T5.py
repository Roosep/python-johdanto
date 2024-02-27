print("Tämä laskin osaa seuraavat toiminnot:")
print("1) Anna luvut")
print("2) Summa")
print("3) Erotus")
print("4) Tulo")
print("5) Osamäärä")
print("6) Potenssi")
print("0) Lopeta")
toiminto = int(input("Valitse toiminto (0-6): "))
luku1 = 0
luku2 = 0
while toiminto != 0:
    if toiminto == 1:
        luku1 = int(input("Anna ensimmäinen luku: "))
        luku2 = int(input("Anna toinen luku: "))
        print("Annoit luvut {} ja {}".format(luku1,luku2))
    elif toiminto == 2:
        print("Summa {} + {} = {}".format(luku1, luku2, luku1+luku2))
    elif toiminto == 3:
        print("Erotus {} - {} = {}".format(luku1, luku2, luku1-luku2))
    elif toiminto == 4:
        print("Tulo {} * {} = {}".format(luku1, luku2, luku1*luku2))
    elif toiminto == 5:
        if luku2 == 0:
            print("Nollalla ei voi jakaa.")
        else:
            print("Osamäärä {} / {} = {}".format(luku1, luku2, round(luku1/luku2, 2)))
    elif toiminto == 6:
        print("Potenssi {} ** {} = {}".format(luku1, luku2, luku1**luku2))
    else:
        print("Tuntematon valinta, yritä uudestaan.")
    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut")
    print("2) Summa")
    print("3) Erotus")
    print("4) Tulo")
    print("5) Osamäärä")
    print("6) Potenssi")
    print("0) Lopeta")
    toiminto = int(input("Valitse toiminto (0-6): "))

print("Lopetetaan")
print("Kiitos ohjelman käytöstä.")