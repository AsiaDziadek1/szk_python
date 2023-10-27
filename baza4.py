# sqlite3 - baza sql w jednym pliku, może być przechowywana w pamięci
import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza została podłaczona")

    insert = """
        insert into software (id, name, price) values (1, 'Python', 5000)
        """
    # cursor.execute(insert)
    # sql_connection.commit()

    select ="""
    select * from software where id =1
    """

    update = """
    update software set price = 2000 where id = 1;
    """

    # cursor.execute(update)
    # sql_connection.commit()

    delete = """
    delete from software where id=1;
    """
    cursor.execute(delete)
    sql_connection.commit()


    for row in cursor.execute(select):
        print(row)  #(1, 'Python', 5000.0)

except sqlite3.Error as e:
    print("Błąd podczas podłaczania bazy danych", e)
finally:  # wykonuje sie zawsze
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")