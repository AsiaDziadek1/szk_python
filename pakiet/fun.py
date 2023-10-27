def powitanie():
    print("cześć")


def info():
    print("jestem pakietem")

# print("Cos dowolnego")

print(__name__)
# gdy program uruchamiany bezposrednio
#__name__ ma wartość __main__
# gdy program jest uruchamiany z pakietu
# __name__ ma wartość nazwy pakietu jaki wywołał np: pakiet.fun
if __name__ == '__main__':
    print("Cos dowolnego")
