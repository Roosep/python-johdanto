arvo1 = int(input("Anna a:n arvo: "))
arvo2 = int(input("Anna b:n arvo: "))

print("a: {} b: {}".format(arvo1, arvo2))
while arvo1 <= 10000 and arvo2 <= 10000:
    arvo1 = arvo1 * 2
    arvo2 += 100
    print("a: {} b: {}".format(arvo1, arvo2))
    if arvo1 > arvo2:
        break

print("Kiitos ohjelman käytöstä.")