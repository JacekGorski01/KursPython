class Krzeslo():
    def __init__(self, kolor_siedziska = "czerwony"):
        self.kolor_siedziska = kolor_siedziska
        self.ilosc_kol = 5
        self.wysokosc = '90cm'
        self.szerokosc = '90cm'
        self.szerokosc = '40cm'
        self.regulacja_wysokosci = True
        self.material = '100% cotton'

    def __str__(self):
        return f'Krzesło koloru {self.kolor_siedziska}'

obiekt = Krzeslo()
print(obiekt)
print(obiekt.kolor_siedziska)

obiekt = Krzeslo("niebieski")
print(obiekt)
print(obiekt.kolor_siedziska)