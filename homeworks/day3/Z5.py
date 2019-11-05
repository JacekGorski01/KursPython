def print_answer(x):
    if x == "tak":
        print(f"Rok {year} jest przestępny")
    elif x == "nie":
        print(f"Rok {year} nie jest przestępny")

year=int(input("Podaj rok: "))


if year % 400 == 0:
    print_answer("tak")
elif year % 100 != 0 and year % 4 == 0:
    print_answer("tak")
else:
    print_answer("nie")