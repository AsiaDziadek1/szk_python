# json - {"name": "Radek"}
# obiekt typu klucz-wartość
# odpowiednikiem jsona w pythonie jest słownik

import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)  # dump - komenda zrzuć do pliku
# {"name": "Radek", "age": 40, "czy_pali": null}
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }  - tak układa indent

# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# } - sor_keys - posortowane alfabetycznie po nazwie klucza

with open("nasze_dane.json", "r") as fh:
    data = json.load(fh)  # wczytanie jsona do słownika w python
print(data)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(data))  # <class 'dict'>
print(data['name'])  # Radek

json_text = json.dumps(data)  #zamiana słownika na json w formie string
print(json_text)  #{"age": 40, "czy_pali": null, "name": "Radek"}
string_json = json.loads(json_text)  #zamiana jsona na słownik
print(string_json)  #{'age': 40, 'czy_pali': None, 'name': 'Radek'}
