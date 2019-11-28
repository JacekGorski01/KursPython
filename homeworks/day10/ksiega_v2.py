import pickle
import random
from create_menu import menu_builder
from datetime import datetime


class Entry():

    def __init__(self):
        self.title = input('Tytuł: ')
        self.body = input('Treść: ')
        self.author = input('Autor: ')
        self.date = str(datetime.now())

    def create_entry(self):

        row = {"title": self.title, "body": self.body, "author": self.author, "date": self.date}
        return row

class Book():

    with open('book.pkl', 'rb+') as book_file:
        entries = pickle.load(book_file)

    def __init__(self, entries = entries):
        self.entries = entries
        self.entries_count = len(entries)

    def add_entry(self, row):

        self.entries.append(row)
        self.entries_count += 1
        with open('book.pkl', 'wb+') as book_file:
            pickle.dump(self.entries, book_file)

    def search_book(self, find_value):
        search_result = []
        for i, row in enumerate(self.entries):
            for key in row.keys():
                result = row[key].find(find_value)

                if result >= 0:
                    search_result.append(row.items()) #musze dodawać do zainicjowanej listy żeby karmić returna poza pętlą. inne sposoby?

        return search_result

    def sort_book(self, torf):
        sorted_list = self.entries.copy() #musze skopiować listę, żeby nie przekręcać instancji
        sorted_list.sort(key=lambda x: x['date'], reverse=torf)
        return sorted_list


book = Book()

choice = "X"
while choice != "Q":
    line = 4
    choice = menu_builder(["menu"], line) #napętlam do upadłego - czyli "Q"


    if choice == "1":
        ans = "T"

        while ans == "T":
            row = Entry()
            book.add_entry(row.create_entry())
            ans = input(f"Dziękuję za dodanie {book.entries_count} wpisu. Czy dodać kolejny wpis (T/N): ")
        choice = input('Jeśli chcesz zakończyć wybierz "Q", by kontynuować wybierz cokolwiek ')

    elif choice == "2":
        x = book.search_book(input(f'Wyszukaj: '))
        for i in x:
            print(i)
        choice = input('Jeśli chcesz zakończyć wybierz "Q" by kontynuować wybierz cokolwiek...')


    elif choice in ["3", "4"]:
        if choice == "3":
            tof = False
        elif choice == "4":
            tof = True

        x = book.sort_book(torf=tof) #true or false
        print(x)

        choice = input('Jeśli chcesz zakończyć wybierz "Q", by kontynuować wybierz cokolwiek...')



# wpis = Entry()
# entries = Book()
# x = entries.entries_count
# print(x)
# # #sort_result = Book.entries.sort(key=lambda x: x['date'], reverse=True)
# # #print(sort_result)
# # x = entries.sort_book(False)
# # #y = entries.SortInserts(True)
# # print(x)
# #
# y = entries.sort_book(True)
# print(y)
# # print(Book.entries)
# # #print(entries.entries)
# row = Entry.create_entry(wpis)
# entries.add_entry(row)
# # x = entries.search_book("asd")
# # print(x)
# print(entries.entries_count)