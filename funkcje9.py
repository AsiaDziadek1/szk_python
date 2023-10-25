def odejmij(a, b):
    return a - b


print(odejmij(6, 7))
# lambda - skrócona wersja funkcji
odejmij2 = lambda a, b: a - b  # return jest w lambda domyślnie
print(odejmij2(6, 7))

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(8))  # dziecko
print(wiek(15))  # nastolatek
print(wiek(25))  # dorosły

lista = [1, 2, 3, 4, 6, 7, 8, 10, 23, 58]
l = []  # pusta lista

for i in lista:
    l.append(i * 2)
print(l)  # [2, 4, 6, 8, 12, 14, 16, 20, 46, 116]


#  map() - bierze każdy element z kolekcji, wykonuje na nim operacje wg zadanej funkcji

def zmien(x):
    return x * 2
print(f"Zastosowanie map(): {list(map(zmien,lista))}")  #Zastosowanie map(): [2, 4, 6, 8, 12, 14, 16, 20, 46, 116]
print(f"Zastosowanie map(): {list(map(lambda x: x*2,lista))}")   #Zastosowanie map(): [2, 4, 6, 8, 12, 14, 16, 20, 46, 116]
# lambda uzyta jako funkcja anonimowa zdefiniowana w miejscu wykonania

# filter() - bierze elementy kolekcji i sprawdza wg warunku zadanego funkcji
print(f"Zastosowanie filter(): {list(filter(lambda x: x <3,lista))}")  #Zastosowanie filter(): [1, 2]

#wyfiltrować listę l warunkiem gdzie x>8
print(f"Zastosowano filter(): {list(filter(lambda x: x>8, l))}")  #Zastosowano filter(): [12, 14, 16, 20, 46, 116]

# wyfiltrować z listy l większe od 3, mniejsze od 20
print(f"Zastosowano filter(): {list(filter(lambda x: 3< x <20, l))}")  #Zastosowano filter(): [4, 6, 8, 12, 14, 16]


