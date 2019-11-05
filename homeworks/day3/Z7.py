quota = float(input("Podaj kwotę: ")) * 100
quota = round(int(quota))
moneta = [500, 200, 100, 50, 20, 10]


def polski_piekna_jezyk(ammount,e):
    if ammount == 1:
        word = "monetę"
    elif ammount in range(2,5):
        word = "monety"
    else:
        word = "monet"

    if e < 100:
        unit = "gr"
    else:
        e = int(e / 100)
        unit = "zł"

    print(f"{ammount} {word} {e} {unit}")


if quota < 0 or quota % 10 != 0:
    print("Podana kwota musi być większa od ZERA oraz NIE MOŻE skaładać się z reszty mniejszej niż 10 groszy")
else:
    print("Otrzymasz: ")
    for i, e in enumerate(moneta):
        ammount = int(quota / e)
        quota = quota % e
        if ammount == 0:
            pass
        else:
            polski_piekna_jezyk(ammount,e)






