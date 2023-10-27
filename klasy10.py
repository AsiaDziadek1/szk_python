# dekorator
# dodaje do funkcji dodatkowe właściwości

def dekor(funk):

    def wew():
        print("Dekorujemy")
        return funk()  # tu z nawiasami bo wynik działania
    return wew # tu bez nawiasów bo adres w pamieci

@dekor  # po dodaniu @dekor do funkcji dekorujemy ją
def hej():
    print('Hej!!!')

hej()
# dk = dekor(hej)
# dk()

