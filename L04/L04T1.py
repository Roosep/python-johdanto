aloitus = int(input("Anna aloitusarvo: "))
lopetus = int(input("Anna lopetusarvo: "))

print("Toteutus for-lauseella:")
for luku in range(aloitus, lopetus+1):
    print(luku, end=" ")

print("")
print("")
print("Toteutus while-lauseella:")
luku = aloitus
while luku <= lopetus:
    print(luku, end=" ")
    luku += 1

print()
print()
print("Kiitos ohjelman käytöstä.")