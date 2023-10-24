# match case - instrukcja sterowania przepływem
lista = []
lang = input("Podaj znany Ci język programowania")

match lang.lower().replace(" ",""):
    case "python":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case "c++":
        lista.append(lang)
    case _:  # odpowiednik else
        print('Domyslny')
print(lista)
