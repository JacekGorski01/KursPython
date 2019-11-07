import random
from create_menu import menu_builder

menu_builder(["Z1.py", "Z2.py", "Z3.py", "Z4.py", "Z5.py"], 3)

choice = input("\nWybierz program (1-10) lub: ")

right_values = ["1", "2", "3", "4", "5", "R", "Q"]

while choice not in right_values:
    print('Nieprawidłowy wybór, wpisz liczbę w przedziale 1-10, "R" lub "Q": ')
    choice = input("\nWybierz program (1-10): ")

print(f"Wybrałeś: {choice}")
if choice == "R":
        choice = random.choice(right_values[0:6])
        print(f"Wylosowałęś opcję {choice}")
else:
    pass

if choice == "Q":
        print("Do zobaczenia!")
        exit(5)
elif choice == "1":
        import Z1.py
elif choice == "2":
        import Z2.py
elif choice == "3":
        import Z3.py
elif choice == "4":
        import Z4.py
elif choice == "5":
        import Z5.py