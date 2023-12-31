wiek = 47  # int
rok = 2023  # int
temp = 36.6  # float
wiek2 = 37.5  # float

print(wiek)
print(type(wiek2))  # <class 'float'>
print(3 * "Radek")  # RadekRadekRadek

print(wiek + rok)
print(wiek * rok)
print(wiek / rok)  # dzielenie daje w wyniku float
print(wiek - rok)
print(wiek // rok)  # część całkowita z dzielenia
print(wiek % rok)  # reszta z dzielenia tzw modulo
print(wiek ** rok)  # potęgowanie

print(5 % 2)  # 1 bo 2*2+1=5
print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
# wystepuje bład zaokrąglenia
print(f"{0.2 + 0.7:.1f}")
print(f"Sprawdzenie zmiennej temp {wiek} {temp}")
print(f"""
{wiek}
{temp}""")

# typ logiczny
# prawda lub fałsz
# True, False
czy_znasz_python = True
print(czy_znasz_python)
print(type(czy_znasz_python))  # <class 'bool'>
print(int(czy_znasz_python))  # True - 1, false - 0
x = 1
print(bool(x))  # bool() - zamiana na tryb logiczny
x = 100
print(bool(x))
x = -10
print(bool(x))
x = 0
print(bool(x))
x = "Radek"
print(bool(x))
x = ''
print(bool(x))
x = None
print(bool(x))  #False, None - odpowiednik null (nic)

#działania logiczne
print(True and True)  #True
print(True and False)  #False
print(False and True)  #False
print(False and False)  #False
print(True or True)  #True
print(True or False)  #True
print(False or True)  #True
print(False or False)  #False

#not - negacja
print(not False)  #True
print(not True)  #False

x = 0
print(not x == 1)  #True

a = 8
b = 7

print(f"Porównanie {a} > {b}", a >b)  # Porównanie 8 > 7 True
print(f"Porównanie {a} < {b}", a <b)  #Porównanie 8 < 7 False
print(f"Porównanie {a} == {b}", a ==b)  #porównanie (dwa znaki ==) Porównanie 8 == 7 False
print(f"Porównanie {a} != {b}", a != b)  # !=czy rózne Porównanie 8 != 7 True
print(f"Porównanie {a} >= {b}", a >=b)  #Porównanie 8 >= 7 True
print(f"Porównanie {a} <= {b}", a <= b)  #Porównanie 8 <= 7 False




