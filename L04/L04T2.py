luvut = []
arvosana = int(input("Anna kurssiarvosana väliltä 1-5 (-1 lopettaa): "))
while arvosana != -1:
    if 1 <= arvosana <= 5:
        luvut.append(arvosana)
    else:
        print("Väärä syöte. Vain arvosanat 1-5 kelpaavat (-1 lopettaa).")
    arvosana = int(input("Anna kurssiarvosana väliltä 1-5 (-1 lopettaa): "))

summa = 0
for luku in luvut:
    summa += luku

keskiarvo = round(summa / len(luvut), 2)

print("Arvosanojen keskiarvo on {}.".format(keskiarvo))
print("Kiitos ohjelman käytöstä.")