#  pliki csv - dane rozdzielone przecinkiem lub innym dopuszczonym znakiem podziału

# Zenek, Michał, Radek, Monika
import csv
#biblioteka do pracy z plikami csv

fields = ['name', 'brand', 'year', 'cgpa']
row = ['radek', 'coe', '3', '0']


filename = 'records.csv'
dict_list = [
{'name': 'radek', 'brand': 'coe', 'year': '3', 'cgpa': '0'},
{'name': 'Zosia', 'brand': 'cos', 'year': '4', 'cgpa': '9'},
{'name': 'Asia', 'brand': 'cot', 'year': '5', 'cgpa': '11.5'},
{'name': 'Monika', 'brand': 'cob', 'year': '9', 'cgpa': '8'},
{'name': 'Zenek', 'brand': 'coo', 'year': '1', 'cgpa': '2'},
]

dict_2 = dict(zip(fields, row))
print(dict_2)

with open(filename, 'w', newline='') as csv_f:
    # csvwriter = csv.writer(csv_f)
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter=";")
    # csvwriter.writerow(row)  #zapisanie pojedynczego wiersza z listy
    csvwriter.writeheader()  #zapisanie nagłówka czyli nazw kolumn
    csvwriter.writerow(dict_2)  #zapisanie danych ze słownika do csv
    csvwriter.writerows(dict_list)  # zapisanie listy słowników jako kolejnych wierszy




