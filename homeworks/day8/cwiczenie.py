class Zwierze():
    def __init__(self):
        self.oczy = 2
        self.wlosy = True

    def __str__(self):
        return f'Oczy: {self.oczy}, włosy: {self.wlosy}'


class Czlowiek(Zwierze):
    def dajglos(self):
        print('Hęęę')

class Student(Czlowiek):
    def dajglos(self):
        print('Siema jestem student')

class Kot(Zwierze):
    def dajglos(self):
        print('Miauu')

class Pies(Zwierze):
    def dajglos(self):
        print('Hauuu')

class Bokser(Pies):
    pass

class Jamnik(Pies):
    pass

class Dresiarz(Czlowiek):
    def __init__(self):
        self.wlosy = False

    def dajglos(self):
        print('Masz jakiś problem')

zwierze = Zwierze()
czlowiek = Czlowiek()
czlowiek.dajglos()
print(czlowiek.oczy)
pies = Pies()
pies.dajglos()
print(pies.oczy)
kot = Kot()
kot.dajglos()
print(kot.oczy)
jamnik = Jamnik()
jamnik.dajglos()
print(jamnik.oczy)

dresiarz = Dresiarz()
print(dresiarz)