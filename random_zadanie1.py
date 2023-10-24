import random

# random - biblioteka do działania z liczbami pseudolosowymi

print(random.randint(1, 6))  # 1...6 int
print(random.random())  # float 0....0.99999
print(random.random() * 6)  # float 0...5.999
print(random.randrange(6))  # 0...5 int
print(random.randrange(1, 6))  # 1...5 int

lista = [5, 7, 45, 34, 56]
print(random.choice(lista))  # 45

lista2 = list(range(1,50))  # int 1...49
print(lista2)

lista_wynik = []
wyn = random.choice(lista2)
lista2.remove(wyn)
lista_wynik.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista_wynik.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista_wynik.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista_wynik.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista_wynik.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista_wynik.append(wyn)
print(lista_wynik)  # [41, 44, 26, 30, 33, 8]

print(random.choices(lista2, k=6))  #[22, 47, 23, 10, 38, 31] liczby moga się powtarzać
print(random.sample(lista2,6))  #[24, 8, 5, 31, 41, 37] liczby unikatowe
