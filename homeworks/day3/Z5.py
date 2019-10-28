year=int(input("Podaj rok: "))

if year % 400 == 0:
    print(f"Rok {year} jest przestępny")
elif year % 100 != 0 and year % 4 == 0:
    print(f"Rok {year} jest przestępny")
else:
    print(f"Rok {year} nie jest przestępny")