pii = 3.14
luku = int(input("Anna positiivinen kokonaisluku: "))
print("Luku {} kerrottuna itsellään on {}".format(luku, luku*luku))
sade = int(input("Anna ympyrän säteen pituus kokonaislukuna: "))
print("Ympyran säde on {}, kehä on {} ja pinta-ala on {}.".format(sade, 2*pii*sade, pii*sade**2))
sivu1 = int(input("Anna suorakulmion yhden sivun pituus kokonaislukuna: "))
sivu2 = int(input("Anna suorakulmion toisen sivun pituus kokonaislukuna: "))
print("Suorakulmion sivut ovat {} ja {}; kehä on {}; ja pinta-ala on {}.".format(sivu1, sivu2, sivu1*2+sivu2*2, sivu1*sivu2))
print("Kiitos ohjelman käytöstä.")