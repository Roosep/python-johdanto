sana = input("Anna pitkä sana: ")
print("Antamasi sanan viisi ensimmäistä kirjainta ovat {}".format(sana[:5]))
print("Viisi viimeistä kirjainta ovat {}".format(sana[-5:]))
print("Kirjaimet 2,3,4 ja 5 ovat {}".format(sana[1:5]))
print()

print("Sanan joka toinen kirjain alkaen toisesta kirjaimesta: {}".format(sana[1:len(sana):2]))
print()

print("Annoit sanan '{}', joka on takaperin {}".format(sana, sana[::-1]))
print()

aloitus = int(input("Anna aloituspaikka: "))
lopetus = int(input("Anna lopetuspaikka: "))
siirtyma = int(input("Anna siirtymä: "))
print("Antamillasi asetuksilla sana {} tulostuu näin: {}".format(sana, sana[aloitus:lopetus:siirtyma]))
print()

print("Sana oli {} merkkiä pitkä.".format(len(sana)))
print("Kiitos ohjelman käytöstä.")