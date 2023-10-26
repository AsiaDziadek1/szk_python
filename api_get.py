# crud - create, read, update, delete
# HTTP - post, get, put/patch, delete
# baza - insert, select, update, delete
# REST API
import requests as re
# lub pip install requests w terminalu

# url  =  'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'
url  =  'http://api.nbp.pl/api/exchangerates/rates/A/USD/'

# NBP wskazuje aby użyć metody http get
response = re.get(url)
print(response)  #<Response [200]>  - status odpowiedzi, 200 oznacza że jest ok
# 2.. - jest ok
# 3... - błedy przeglądarki, np. przekierowania
# 4... - błąd danych np. 404 - brak zasobów, 400 bad request
# 5... - błedy wewnętrzne serwera np problem z bazą

# Komunikaty błędów
# W przypadku braku danych dla prawidłowo określonego zakresu czasowego zwracany jest komunikat 404 Not Found
# W przypadku zadania nieprawidłowo sformułowanych zapytań serwis zwraca komunikat 400 Bad Request
# W przypadku zapytania przekraczającego limit zwracanych danych serwis zwróci komunikat 400 Bad Request - Przekroczony limit

table = response.json()
print(table)
#{'table': 'A', 'currency': 'euro', 'code': 'EUR',
# 'rates': [{'no': '207/A/NBP/2023', 'effectiveDate': '2023-10-25', 'mid': 4.4758}]}
print(type(table))  #<class 'dict'>
print(table.keys())

for k in table.keys():
    print(k,table[k])
print(table['rates'][0])
for k in table['rates'][0]:
    print(k, table['rates'][0][k])

url_zloto = 'http://api.nbp.pl/api/cenyzlota'
# NBP wskazuje aby użyć metody http get
response = re.get(url_zloto)
print(response)  #<Response [200]>  - status odpowiedzi, 200 oznacza że jest ok
# 2.. - jest ok
# 3... - błedy przeglądarki, np. przekierowania
# 4... - błąd danych np. 404 - brak zasobów, 400 bad request
# 5... - błedy wewnętrzne serwera np problem z bazą

# Komunikaty błędów
# W przypadku braku danych dla prawidłowo określonego zakresu czasowego zwracany jest komunikat 404 Not Found
# W przypadku zadania nieprawidłowo sformułowanych zapytań serwis zwraca komunikat 400 Bad Request
# W przypadku zapytania przekraczającego limit zwracanych danych serwis zwróci komunikat 400 Bad Request - Przekroczony limit

gold = response.json()
print(gold)  #[{'data': '2023-10-26', 'cena': 269.6}]

print(type(gold))  #<class 'list'>
print(gold[0]['cena'])  #269.6

gold_dict=gold[0]
for k in gold_dict:
    print(k,'=>',gold_dict[k])
# data => 2023-10-26
# cena => 269.6












