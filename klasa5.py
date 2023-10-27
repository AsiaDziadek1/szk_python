# dziedziczenie
class Pojazd:
    """
    klasa opisujaca pojazd
    """
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")

class Samochod(Pojazd):
    """
    klasa opisujaca samochód
    """
    def __init__(self, kolor, marka):  #inicjalizator dla klasy marka
    # pass
        super().__init__(kolor)
        self.marka = marka

    def info(self):
        """
        metoda informujaca o cechach obiektu
        :return: None
        """
        # print(f"{self.marka}:{self.kolor}")
        super().info()  #mozna uzyć metody z klasy wyższej
        print(f"samochód: {self.marka}")

poj = Pojazd("zielony")
poj.info()

sam = Samochod("czerwony","Maserati")
sam.info()

print(sam.__doc__)  # wypisanie dokumentacji klasy
print(sam.info.__doc__)  #wypisanie dokumentacji metody w klasie