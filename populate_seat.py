import mysql.connector
import keyring


def get_list_of_numbers():
    my_cursor.execute("select * from SeatNum")
    numbers = my_cursor.fetchall()
    list_of_nums = []
    for number in numbers:
        list_of_nums.append(number[0])
    return list_of_nums


def get_list_of_letters():
    my_cursor.execute("select * from SeatRow")
    numbers = my_cursor.fetchall()
    list_of_letters = []
    for number in numbers:
        list_of_letters.append(number[0])
    return list_of_letters


def populate_data_for_wheel_chair_seat(list_of_letters, list_of_numbers):
    list_of_letters_included = {'P', 'Q', 'R'}
    mysql_form = "Insert into Seat (SeatRow_new_SeatRow, SeatNum_new_SeatNum, Section, Side, PricingTier, Wheelchair)" \
                 "values ('{0}',{1}, 'MAIN FLOOR', '{2}', 'Side', true)"
    for letter in list_of_letters:
        for number in list_of_numbers:
            if number in range(109, 123) and letter in list_of_letters_included:
                if number % 2 == 0:
                    my_cursor.execute(mysql_form.format(letter, number, 'Right'))
                    my_db.commit()
                else:
                    my_cursor.execute(mysql_form.format(letter, number, 'Left'))
                    my_db.commit()
            else:
                continue


def populate_data_for_middle_main_floor_(list_of_letters, list_of_numbers):
    mysql_form = "Insert into Seat (SeatRow_new_SeatRow, SeatNum_new_SeatNum, Section, Side, PricingTier, Wheelchair)" \
                 "values ('{0}',{1}, 'MAIN FLOOR', '{2}', 'Orchestra', false)"
    list_of_1st_rows = {'A', 'B', 'C'}
    list_of_2nd_rows = {'D', 'E', 'F'}
    list_of_3rd_rows = {'G', 'H', 'J'}
    list_of_4th_rows = {'K', 'L', 'M'}
    list_of_5th_rows = {'N', 'O', 'P'}
    list_of_6th_rows = {'Q', 'R'}

    for letter in list_of_letters:
        for number in list_of_numbers:
            if number in range(1, 16):
                if letter in list_of_1st_rows and number in range(1, 11):
                    my_cursor.execute(mysql_form.format(letter, number, 'Middle'))
                    my_db.commit()
                elif letter in list_of_2nd_rows and number in range(1, 12):
                    my_cursor.execute(mysql_form.format(letter, number, 'Middle'))
                    my_db.commit()
                elif letter in list_of_3rd_rows and number in range(1, 13):
                    my_cursor.execute(mysql_form.format(letter, number, 'Middle'))
                    my_db.commit()
                elif letter in list_of_4th_rows and number in range(1, 14):
                    my_cursor.execute(mysql_form.format(letter, number, 'Middle'))
                    my_db.commit()
                elif letter in list_of_5th_rows and number in range(1, 15):
                    my_cursor.execute(mysql_form.format(letter, number, 'Middle'))
                    my_db.commit()
                elif letter in list_of_6th_rows and number in range(1, 16):
                    my_cursor.execute(mysql_form.format(letter, number, 'Middle'))
                    my_db.commit()
            else:
                continue


def populate_data_for_right_main_floor(list_of_letters, list_of_numbers):
    mysql_form = "Insert into Seat (SeatRow_new_SeatRow, SeatNum_new_SeatNum, Section, Side, PricingTier, Wheelchair)" \
                 "values ('{0}',{1}, 'MAIN FLOOR', '{2}', '{3}', false)"
    list_of_wheel_chair_seats = {'P', 'Q', 'R'}
    orchestra_right_seats = {102, 104, 106}
    list_of_main_right_seats_1 = {'B', 'C', 'D', 'E'}
    list_of_main_right_seats_2 = {'F', 'G', 'H', 'J'}
    list_of_main_right_seats_3 = {'K', 'L', 'M', 'N'}
    list_of_main_right_seats_4 = {'O', 'P', 'Q', 'R'}
    for letter in list_of_letters:
        for number in list_of_numbers:
            if len(letter) == 1 and number in range(101, 123) and number % 2 == 0:
                if letter in list_of_wheel_chair_seats and number in range(110, 123):
                    continue
                elif number in orchestra_right_seats:
                    my_cursor.execute(mysql_form.format(letter, number, 'Right', 'Orchestra'))
                    my_db.commit()
                elif letter == 'A' and number in range(108, 115):
                    my_cursor.execute(mysql_form.format(letter, number, 'Right', 'Side'))
                    my_db.commit()
                elif letter in list_of_main_right_seats_1 and number in range(108, 117):
                    my_cursor.execute(mysql_form.format(letter, number, 'Right', 'Side'))
                    my_db.commit()
                elif letter in list_of_main_right_seats_2 and number in range(108, 119):
                    my_cursor.execute(mysql_form.format(letter, number, 'Right', 'Side'))
                    my_db.commit()
                elif letter in list_of_main_right_seats_3 and number in range(108, 121):
                    my_cursor.execute(mysql_form.format(letter, number, 'Right', 'Side'))
                    my_db.commit()
                elif letter in list_of_main_right_seats_4 and number in range(108, 123):
                    my_cursor.execute(mysql_form.format(letter, number, 'Right', 'Side'))
                    my_db.commit()
            else:
                continue


