class MyException (Exception): # dziedziczenie po Exception - głównym wyjątku w Pythonie

    def __init__(self,message):
        super().__init__(message)

try:
    # print(6/0)
    raise ValueError("Błąd wartości")  #Błąd Błąd wartości
    # po wystąpieniu pierwszego błedu program przerywa działanie i kieruje sie do skcji obsługi błedów
    raise MyException("Wystapił wyjatek") # raise rzucenie wyjątku
except ZeroDivisionError:
    print("dzielenie przez zero")
except MyException:
    print("Wystąpił wyjatek MyException")
except Exception as e:  # worek na pozostałe błędy
    print("Błąd:", e)

print("Program nadal działa")
