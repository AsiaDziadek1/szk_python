# napisać program kalkulator z wykorzystaniem petli while True
# menue z dostepnymi działaniami
# pobrac od uzytkownika liczby do obliczeń
# wyswielić wynik obliczenia

while True:
    print("""
    1.dodawanie
    2.odejmowanie
    3.mnożenie
    4.dzielenie
    5.koniec
    """)
    odp = input("Podaj opcje z menu")
    if odp >= '5':
        break
    a = float(input("Podaj liczbe1"))
    b = float(input("Podaj liczbe2"))
    if odp == '1':
        print(a + b)
    elif odp == '2':
        print(a - b)
    elif odp == '3':
        print(a * b)
    elif odp == '4':
        if b != 0:
            print(a / b)
        else:
            print("nie dziel przez zero")
    else:
        print("nie znam takiego działania")
