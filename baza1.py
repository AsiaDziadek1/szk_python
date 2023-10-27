# sqlite3 - baza sql w jednym pliku, może być przechowywana w pamięci
import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza została podłaczona")
except sqlite3.Error as e:
    print("Błąd podczas podłaczania bazy danych", e)
finally:  # wykonuje sie zawsze
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")
