import pandas as pd
# pip install pandas w terminalu

data = pd.read_csv('records.csv', delimiter =",")
print(data)
#    name brand  year  cgpa
# 0   radek   coe     3   0.0
# 1   radek   coe     3   0.0
# 2   Zosia   cos     4   9.0
# 3    Asia   cot     5  11.5
# 4  Monika   cob     9   8.0
# 5   Zenek   coo     1   2.0

print(data.columns)  #Index(['name', 'brand', 'year', 'cgpa'], dtype='object')
print(data.values)
# [['radek' 'coe' 3 0.0]
#  ['radek' 'coe' 3 0.0]
#  ['Zosia' 'cos' 4 9.0]
#  ['Asia' 'cot' 5 11.5]
#  ['Monika' 'cob' 9 8.0]
#  ['Zenek' 'coo' 1 2.0]]

print(data.values[0])  #['radek' 'coe' 3 0.0]
print(data.items)
# <bound method DataFrame.items of      name brand  year  cgpa
# 0   radek   coe     3   0.0
# 1   radek   coe     3   0.0
# 2   Zosia   cos     4   9.0
# 3    Asia   cot     5  11.5
# 4  Monika   cob     9   8.0
# 5   Zenek   coo     1   2.0>





