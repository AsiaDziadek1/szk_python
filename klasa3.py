class Car:
    """
    Klasa opisująca samochów
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        # pole prywatne __
        self.__predkosc=0  # wartość 0 zawsze przy tworzeniu obiektu


    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def licznik(self):
        print(f"Jedziesz z szybkością {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 25

    def __zmien_bieg(self):
        """
        metoda prywatna
        """
        print("Zmiana biegu")


ferrari = Car("Ferrari", 1960)
ferrari.gaz()
ferrari.gaz()
ferrari.gaz()
ferrari.gaz()
ferrari.gaz()
# print(ferrari.__predkosc) po nadaniu prędkosci pola prywatnego takie pole nie istnieje
ferrari.licznik()   #Jedziesz z szybkością 50 km/h
ferrari.__predkosc = 0  #ustawianie prędkości w sposób niekontrolowany przez klasę
ferrari.__predkosc = 100  #ustawianie prędkości w sposób niekontrolowany przez klasę
ferrari.licznik()
# print(ferrari.__predkosc) - nie uzywamy gdy pola mamy oznaczone jako prywatne
ferrari.hamuj()
ferrari.hamuj()
ferrari.licznik()  #enkapsulacja wystawia pole klasy - pole prędkosć
# print(ferrari.__predkosc)


