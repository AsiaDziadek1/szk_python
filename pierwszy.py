# clean code
# PEP8 - ctr alt l - formatowanie kodu
print()  # wydrukuj/wypisz
print("Nazywam się Asia")  # w cudzysłowiu umieszczam tekst (str)
print("Nazywam się Asia")  # w cudzysłowiu umieszczam tekst (str)
print("Nazywam się Asia")  # w cudzysłowiu umieszczam tekst (str)
print("Nazywam się Asia")  # w cudzysłowiu umieszczam tekst (str)
print('Nazywam się Asia')  # w cudzysłowiu umieszczam tekst (str)
# ctr d - kopiowanie linii
print(type("Asia"))  # <class 'str'> tekst
# type() - zwraca typ jakiego rodzaju podaliśmy argument

print(39)
print(type(39))  # <class 'int'> liczby całkowite

print("39" + "15")  # łaczenie tekstów - konkatenacja
print(39 + 15)
print(5 * "4")

# zmienne - pudełko na dane
imie = "Asia"
print(type(imie))
print(imie)

imie = 47
print(type(imie))

wiek = 42
print(type(wiek))
print(wiek)
print(wiek + imie)

imie = "Asia"
# ctrl / - komentarz linii pod kursorem
# print(wiek + imie)  #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print((str(wiek) + imie)) # str() - zamiana - rzutowanie na str

print(int("34") + int("54"))  # int() - rzutowanie na int, zamiana na int


