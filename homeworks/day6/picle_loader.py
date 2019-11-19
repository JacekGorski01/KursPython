import pprint
import pickle
import random
from create_menu import menu_builder
from datetime import datetime

def search_book(string):
    '''Search substring in strings - values in dictionary and print them

        Parameters:
        string (str) - piece of string you want to find

        Return:
        None

'''
    for i,row in enumerate(entries):

        for key in row.keys():
            result = row[key].find(find_value)

            if result >= 0:
                print(row.items())
            else:
                pass


menu_builder(["menu"], 5)

with open('book.pkl', 'rb+') as book_file:
        entries = pickle.load(book_file)
        print(entries)


right_values = ["1", "2", "3", "4", "5", "Q", "R"]
choice = input('\nWybierz program (1-10,"R","Q"): ')
while choice not in right_values:
    print('Nieprawidłowy wybór, wpisz liczbę w przedziale 1-10, "R" lub "Q": ')
    choice = input("\nWybierz program (1-10): ")

print(f"Wybrałeś: {choice}")
if choice == "R":
        choice = random.choice(right_values[0:6]) #wykluczam by nie wylosowało się ponownie R
        print(f"Wylosowałęś opcję {choice}")
else:
    pass

if choice == "Q":
        print("Do zobaczenia!")
        exit(5)
elif choice == "1":
    ans = "T"

    while ans == "T":
        inserts_num = len(entries)
        print("Dodaj wpis!")
        title_content = input("Tytuł wpisu : ")
        body_content = input("Treść wpisu : ")
        author_content = input("Autor wpisu : ")
        date_content = str(datetime.now())

        entries.append({"title": title_content, "body": body_content, "author": author_content, "date": date_content})

        ans = input(f'Dziękujemy za dodanie {inserts_num} wpisu. Czy chcesz dodać kolejny (T)? ')

elif choice == "2":
    find_value = input("Wyszukaj: ")
    search_book(find_value)

elif choice == "3":
        entries.sort(key = lambda x:x['date'], reverse = True, )
        for i in entries:
            print(i)
elif choice == "4":
        entries.sort(key=lambda x: x['date'],)
        for i in entries:
            print(i)
elif choice == "5":
        show = 0
        print(entries[show])
        while show in range(0,len(entries)):
            if show == 0:
                prev_nest = input(f"To jest pierwszy wpis, pokazać następny (n)? :")
                if prev_nest == "n":
                    show =+ 1
                    print(entries[show])
                else:
                    print(f"Do zobaczenia!")
                    exit(5)

            elif show in range(1,len(entries)- 1):
                prev_nest = input(f"Pokazać następny (n) lub poprzedni (p)? : ")
                if prev_nest == "n":

                    show += 1
                    print(entries[show])
                elif prev_nest == "p":
                    show -= 1
                    print(entries[show])
                else:
                    print(f"Do zobaczenia!")
                    exit(5)

            elif show == (len(entries) -1):
                prev_nest = input(f"To ostatni wpis, pokazać poprzedni (p)? :")
                if prev_nest == "p":
                    show -= 1
                    print(entries[show])
                else:
                    print(f"Do zobaczenia!")
                    exit(5)


with open('book.pkl', 'wb+') as book_file:
    pickle.dump(entries, book_file)


