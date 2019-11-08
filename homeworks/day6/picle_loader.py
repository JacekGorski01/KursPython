import pickle
from datetime import datetime

with open('book.pkl', 'rb+') as book_file:
        entries = pickle.load(book_file)
        print(entries)


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



datatata = str(datetime.now())
ans = "T"

while ans == "T":
    inserts_num = len(entries)
    print("Dodaj wpis!")
    title_content = input("Tytuł wpisu : ")
    body_content = input("Treść wpisu : ")
    author_content = input("Autor wpisu : ")
    date_content = str(datatata)

    entries.append({"title": title_content, "body": body_content, "author": author_content, "date": date_content})

    ans = input(f'Dziękujemy za dodanie {inserts_num} wpisu. Czy chcesz dodać kolejny (T)? ')


with open('book.pkl', 'wb+') as book_file:
    pickle.dump(entries, book_file)

show_inserts = input('Wpisy zostały zapisane, chcesz zobaczyć wszystkie wpisy (T) lub wyszukać konkretny (S)?  ' )
if show_inserts == "T":
    for i in entries:
            print(i)
elif show_inserts == "S":
    find_value = input("Wyszukaj: ")
    search_book(find_value)

else:
    print("Do zobaczenia!")



