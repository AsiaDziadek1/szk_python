# klasa abstrakcyjna - klasa w której nie mozna stworzyć obiektów

from abc import ABC, abstractmethod
class Ptak(ABC):
    """
    klasa opisujaca ptaka w Pythonie
    """
    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością",self.szybkosc)

    @abstractmethod  # metoda staje się abstrakcyjna i nie mozna stworzyć klasy
    def wydaj_odglos(self):
        pass

class Kura(Ptak):

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)
    def latam(self):
        print("Tu", self.gatunek, "ja nie latam")

    def wydaj_odglos(self):
        print("Tu", self.gatunek, "wydaj odgłos ko ko ko")

class Orzel(Ptak):

    def wydaj_odglos(self):
        print("kiiiir ki-er")


# po dodaniu@abstractmethod klasa stała sie abstrakcyjn
# nie mozna stworzyć obiektu takiej klasy
# TypeError: Can't instantiate abstract class Ptak with abstract method wydaj_odglos

# orzel = Ptak("Orzel", 48)
# orzel.latam()
#
# kur = Ptak("kura",0)
# kur.latam()
kur2 = Kura("Kura")
kur2.latam()
kur2.wydaj_odglos()

or2 = Orzel("Orzeł", 48)
or2.latam()
or2.wydaj_odglos()






