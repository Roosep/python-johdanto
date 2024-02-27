luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
print("Laskin osaa seuraavat toiminnot:")
print("1) Summa")
print("2) Erotus")
print("3) Tulo")
print("4) Osamäärä")
print("5) Potenssi")
print("Antamasi luvut ovat {} ja {}".format(luku1, luku2))
komento = int(input("Valitse toiminto (1-5): "))
if komento == 1:
    print("Summa {} + {} = {}".format(luku1, luku2, luku1+luku2))
elif komento == 2:
    print("Erotus {} - {} = {}".format(luku1, luku2, luku1-luku2))
elif komento == 3:
    print("Tulo {} * {} = {}".format(luku1, luku2, luku1*luku2))
elif komento == 4:
    if luku2 == 0:
        print("Nollalla ei voi jakaa.")
    else:
        print("Osamäärä {} / {} = {}".format(luku1, luku2, luku1/luku2))
elif komento == 5:
    print("Potenssi {} ** {} = {}".format(luku1, luku2, luku1**luku2))
else:
    print("Toimintoa ei tunnistettu.")
print("Kiitos ohjelman käytöstä.")