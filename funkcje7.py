def connect(**opcje):  # parametry słownikowe
    print("funkcja connect")
    print("opcje",opcje)
    print(type(opcje))  # <class 'dict'>

    connect_param = {
        'host': '127.0.0.7',
        'part': '8088'
    }
    print(connect_param)
    connect_param['part'] = opcje
    print("słownik w słowniku",connect_param)


def connect_all(*args, **kwargs):
    print("funkcja connect_all")
    print(args)  # pozycyjne
    print(kwargs)  # nazwane


connect(a=6, b=7, c=9)  # parametry nazwane
#  {'a': 6, 'b': 7, 'c': 9}
#  przy takiej konstrukcji wszystkie paramtry przekazywane do funkcji po nazwie zostana
#  zamienione na pary klucz, wartość w słowniku
connect()
connect(name='Radek')
connect_all(1, 2)  #(1, 2)
connect_all(1, 2, a=9)  #{'a': 9}
connect(a=9)
