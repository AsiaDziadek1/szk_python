dictionary = {'imie': "Radek", 'nazwisko': "Kowalski"}
print(dictionary)
print(type(dictionary))

for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)

#zwraca wartości
for v in dictionary.values():
    print(v)

# zwraca pary
for p in dictionary.items():
    print(p)

#rozpakowanie krotki
for k, v in dictionary.items():
    print(k, v)


dict1 = {'name': 'imie', 'company': 'Comarch' }
print(dict1)
print({value: key for key, value in dict1.items()})  #{'imie': 'name', 'Comarch': 'company'}
d2 = {}
for key, value in dict1.items():
    d2[value]=key  #{'imie': 'name', 'Comarch': 'company'}
print(d2)
