teksty = "Witaj świecie"
print(teksty)
print(teksty.upper())  # WITAJ ŚWIECIE
print(teksty)
tekst2 = teksty.upper()
print(tekst2)

tekst3 = teksty.lower()
print(tekst3)  # witaj świecie
print(teksty)  # Witaj świecie
print(tekst2)  # WITAJ ŚWIECIE

print(teksty.removeprefix("Witaj"))  # świecie
print(teksty.removesuffix("świecie"))  # Witaj
print(teksty.removeprefix("Wi").removesuffix("cie"))
print(teksty)
print(teksty.count("i"))
print(teksty.count("i", 0, 4))  # sprawdza indeksy od 0 do 3 (4 już nie bierze pod uwage)
# Asia
# 01234 - indeksowanie od 0

encoded_s = teksty.encode('utf-8')
print(encoded_s)
# b - zapis binarny
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))

imie = "Asia"
tekst_format = f"\tMam na imię {imie}\n i lubie Pythona\b" # f - tekst sformatowany
# mozemy umiescic wartość w tekście poprzez {}
print(tekst_format)
# \t tabulator
# \n nowa linia
# \b backspace

starszy = "witaj %s!"
print(starszy % imie)
print("witaj {}!".format(imie))  #witaj Asia!
print("""Tekst
    WIELOLINIJKOWY""")

