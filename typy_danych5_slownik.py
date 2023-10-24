# słownik - para klucz wartość
# {"name" : "Asia"}
# klucze nie moga sie powtarzać

dictionary = {}  # pusty słownik
print(type(dictionary))  # <class 'dict'>

dictionary['imie'] = "Asia"
print(dictionary)  # {'imie': 'Asia'}
dictionary['wiek'] = 39
print(dictionary)  # {'imie': 'Asia', 'wiek': 39}

print(dictionary.values())  # dict_values(['Asia', 39])
print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.items())  # dict_items([('imie', 'Asia'), ('wiek', 39)])

dictionary.update({"date": "12-12-2023"})
print(dictionary)  # {'imie': 'Asia', 'wiek': 39, 'date': '12-12-2023'}

dict2 = {'x': 2}
dict2.update([("y", 5), ("z", 7)])
print(dict2)  # {'x': 2, 'y': 5, 'z': 7}

dict3 = {"kot": "cat", "pies": "dog"}
print(dict3)
print(dict3["kot"])  #cat
print(f"Umiem przetłumaczyć {dict3.keys()}")
key = input("Podaj słowo do przetłumaczenia")  #pobieranie danych od użytkownika, zawsze zwraca str
print(dict3[key.lower().replace(" ","")])
#lower() - zamiana na małe, replace() - zmiana spacji na pusty ciąg znaków

#kalkulator
#pobrać a i b od uzytkownika
# wyświetlić wynik
liczba1 = int(input("podaj liczbe 1"))
liczba2 = int(input("Podaj liczbe 2"))
liczba3 = int(liczba1)+int(liczba2)
print(liczba3)
#int() rzutowanie int(całkowite) float() - rzutowanie zmiennoprzecinkowe