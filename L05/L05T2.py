def vertailu(luku1, luku2):
    if luku1 > luku2:
        print("Testatuista luvuista {} on suurempi kuin {}".format(luku1, luku2))
        return luku1
    elif luku2 < luku1:
        print("Testatuista luvuista {} on suurempi kuin {}".format(luku2, luku1))
        return luku2
    else:
        print("Luvut ovat samansuuruiset.")
        return luku1

def main():
    luku1 = int(input("Anna ensimmäinen luku: "))
    luku2 = int(input("Anna toinen luku: "))

    tulos = vertailu(luku1, luku2)

    luku3 = int(input("Paljonko vähennetään suuremmasta luvusta: "))

    luku4 = tulos - luku3

    if tulos == luku1:
        vertailu(luku2, luku4)
    else:
        vertailu(luku1, luku4)

    
    print("Kiitos ohjelman käytöstä.")
    

main()