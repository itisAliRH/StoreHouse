import sys
import os
import time
import sqlite3
from subprocess import call


def connect_db():
    clear()
    conn = sqlite3.connect('af.db')
    print('Database connected successfully!')
    time.sleep(1)


def clear():
    tmp = call('clear' if os.name == 'posix' else 'cls')


def main_menu():
    clear()
    print('*****Main Menu*****', '\n')
    print('Please select:')
    choice = input("""\nA: Manipulate Data \nB: Reports\n0:Exit\n""")

    if choice == 'A' or choice == 'a':
        mdata_menu()
    elif choice == 'B' or choice == 'b':
        reports_menu()
    elif choice == '0':
        clear()
        print('if you want to exit, type Yes:')
        ex = input()
        if ex == 'Yes':
            clear()
            sys.exit()
        else:
            main_menu()
    else:
        retry()
        main_menu()


def mdata_menu():
    clear()
    print('*****Manipulate Data Menu*****')
    print('Please select:')
    choice = input("""\nA: Items\nB: Staffs\nC: Store Houses\nD:Stock\n\n0:Back\n""")
    if choice == 'A' or choice == 'a':
        items_menu()
    elif choice == 'B' or choice == 'b':
        staffs_menu()
    elif choice == 'C' or choice == 'c':
        house_menu()
    elif choice == 'D' or choice == 'd':
        stock_menu()
    elif choice == '0':
        main_menu()
    else:
        retry()
        mdata_menu()


def items_menu():
    pass


def staffs_menu():
    pass


def house_menu():
    pass


def stock_menu():
    pass


def reports_menu():
    clear()
    print('*****Reports Menu*****')
    print('Please Select:')
    choice = input(
        """\nA: Number of items available in all store houses\nB:Value of each store house\nC:staff names and""")


def retry():
    clear()
    print("Try Again!!")
    time.sleep(1)


connect_db()
main_menu()
