import pickle
import random
from create_menu import menu_builder
from datetime import datetime


#Zgrubnie, zabrakło czasu. Jakoś te wywołania obiektów działają.
#Czy jest jakiś zastanawiam się czy można w __init__ przyjąć zmienną od użytkowanika tak by to wszystko odbywało się
#w ramach klasy. Teraz słownik pobrany z pliku przekazuje z "zewnątrz" przy powołaniu instancji np "user_insert = Insert(entries = entries)"
#




class Insert():

    def __init__(self, entries):
        self.entries = entries

    def CreateInsert(self):
        print(f'Dodaj wpis!')
        title = input("Tytuł wpisu : ")
        body = input("Treść wpisu : ")
        author = input("Autor wpisu : ")
        date = str(datetime.now())
        row = {"title": title, "body": body, "author": author, "date": date}

        return row

    def AddInsert(self, row):
        self.entries.append(row)
        with open('book.pkl', 'wb+') as book_file:
            pickle.dump(self.entries, book_file)

        return self.entries


class Book(Insert):

    def __init__(self, entries):
        super().__init__(entries)

    def LoadEntries(self):
        with open('book.pkl', 'rb+') as book_file:
            entries = pickle.load(book_file)
        return entries

    def SearchBook(self):
        find_value = input("Wyszukaj: ")
        for i, row in enumerate(entries):
            for key in row.keys():
                result = row[key].find(find_value)
                found = 0

                if result >= 0:
                    found += 1
                    return row.items()

                else:
                    pass

                    if found == 0:
                        return f'Nie znaleziono szukanej frazy'




    def SortInserts(self):
        entries.sort(key=lambda x: x['date'], reverse=True)
        for i in entries:
            print(i)



with open('book.pkl', 'rb+') as book_file:
    entries = pickle.load(book_file)

user_insert = Insert(entries = entries)

current_book_state = user_insert.AddInsert(user_insert.CreateInsert())
print(current_book_state)

upload_book = Book(entries)
x = upload_book.LoadEntries()
print(x)

x = upload_book.SearchBook()
print(x)
print(upload_book.entries)









