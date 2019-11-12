#Przeliczanie temperatur

from whatnext import start_other_module

print("\n*** To jest program do przeliczania temperatur st.\u2103 na st.\u2109 lub odwrotnie. ***\n")

print("Którą jednostkę temperatury chcesz skonwertować? \n 1. St. Celsjusza na Fahrenheita \n 2. St. Fahrenheit na Celsjusza.")
choose=int(input("Wybierz 1 lub 2: "))
list=[1,2]
while choose not in list:
    print("Nieprawidłowy wybór,  wpisz 1 lub 2")
    choose=int(input("Wpisz 1 lub 2: "))
else:
    print(f"Wybrałeś: {choose}")
    if choose == 1:
        c = int(input("Policzymy to wzorem:\nT(°F) = T(°C) × 9/5 + 32\n\Podaj liczbę stopni Celcjusza: "))
        f = c * 9/5 + 32
        print(f"\n{c} stopni \u2103 to {f} stopni \u2109")

    elif choose == 2:
        f = int(input("Policzymy to wzorem: \n T(°C) = (T(°F) - 32) / (9/5)\nPodaj liczbę stopni Fahrenheita: "))
        c = (f - 32) / (9/5)
        print(f"\n{f} stopni \u2109 to {c} stopni \u2103 ")

start_other_module("multitool")



