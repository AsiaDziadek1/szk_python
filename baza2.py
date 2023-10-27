# sqlite3 - baza sql w jednym pliku, może być przechowywana w pamięci
import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    query = """
    create table if not exists developers(
    id integer primary key,
    name text not null,
    email text not null unique,
    joining_date datetime,
    salary real not null);
    """
    insert = """
    insert into developers (id, name, email, salary) values (1, 'Radek', 'raj@wp.pl', 5000)
    """
    cursor = sql_connection.cursor()
    print("Baza została podłaczona")

    sql_connection.execute(query)

    sql_connection.execute(insert)

    sql_connection.close()
except sqlite3.Error as e:
    print("Błąd podczas podłaczania bazy danych", e)
finally:  # wykonuje sie zawsze
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")