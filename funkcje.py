# funkcja - wydzielony fragment kodu który mozna wywoływać wielokrotnie

a = 6
b = 7


# deklarowanie funkcji

def dodaj():  # funkcja bezargumentowa, tylko zapamiętuje to miejsce jako miejsce umieszczenia funkcji
    print(a + b)  # wyświetli wynik działania


# parametr opcjonalny pozwala zasymulować przeciążenie funkcji liczba argumentów


def dodaj2(a, b):  # funkcja z argumentami a i b (obowiązkowymi)
    print(a + b)


def odejmij(a, b, c=0):
    # a i b obowiązkowe, c ma wartosc domyslną
    print(a - b - c)


# uruchomienie funkcji: nazwa i nawiasy ()
dodaj()  # 13
dodaj2(5, 6)  # 11
odejmij(9, 5)  # 4
odejmij(9, 5, 2)  # 2
odejmij(b=5, a=9)  # przekazanie parametrów po nazwie
odejmij(c=2, b=5, a=9)  # przekazanie parametrów po nazwie
print(dodaj())  # None
print(dodaj() + dodaj2(5, 6))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
