class Human:
    """
    Klasa człowieka w Pythonie
    """

    def __init__:(self, imie, wiek, plec="k"):  # inicjator, konstruktor
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def powitanie(self):
        print(f"Mam na imie {self.imie}")

    def podaj_wiek(self):
        print(f"Wiek {self.wiek}")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w droge")
        else:
            print("Ruszyłem w drogę")


cz1 = Human("Ania", "39")
print(cz1.wiek)
print(cz1.plec)
print(cz1.imie)
