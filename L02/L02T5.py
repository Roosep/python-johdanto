import math
print("Tämä ohjelma laskee antamiesi 3 luvun keskiarvon.")
luku1 = int(input("Anna luku 0 ja 10 väliltä: "))
luku2 = int(input("Anna toinen luku 0 ja 10 väliltä: "))
luku3 = int(input("Anna kolmas luku 0 ja 10 väliltä: "))
print()
keskiarvo = (luku1+luku2+luku3)/3
print("Antamiesi lukujen summa on {}.".format(luku1+luku2+luku3))
print("Antamiesi lukujen keskiarvo on {}.".format(keskiarvo))
print("Keskiarvo on kokonaislukuna {}.".format(math.floor(keskiarvo)))
print("Keskiarvo pyöristettynä 3 desimaalin tarkkuuteen on {}.".format(round(keskiarvo, 3)))
print("Kiitos ohjelman käytöstä.")
