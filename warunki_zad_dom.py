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

    a = float(input("Podaj pierwszą liczbe"))
    b = float(input("Podaj drugą liczbe"))


    match odp:
        case '5':
            break
        case '1':
            print(a + b)
        case  '2':
            print(a - b)
        case '3':
            print(a * b)
        case  '4':
            if b != 0:
                print(a / b)
            else:
                print("nie dziel przez zero")
        case '5':
            break
        case _:
            print("nie znam takiego działania")