def populate_data_for_left_main_floor(list_of_letters, list_of_numbers):
    mysql_form = "Insert into Seat (SeatRow_new_SeatRow, SeatNum_new_SeatNum, Section, Side, PricingTier, Wheelchair)" \
                 "values ('{0}',{1}, 'MAIN FLOOR', '{2}', '{3}', false)"
    list_of_wheel_chair_seats = {'P', 'Q', 'R'}
    orchestra_left_seats = {101, 103, 105}
    list_of_main_right_seats_1 = {'B', 'C', 'D', 'E'}
    list_of_main_right_seats_2 = {'F', 'G', 'H', 'J'}
    list_of_main_right_seats_3 = {'K', 'L', 'M', 'N'}
    list_of_main_right_seats_4 = {'O', 'P', 'Q', 'R'}
    for letter in list_of_letters:
        for number in list_of_numbers:
            if len(letter) == 1 and number in range(101, 122) and number % 2 != 0:
                if letter in list_of_wheel_chair_seats and number in range(109, 122):
                    continue
                elif number in orchestra_left_seats:
                    my_cursor.execute(mysql_form.format(letter, number, 'Left', 'Orchestra'))
                    my_db.commit()
                elif letter == 'A' and number in range(107, 114):
                    my_cursor.execute(mysql_form.format(letter, number, 'Left', 'Side'))
                    my_db.commit()
                elif letter in list_of_main_right_seats_1 and number in range(107, 116):
                    my_cursor.execute(mysql_form.format(letter, number, 'Left', 'Side'))
                    my_db.commit()
                elif letter in list_of_main_right_seats_2 and number in range(107, 118):
                    my_cursor.execute(mysql_form.format(letter, number, 'Left', 'Side'))
                    my_db.commit()
                elif letter in list_of_main_right_seats_3 and number in range(107, 120):
                    my_cursor.execute(mysql_form.format(letter, number, 'Left', 'Side'))
                    my_db.commit()
                elif letter in list_of_main_right_seats_4 and number in range(107, 122):
                    my_cursor.execute(mysql_form.format(letter, number, 'Left', 'Side'))
                    my_db.commit()
            else:
                continue


def populate_data_for_middle_balcony_seats(list_of_letters, list_of_numbers):
    mysql_form = "Insert into Seat (SeatRow_new_SeatRow, SeatNum_new_SeatNum, Section, Side, PricingTier, Wheelchair)" \
                 "values ('{0}',{1}, 'Balcony', 'Middle', '{2}', false)"
    list_of_orchestra_seats = {'BB', 'CC', 'DD'}
    list_of_upper_balcony_seats_1 = {'EE', 'FF'}
    list_of_upper_balcony_seats_2 = {'GG', 'HH'}
    for letter in list_of_letters:
        for number in list_of_numbers:
            if letter == 'AA' and number in range(1, 14):
                my_cursor.execute(mysql_form.format(letter, number, 'Orchestra'))
                my_db.commit()
            elif letter in list_of_orchestra_seats and number in range(1, 15):
                my_cursor.execute(mysql_form.format(letter, number, 'Orchestra'))
                my_db.commit()
            elif letter in list_of_upper_balcony_seats_1 and number in range(1, 11):
                my_cursor.execute(mysql_form.format(letter, number, 'Upper Balcony'))
                my_db.commit()
            elif letter in list_of_upper_balcony_seats_2 and number in range(1, 12):
                my_cursor.execute(mysql_form.format(letter, number, 'Upper Balcony'))
                my_db.commit()
            else:
                continue


