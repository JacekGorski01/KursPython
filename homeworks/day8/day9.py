class Krzeslo():
    def __init__(self, kolor_siedziska = "czerwony", cena = 100):
        self.kolor_siedziska = kolor_siedziska
        self.ilosc_kol = 5
        self.wysokosc = '90cm'
        self.szerokosc = '40cm'
        self.glebokosc = '40cm'
        self.regulacja_wyskosci = True
        self.regulacja_podlokietnikow = False
        self.material = '100% cotton'
        self.cena = cena
        self.vat = 23


    def __str__(self):
        return f'Krzesło koloru: {self.kolor_siedziska}'

    def __len__(self):
        return self.wysokosc * self.szerokosc * self.glebokosc

    def pobierz_cene_netto(self):



​obiekt = Krzeslo()
print(obiekt)
print(obiekt.kolor_siedziska)
​
obiekt = Krzeslo('niebieski')
print(obiekt)
print(obiekt.kolor_siedziska)
​
obiekt = Krzeslo()
print(obiekt)
print(obiekt.kolor_siedziska)



