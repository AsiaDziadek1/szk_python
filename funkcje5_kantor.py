# stworzenie funkcji kantor zawierajacej 2 funkcje usd i eur
# wykorzystanie funkcji wewnętrznych w zalezności od parametru inicjującego

def kantor(waluta):
    print("Uruchomienie kantoru")

    def usd(kwota=0):
        print(f"Wymieniam {kwota} dol ={kwota * 4.10} ")

    def eur(kwota=0):
        print(f"Wymieniam {kwota} eur ={kwota * 4.50} ")

    if waluta == 'eur':
        return eur
    else:
        return usd


kantor_usd = kantor('usd')
kantor_usd()  # dolary

# dodać mozliwość przekazywania kwoty do wymiany
# ładnie wypisać przeliczoną kwotę
# np: wymieniam 100 dol = 410 pln
kantor_usd(1000)

# stworzyć i użyć kantor eur
kantor_eur = kantor('eur')
kantor_eur(1000)
