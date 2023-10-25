a = 10
b = 10


def dodaj():
    a = 6  # a i b zdeklarowane lokalnie
    b = 7  #nie wpływaja na wartość globalną
    print(a, b)

def dodaj2():
    print(a+b)  #uzyje z globalnego scopa(zakresu)

def dodaj3():
    global a
    a=6
    b=7
    print(a+b)

def dodaj4(a,b):
    print(a,b)

print(f"Zmienna a z góry {a}")  #zmienna a z góry
dodaj()  #6 7
print(f"Zmienna a z góry {a}")  #zmienna a z góry
dodaj2()  #20
print(f"Zmienna a z góry {a}")  #zmienna a z góry
dodaj3()
print(f"Zmienna a z góry {a}")  #zmienna a z góry
dodaj2()  #16
dodaj4(a,b)

