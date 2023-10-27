# wielodziedziczenie
# w pythonie mozna dziedziczyc po wielu klasach

class A:

    def method(self):
        print('Metoda z klasy A')

class B:

    def method(self):
        print('Metoda z klasy B')

class C(B, A):
    """
    Klasa C dziedziczy po klasie A i po klasie B
    """
    def method(self):
        print("Metoda z klasy C") # po nadpisaniu metod w klasie C mamy wynik Metoda z klasy C
        super().method() # po dodaniu metod w klasie C super().method() czyli wywołania metody z klasy wyższej mamy wynik Metoda z klasy B
        B.method(self) # możemy wskazać z której klasy ma byc uzyta method


obiekt1 = A()
obiekt2 = B()
obiekt1.method()
obiekt2.method()
obiekt3 = C()
obiekt3.method()  # Metoda z klasy B
print(C.__mro__)  #(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# kolejnośc w zapisie dziedziczenia ma znaczenie C(B,A)
# po nadpisaniu metod w klasie C mamy wynik Metoda z klasy C
# po dodaniu metod w klasie C super().method() czyli wywołania metody z klasy wyższej mamy wynik Metoda z klasy B
# możemy wskazać z której klasy ma byc uzyta method


