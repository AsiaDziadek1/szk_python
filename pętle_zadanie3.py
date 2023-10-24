# while - petla sterowana warunkiem

licznik = 0
while True:
    licznik += 1
    print("komunikat1")
    if licznik > 10:
        break  # przerwanie bieżącej petli
print(licznik)  # 11
licznik = 0
while licznik < 10:
    print("komunikat2")
    licznik += 1

lista = []
lista2 = []
while True:
    wej = input("Podaj liczbę")
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))
print(lista)  # ['5', '3', '6', '2', '5', '5', '4']
print(lista2)  # [5, 3, 6, 2, 5, 5, 4]
