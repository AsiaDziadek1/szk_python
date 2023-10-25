# funkcje zagnieżdżone
def fun1():
    print("To jest fun1")

    def fun2():  # funkcja zagnieżdżona (definicja)
        print("To jest fun2")
    return fun2  #zwracamy tylko adres funkcji (nie dajemy ())


print(fun1())  #<function fun1.<locals>.fun2 at 0x000001D53EB9B6A0>
xfun = fun1()
print(xfun)   #<function fun1.<locals>.fun2 at 0x000001AAF565B6A0>
print(type(xfun))  #<class 'function'>
xfun()