def populate_data_for_left_balcony_seats(list_of_letters, list_of_numbers):
    mysql_form = "Insert into Seat (SeatRow_new_SeatRow, SeatNum_new_SeatNum, Section, Side, PricingTier, Wheelchair)" \
                 "values ('{0}',{1}, 'Balcony', 'Left', '{2}', false)"
    list_of_side_seats_1 = {'AA', 'BB', 'CC'}
    list_of_side_seats_2 = {'DD'}
    list_of_side_seats_3 = {'EE', 'FF'}
    list_of_side_seats_4 = {'GG'}
    list_of_side_seats_5 = {'HH'}

    for letter in list_of_letters:
        for number in list_of_numbers:
            if number in range(101, 126) and number % 2 != 0:
                if letter in list_of_side_seats_1 and number in range(101, 124):
                    my_cursor.execute(mysql_form.format(letter, number, 'Side'))
                    my_db.commit()
                elif letter in list_of_side_seats_2 and number in range(101, 126):
                    my_cursor.execute(mysql_form.format(letter, number, 'Side'))
                    my_db.commit()
                elif letter in list_of_side_seats_3 and number in range(101, 122):
                    my_cursor.execute(mysql_form.format(letter, number, 'Upper Balcony'))
                    my_db.commit()
                elif letter in list_of_side_seats_4 and number in range(101, 120):
                    my_cursor.execute(mysql_form.format(letter, number, 'Upper Balcony'))
                    my_db.commit()
                elif letter in list_of_side_seats_5 and number in range(101, 118):
                    my_cursor.execute(mysql_form.format(letter, number, 'Upper Balcony'))
                    my_db.commit()
                else:
                    continue


def populate_data_for_right_balcony_seats(list_of_letters, list_of_numbers):
    mysql_form = "Insert into Seat (SeatRow_new_SeatRow, SeatNum_new_SeatNum, Section, Side, PricingTier, Wheelchair)" \
                 "values ('{0}',{1}, 'Balcony', 'Right', '{2}', false)"
    list_of_side_seats_1 = {'AA', 'BB', 'CC'}
    list_of_side_seats_2 = {'DD'}
    list_of_side_seats_3 = {'EE', 'FF'}
    list_of_side_seats_4 = {'GG'}
    list_of_side_seats_5 = {'HH'}

    for letter in list_of_letters:
        for number in list_of_numbers:
            if len(letter) == 2 and number in range(102, 127) and number % 2 == 0:
                if letter in list_of_side_seats_1 and number in range(102, 125):
                    my_cursor.execute(mysql_form.format(letter, number, 'Side'))
                    my_db.commit()
                elif letter in list_of_side_seats_2 and number in range(102, 127):
                    my_cursor.execute(mysql_form.format(letter, number, 'Side'))
                    my_db.commit()
                elif letter in list_of_side_seats_3 and number in range(102, 123):
                    my_cursor.execute(mysql_form.format(letter, number, 'Upper Balcony'))
                    my_db.commit()
                elif letter in list_of_side_seats_4 and number in range(102, 121):
                    my_cursor.execute(mysql_form.format(letter, number, 'Upper Balcony'))
                    my_db.commit()
                elif letter in list_of_side_seats_5 and number in range(102, 119):
                    my_cursor.execute(mysql_form.format(letter, number, 'Upper Balcony'))
                    my_db.commit()
                else:
                    continue


if __name__ == '__main__':
    pw = keyring.get_password('mysql', 'root')
    my_db = mysql.connector.connect(host='localhost', user='root', password=pw, database='theater')
    my_cursor = my_db.cursor()
    populate_data_for_wheel_chair_seat(get_list_of_letters(), get_list_of_numbers())
    populate_data_for_left_main_floor(get_list_of_letters(), get_list_of_numbers())
    populate_data_for_right_main_floor(get_list_of_letters(), get_list_of_numbers())
    populate_data_for_middle_main_floor_(get_list_of_letters(), get_list_of_numbers())
    populate_data_for_middle_balcony_seats(get_list_of_letters(), get_list_of_numbers())
    populate_data_for_left_balcony_seats(get_list_of_letters(), get_list_of_numbers())
    populate_data_for_right_balcony_seats(get_list_of_letters(), get_list_of_numbers())
    my_db.close()
