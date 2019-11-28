import datetime

class Student():

    def __init__(self):
        self.imie = None
        self.nazwisko = None
        self.data_dodania = None
        self.data_usuniecia = None
        self.skasowany = False

    @property
    def imie(self):
        return self.__imie.capitalize()

    @imie.setter
    def imie(self, wartosc):
        self.__imie = wartosc

    @imie.deleter
    def imie(self):
        self.skasowany = True
        self.data_dodania = self.pobierz_date()

    @staticmethod
    def pobierz_date():
        return datetime.datetime.now().strftime('Y%-%m-%d')

student = Student()
student.imie = 'łukasz'
student.nazwisko = 'falkowicz'
student.data_dodania = datetime.datetime.now().strftime('Y%-%m-%d')

print(student.imie)