sana1 = input("Anna sana 1: ")
sana2 = input("Anna sana 2: ")

if sana1 == sana2:
    print("Sanat ovat samoja.")
elif sana1 < sana2:
    print("'{}' on aakkosissa aiemmin kuin '{}'.".format(sana1, sana2))
else:
    print("'{}' on aakkosissa aiemmin kuin '{}'.".format(sana2, sana1))

if "z" in sana1 or "z" in sana2:
    if "z" in sana1:
        print("Kirjain 'z' löytyy sanasta 1.")
    if "z" in sana2:
        print("Kirjain 'z' löytyy sanasta 2.")
else:
    print("Kummastakaan sanasta ei löytynyt kirjainta 'z'.")

sana3 = input("Anna testattava sana: ")
if sana3 == sana3[::-1]:
    print("Antamasi sana '{}' on palindromi.".format(sana3))
else:
    print("Antamasi sana ei ole palindromi.")
    print("Se on väärinpäin '{}' ja oikein päin '{}'.".format(sana3[::-1], sana3))

print("Kiitos ohjelman käytöstä.")

