print("*** To jest program do liczenia zawartości skarbonki. ***")
print(f"Powiedz ile masz jakich monet")

suma = []
moneta = [5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

def print_ilosc(moneta):
    x = int(input(f"Podaj ilość {moneta} zł: "))
    quota = x * moneta * 100
    suma.append(quota)

for i, e in enumerate(moneta):
    print_ilosc(e)

fin_sum = sum(suma) / 100
print(f"W twojej skarbonce jest: {fin_sum} pln")


