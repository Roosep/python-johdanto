alaraja = int(input("Anna alueen alaraja: "))
ylaraja = int(input("Anna alueen yläraja: "))

etsinta = False

for i in range(alaraja, ylaraja+1):
    if i % 5 == 0:
        if i % 7 == 0:
            etsinta = True
            break
        else:
            print("{} ei ole jaollinen seitsemällä, hylätään.".format(i))
    else:
        print("{} ei ole jaollinen viidellä, hylätään.".format(i))

if etsinta:
    print("Luku {} on jaollinen 5:llä ja 7:llä.".format(i))
    print("Lopetetaan etsintä.")
else:
    print("Alueelta ei löytynyt sopivaa arvoa.")

print("Kiitos ohjelman käytöstä.")