import csv

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r') as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)  #;, domyslnie jest przecinek
    print(dialect.quotechar)  #" - odczytuje rodzaj cudzysłowia, "" jest domyslny
    csv_f.seek(0)  #zerujemy ponownie wskaźnik, tak zeby wrócił do pierwszego wiersza

    # csvreader = csv.reader(csv_f, delimiter=";")
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)
    print(csvreader)  #<_csv.reader object at 0x000002D85D603FA0>
    fields = next(csvreader)  #pobiera element i wstawia wskaźnik na nastepny
    for row in csvreader:
        rows.append(row)

print(fields)  #['name;brand;year;cgpa']
print(type(fields))  #<class 'list'>
print(rows)
