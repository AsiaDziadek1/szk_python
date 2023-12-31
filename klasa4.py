class Dom:
    """
    Klasa opisujaca dom w Pythonie
    """

    def __init__(self, name, metraz, kolor, liczba_okien):  # inicjalizator konstruktor
        self.__name = name
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def podaj_name(self):
        print(f"Nazywam się {self.__kolor}")

    def podaj_kolor(self):
        print(f"Mam kolor {self.__kolor}")

    def podaj_metraz(self):
        print(f"Mam metraz {self.__repr__()}{self.__metraz}")

    def podaj_okna(self):
        print(f"Mam okien {self.__liczba_okien}")

    def zmien_metraz(self):
        wybor = int(input("Podaj metraz: "))
        self.__metraz = wybor
        self.podaj_metraz()

    def zmien_kolor(self):
        wybor = input("Podaj kolor: ")
        self.__kolor = wybor
        self.podaj_kolor()

    def __repr__(self):
        return f"Parametry: {self.__name} {self.__kolor} {self.__metraz} {self.__liczba_okien}"

    def zmien_liczba_okien(self):
        wybor = int(input("Podaj liczbę okien: "))
        self.__liczba_okien = wybor
        self.podaj_okna()


dom1 = Dom("moj", 200, "szary", 12)
dom1.podaj_name()
dom1.podaj_okna()
dom1.podaj_metraz()
dom1.podaj_kolor()
# Mam okien 12
# Mam metraz 200
# Mam kolor szary

dom1.zmien_kolor()
dom1.zmien_metraz()
dom1.zmien_liczba_okien()

dom2 = Dom(100, "biały", 5)
dom1.podaj_kolor()
dom2.podaj_kolor()

