komento = input("Haluatko lopettaa ohjelman suorittamisen (k/K): ")
if komento not in ["k", "K"]:
    nimi = input("Anna nimi: ")
    salasana = input("Anna salasana: ")

    if nimi == "Matti" and salasana == "salasana":
        print("Käyttäjä tunnistettu.")
    else:
        print("Antamasi nimi oli {} merkkiä pitkä, mutta se tai salasana ei ollut oikein.".format(len(nimi)))
else:
    print("Kiitos ohjelman käytöstä.")