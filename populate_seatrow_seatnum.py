
import mysql.connector
import keyring
import string


def populate_1_letter_to_seat_row():
    list_letters_not_included = {'S', 'T', 'U', 'V', 'W', 'Y', 'Z', 'I', 'X'}
    insert_form = "INSERT into SeatRow (new_SeatRow) VALUES ('{0}')"
    for i in string.ascii_uppercase:
        if i in list_letters_not_included:
            continue
        else:
            my_cursor.execute(insert_form.format(i))
            my_db.commit()


def populate_2_letter_to_seat_row():
    list_of_letters_included = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'}
    insert_form = "INSERT into SeatRow (new_SeatRow) VALUES ('{0}{0}')"
    for i in string.ascii_uppercase:
        if i in list_of_letters_included:
            my_cursor.execute(insert_form.format(i, i))
            my_db.commit()
        else:
            continue


def populate_number_to_seat_1_to_15():
    insert_form = "INSERT into SeatNum (new_SeatNum) VALUES ({0})"
    for i in range(1, 16):
        my_cursor.execute(insert_form.format(i))
        my_db.commit()


def populate_number_to_seat_101_to_126():
    insert_form = "INSERT into SeatNum (new_SeatNum) VALUES ({0})"
    for i in range(101, 127):
        my_cursor.execute(insert_form.format(i))
        my_db.commit()


if __name__ == '__main__':
    pw = keyring.get_password('mysql', 'root')
    my_db = mysql.connector.connect(host='localhost', user='root', password=pw, database='theater')
    my_cursor = my_db.cursor()
    populate_1_letter_to_seat_row()
    populate_2_letter_to_seat_row()
    populate_number_to_seat_1_to_15()
    populate_number_to_seat_101_to_126()
    my_db.close()







