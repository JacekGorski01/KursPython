num = input("Podaj liczbę: ")
num = int(num)
#podzielna przez 3, 5 i 3i5 nie jest


if num%3 == 0 & num%5 == 0:
    print("To liczba podzielna przez 3 i 5")

elif num%5 == 0:
    print("To liczba podzielna przez 5")

elif num%3 == 0:
    print("To liczba podzielna przez 3")

else:
    print("Nie jest podzielna")

