# funkcje zwracajace wynik
# musza byc zakończone słowem return

def dodaj(a,b):
    return a+b


print(dodaj(6, 9))


#napisac funkcje zwracającą wynik 3 argumenty, każdy ma domyślną wartość
#wypisać możliwe sposoby jej wyswietlenia

def dodaj2(a=0, b=0, c=0):
    return a+b+c

def oblicz_vat(cena,vat=23):
    return cena * (100 + vat) /100

print(dodaj2())
print(dodaj2(4,5,2))
print(dodaj2(c=2, b=5, a=2))
#  print(dodaj2(a=2, b=5, 2))  #SyntaxError: positional argument follows keyword argument
print(dodaj2(1, b=2, c=5))
print(oblicz_vat(1000))
print(oblicz_vat(1000,7))
print(oblicz_vat(vat=15, cena=1000))



