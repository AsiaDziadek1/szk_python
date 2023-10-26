# klasa - szablon, który wyznacza jakie cechy, funcje powinien mieć dany obiekt
# klasa może określać pola i funkcje
# instancja klasy jest obiekt
# obiekt - element zbudowanych według wytycznych zawartych w klasie


class Human:
    """
    Klasa opisujaca człowieka w Pythonie
    """
    imie =""
    wiek = None
    plec ="k"

    def powitanie(self):
        print(f"Nazywam sie {self.imie}")

    def podaj_wiek(self):
        print(f"Wiek: {self.wiek}")

print(Human.__doc__)  # Klasa opisujaca człowieka w Pythonie
print(print.__doc__)

cz1 = Human()
print(cz1)  #<__main__.Human object at 0x000001EAAE184990>
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
cz1.imie = "Ania"
cz1.wiek = "45"
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)

cz2=Human()
cz2.imie = "Jacek"
cz2.wiek = "50"
cz2.plec = "m"
cz2.nazwisko='dr'
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
print(cz2.nazwisko)
cz2.powitanie()  #Nazywam sie Jacek
cz1.powitanie()  #Nazywam sie Ania
cz1.podaj_wiek() #Wiek: 45
cz2.podaj_wiek() #Wiek: 45








