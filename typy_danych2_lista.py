# lista - kolekcja, przechowuje różne typy
# zachowuje kolejność dodawania
lista = []  # pusta lista, []
print(lista)
print(type(lista))  # <class 'list'>

lista.append("Radek")
lista.append("Maciek")
lista.append("Jasko")
lista.append("Zenek")
print(lista)  # ['Radek', 'Maciek', 'Jasko', 'Zenek']
#              0(-4)        1(-3)    2(-2)     3(-1)
# indeksowanie od 0
print(lista[0])  # Radek
print(lista[2])  # Jasko
# print(lista[10])  #IndexError: list index out of range
print(lista[-1])
print(len(lista))  # 4 - długość kolekcji
print(lista[3])
print(lista[1])
print(lista[-3])
print(lista[0:3])  # ['Radek', 'Maciek', 'Jasko']
print(lista[:3])  # ['Radek', 'Maciek', 'Jasko']
print(lista[2:])  # ['Jasko', 'Zenek'] do końca włacznie z ostatnim
print(lista[0:-2])  # ['Radek', 'Maciek']

# nadpisanie elementu
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Zenek']

# wstawić element do listy na konkretne miejsce
lista.insert(1, "Marcin")  # ['Radek', 'Marcin', 'Maciek', 'Mikołaj', 'Zenek']
print(lista)

# usunięcie elementu (pierwszy napotkany)
lista.remove("Maciek")
print(lista)

indeks = lista.index("Zenek")
print(indeks)

# usunięcie po indeksie
print(lista.pop(3))  # zwraca usunięty element - Zenek
print(lista)

a = 1
b = 3
a = b
print(a)
b = 7
print(a)
lista2 = lista  # kopiowanie referencji (adresu pamięci)
lista3 = lista.copy()  # kopiowanie wartości listy do drugiej
print(lista)
print(lista2)
lista.clear()  # usuniecie wszystkich elementów z listy
print(lista)
print(lista2)
print(id(lista))
print(id(lista2))
print(lista3)
print(id(lista3))

liczby = [54, 999, 34, 22, 12, 34, 687]
# liczby = [54,999,34,22,12,34,687, "A"]  #TypeError: '<' not supported between instances of 'str' and 'int'
print(liczby)  # [54, 999, 34, 22, 12, 34, 687]
liczby.sort()
print(liczby)  # [12, 22, 34, 34, 54, 687, 999]

lista_osoby = ['radek', 'ola']
lista_osoby.sort(reverse=True)
print(lista_osoby)  # sortowanie i odwrócenie kolekcji
liczby.reverse()  # tylko odwrócone
print(liczby)
liczby[3] = 6666
print(liczby[0:3])
print(liczby[-2])
print(liczby[-3:])  # [34, 22, 12]

liczby.remove(54)
print(liczby)

print(liczby.pop(3))
print(len(liczby))

tekst = "Python"
lista_1 = list(tekst)  # zamiana str na list - rozpakowanie sekwencji
print(lista_1)  # ['P', 'y', 't', 'h', 'o', 'n']

lista_2 = [tekst]
print(lista_2)  #['Python']

krotka = tuple(liczby)  # zamiana listy na krotke, tuple
print(type(krotka))  #<class 'tuple'>
print(krotka)  #(999, 687, 6666, 22, 12)

