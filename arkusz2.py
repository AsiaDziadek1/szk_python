import pandas as pd

excel_data = pd.read_excel('sales.xlsx', sheet_name="Arkusz1")
#excel_data = pd.read_excel('sales.xlsx')  # gdy mamy jeden arkusz
print(excel_data)

data = pd.DataFrame(excel_data)
#   Sales Date    Sales Person  Amount
# 0 2018-05-12      Sila Ahmed   60000
# 1 2019-12-06     Mir Hossain   50000
# 2 2020-08-09    Sarmin Jahan   45000
# 3 2021-04-07  Mahmudul Hasan   30000
print("The content is: \n",data)  #\n przenosi do nowej lini
# The content is:
#    Sales Date    Sales Person  Amount
# 0 2018-05-12      Sila Ahmed   60000
# 1 2019-12-06     Mir Hossain   50000
# 2 2020-08-09    Sarmin Jahan   45000
# 3 2021-04-07  Mahmudul Hasan   30000

print(data.values)
print(data.columns)
print(data.items)

print(data.index[-1])
print(data.index.max())  # ostatni numer indeksu wiersza
print(data.tail(1))  # ostatni wiersz, tail (zwraca ostatnie n wierszy, gdy n=1 zwraca ostatni wiersz)

print(data.columns[2])  #Amount
print(data.iloc[1,2])  #konkretna komórka
print("Wiersz", data.iloc[1])  #wiersz
print("Wiersz2", type(data.iloc[1]))  #wiersz
print("------")
for i in data.iloc[1]:
    print(i)

print(data.loc[1, "Amount"])  # w loc mozna poznać po nazwie
print(data.iloc[1, 2])  # w iloc trzeba podac indeks kolumny


print(data.loc[1])




