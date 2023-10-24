# if - warunek - instrukcja sterowania przepływem

odp = True  # True - prawda, False - fałsz
if odp:
    print("Brawo")
else:  # w przeciwnym wypadku
    print("Ucz się dalej")
print("Idę dalej")

podatek = 0.0
zarobki = int(input("Podaj dochód"))
if zarobki < 10000:
    podatek = 0.0
elif zarobki < 30000:
    podatek = 0.2
elif zarobki < 100000:
    podatek = 0.4
else:
    podatek = 0.6

print(f"Płacisz {zarobki * podatek}")
# kolejność ma znaczenie


suma_zam = 50
if suma_zam > 152:
    rabacik = 25
else:
    rabacik = 0
print(f"Rabacik wynosi: {rabacik}")

rabat = 25 if suma_zam > 150 else 0
print(f"Rabacik wynosi: {rabat}")


#zasymulujemy system zbierania logów i wyświetlania komunikatów
# w zależności od tego jaki system i jaki komunikat przysłał
lista_bledow =[]
alert_system = "console"
error = "krytyczny"
error_message = "Stało się coś strasznego"

if alert_system == 'email':
    print(error_message)
elif alert_system == 'console':
    if error == "medium":
        lista_bledow.append('ostrzeżenie')
    elif error =="krytyczny":
        lista_bledow.append('krytyczny')
    else:
        lista_bledow.append("inny")

print(lista_bledow)


#zrobić test
#zadać pytanie
#odczytać odpowiedz
#sprawdzić odpowiedz i ocenić

odp = input(f"Ile bokow ma trójkąt")

if odp == "3"
    print("Brawo")
else:
    print("Masz w książce")






