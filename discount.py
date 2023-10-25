from datetime import date, timedelta, datetime

today = date.today()
print(today)   #2023-10-25
print(type(today))  #<class 'datetime.date'>

time = datetime.now()
print(time)  #2023-10-25 09:36:41.475726
print(type(time))  #<class 'datetime.datetime'>

tomm = today + timedelta(days=1)
print(tomm)  #2023-10-26
print(type(tomm))  #<class 'datetime.date'>

print(time.hour)
print(time.day)

formated_date = datetime.now().strftime('%d/%m/%Y')
print(formated_date)  #25/10/2023

formated_time = datetime.now().strftime('%H:%M')
print(formated_time)  #09:48
formated_time2 = datetime.now().strftime('%I:%M %p')
print(formated_time2)   #09:51 AM
print(formated_time.removeprefix("0"))  #9:53

products =[
    {'sku':1, 'exp_date':today, 'price': 100.0},
    {'sku':2, 'exp_date':tomm, 'price': 80.0},
    {'sku':3, 'exp_date':today, 'price': 50.0},
    {'sku':4, 'exp_date':today, 'price': 250.0},
]

# print(products)

for product in products:
    #  print(product)
    if product['exp_date'] != today:
        continue  # petla konczy działanie i bierze kolejny element z listy
    #  print(f"{product['exp_date']}: jade dalej")
    product['price'] *= 0.8  #price = price * 0.8
    print(f"""
Price for sku = {product['sku']}
is now {product['price']}""")












