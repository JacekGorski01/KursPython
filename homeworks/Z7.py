quota=float(input("Podaj kwotę: "))

#sprawdzenie czy podana kwota nie zawiera groszówek - na mega okrętkę :).
x = (quota - int(quota))
print(x)
#pobieram długość całego "złośliwego" floata
length = len(str(x))

#żeby wskazać, że zaokrąglenie tyczy się zawsze 3 liczby po przecinku muszę wiedzieć ile mam odjąć od całkowitej liczby znaków, zeby było 3
pos = length - 3
print(pos)
#i tyleż odejmuję
y=round(x, length-pos)
y=y%0.1
print(y)
if quota < 0.1:
        print("Wpisz liczbę większą niż 10 gr.")
elif quota%0.1 != 0:
        print("Kwotę wydajemy z dokładnością do 10 gr.")
else:

    while quota % 5 >= 0.1:
            change=quota % 5
            fives=int(quota /5)
            quota = change
            print(f"Otrzymasz: {fives} monet pięciozłotowych.")
            pass
            change = quota % 2
            twos = int(quota / 2)
            quota = change
            print(f"Otrzymasz: {twos} monet dwuzłotowych.")
            pass
            change = quota % 1
            ones = int(quota / 1)
            quota = change
            print(f"Otrzymasz: {ones} monet jednozłotowych.")
            pass
            change = quota % 0.5
            grfifties = int(quota / 0.5)
            quota = change
            print(f"Otrzymasz: {grfifties} monet pięćdziesięciogroszowych.")
            pass
            change = quota % 0.2
            grtwenties = int(quota / 0.2)
            quota = change
            print(f"Otrzymasz: {grtwenties} monet dwudziestogroszowych.")
            pass
            change = quota % 0.1
            grtens = int(quota / 0.1)
            quota = change
            print(f"Otrzymasz: {grtens} monet dzieścięciogroszowych.")






#print(change)

#     rest = quota % 5
#     while
# x=1%2
# print(x)
# kwota % 5 = reszta
# 1. Kwota / 5 = ilość piątek
# bierzesz ile piatek i dalej
#
# reszta / 2 = ilosc dwójek
# reszta % 2 = reszta
# bierzesz ile dwojek i dalej
#
# reszta / 1 = ilośc zetów
# reszta % 1 = reszta
# biore ile zeta i dalej
#
# 0.5
# 0.2
# 0.1
